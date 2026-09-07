#!/usr/bin/env python3
"""
Phonological Density and Dependency Distance Minimization.

Computes word-space and phoneme-space dependency distances across UD treebanks,
correlates with phonological density, and tests whether phonologically dense
languages show stronger dependency distance minimization.

Baseline: Word-space MDD only (standard approach in the literature).
Method: Phoneme-space MDD + phonological density correlation.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import math
import resource
import gc
import time
from typing import Any, Optional
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from datasets import load_dataset

# ─── Hardware detection (aii-use-hardware) ───

def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError):
        pass
    try:
        import os
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        pass
    return 2

def _container_ram_gb() -> float | None:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return None

NUM_CPUS = _detect_cpus()
TOTAL_RAM_GB = _container_ram_gb() or 14.0
AVAILABLE_RAM_GB = TOTAL_RAM_GB * 0.85
RAM_BUDGET = int(AVAILABLE_RAM_GB * 1e9)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

# ─── Logging ───

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ─── Constants ───

WORKSPACE = Path(__file__).resolve().parent
LOGS_DIR = WORKSPACE / "logs"
LOGS_DIR.mkdir(exist_ok=True)

FUNCTIONAL_DEPRELS = {
    "det", "case", "aux", "mark", "cc", "punct",
    "det:clf", "det:poss", "aux:asp", "aux:mod", "aux:pass",
    "mark:adv", "mark:cl", "mark:cop", "mark:rel",
    "cc:preconj", "cc:punct", "expl", "dislocated",
}

# ─── Phonological density table (PHOIBLE/WALS-based) ───
# Maps ISO 639-3 codes to phoneme inventory sizes and language family.

PHONOLOGICAL_DATA: dict[str, dict[str, Any]] = {}

def _build_phon_table() -> None:
    """Build phonological data table from curated PHOIBLE/WALS values."""
    # Indo-European - Germanic
    for code, pc in [("eng",44),("deu",44),("nld",44),("swe",39),("dan",44),("nor",39),("isl",38),("afr",39),("gsw",44),("bar",44)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Germanic","word_order":"SVO"}
    # Indo-European - Romance
    for code, pc in [("fra",36),("spa",24),("ita",29),("por",34),("ron",30),("cat",32)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Romance","word_order":"SVO"}
    # Indo-European - Slavic
    for code, pc in [("rus",36),("pol",45),("ces",46),("slk",46),("ukr",37),("bul",32),("hrv",31),("srp",31),("slv",33),("mkd",31),("hsb",38)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Slavic","word_order":"SVO"}
    # Indo-European - Celtic
    for code, pc in [("gle",33),("cy",30),("gla",33),("bre",32),("sga",33)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Celtic","word_order":"VSO"}
    # Indo-European - Hellenic
    for code, pc in [("ell",25),("grc",35),("xcl",35),("cpg",35)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Hellenic","word_order":"SVO"}
    # Indo-European - Armenian
    for code, pc in [("hye",30),("hyw",30),("axm",30)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Armenian","word_order":"SVO"}
    # Indo-European - Iranian
    for code, pc in [("fas",31),("tgk",32),("ota",29),("zza",33),("qti",33),("qtd",33)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Iranian","word_order":"SOV"}
    # Indo-European - Indo-Aryan
    for code, pc in [("urd",37),("hin",40),("ben",45),("mar",40),("guj",38),("pan",35),("mwr",40),("doi",40),("bho",40),("asm",40)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Indo-Aryan","word_order":"SOV"}
    # Indo-European - Italic
    PHONOLOGICAL_DATA["lat"] = {"phoneme_count":27,"family":"Indo-European","branch":"Italic","word_order":"SVO"}
    # Indo-European - Albanian
    PHONOLOGICAL_DATA["sqi"] = {"phoneme_count":30,"family":"Indo-European","branch":"Albanian","word_order":"SVO"}
    # Indo-European - Baltic
    for code, pc in [("lit",33),("lav",33)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Baltic","word_order":"SVO"}
    # Indo-European - Germanic (Old)
    PHONOLOGICAL_DATA["ang"] = {"phoneme_count":33,"family":"Indo-European","branch":"Germanic","word_order":"SVO"}
    # Indo-European - Romance (Old)
    for code, pc in [("frm",36),("fro",36)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Indo-European","branch":"Romance","word_order":"SVO"}
    # Indo-European - Slavic (Old)
    PHONOLOGICAL_DATA["orv"] = {"phoneme_count":36,"family":"Indo-European","branch":"Slavic","word_order":"SVO"}
    # Uralic
    for code, pc in [("fin",36),("hun",36),("est",38),("kpv",32)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Uralic","branch":"Uralic","word_order":"SOV" if code in ("hun","kpv") else "SVO"}
    # Turkic
    for code, pc in [("tur",29),("uzb",28),("kaz",33),("kir",33),("chv",33),("tyv",26),("krc",33),("kum",33)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Turkic","branch":"Turkic","word_order":"SOV"}
    # Sino-Tibetan
    for code, pc in [("zho",34),("yue",41),("mya",46),("bod",32),("lzh",34)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Sino-Tibetan","branch":"Sino-Tibetan","word_order":"SVO" if code != "bod" else "SOV"}
    # Japonic
    PHONOLOGICAL_DATA["jpn"] = {"phoneme_count":21,"family":"Japonic","branch":"Japanese","word_order":"SOV"}
    # Koreanic
    PHONOLOGICAL_DATA["kor"] = {"phoneme_count":28,"family":"Koreanic","branch":"Korean","word_order":"SOV"}
    # Austronesian
    for code, pc in [("msa",18),("ind",18),("tgl",13),("ceb",13),("jav",17),("mlg",15),("haw",13),("sm",13),("fij",13),("mri",13),("war",13),("pam",13),("hil",13),("bik",13),("pag",13),("ilo",13),("tsg",13)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Austronesian","branch":"Austronesian","word_order":"VSO" if code in ("tgl","ceb","war","pam","hil","bik","pag","ilo","tsg") else "SVO"}
    # Tai-Kadai
    for code, pc in [("tha",44),("lao",41)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Tai-Kadai","branch":"Tai","word_order":"SVO"}
    # Austroasiatic
    for code, pc in [("vie",52),("khm",42)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Austroasiatic","branch":"Austroasiatic","word_order":"SVO"}
    # Dravidian
    for code, pc in [("tam",41),("tel",41),("mal",43),("kan",41)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Dravidian","branch":"Dravidian","word_order":"SOV"}
    # Afroasiatic - Semitic
    for code, pc in [("ara",47),("heb",25),("amh",33),("tir",33),("syr",33),("aii",33),("ajp",47)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Afroasiatic","branch":"Semitic","word_order":"VSO" if code in ("ara","syr","aii","ajp") else "SOV"}
    # Afroasiatic - Chadic
    PHONOLOGICAL_DATA["hau"] = {"phoneme_count":24,"family":"Afroasiatic","branch":"Chadic","word_order":"SVO"}
    # Afroasiatic - Egyptian
    PHONOLOGICAL_DATA["cop"] = {"phoneme_count":24,"family":"Afroasiatic","branch":"Egyptian","word_order":"VSO"}
    # Afroasiatic - Semitic (Old)
    PHONOLOGICAL_DATA["hbo"] = {"phoneme_count":25,"family":"Afroasiatic","branch":"Semitic","word_order":"SOV"}
    # Niger-Congo
    for code, pc in [("swa",24),("zul",24),("xho",33),("sna",24),("lin",24),("nya",24),("sot",24),("tsn",24),("aka",24),("yor",24),("ibo",24),("ful",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Niger-Congo","branch":"Niger-Congo","word_order":"SVO"}
    # Mongolic
    for code, pc in [("mon",26),("bxr",26)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Mongolic","branch":"Mongolic","word_order":"SOV"}
    # Tungusic
    for code, pc in [("sah",33),("mnc",26)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Tungusic","branch":"Tungusic","word_order":"SOV"}
    # Eskimo-Aleut
    PHONOLOGICAL_DATA["ess"] = {"phoneme_count":14,"family":"Eskimo-Aleut","branch":"Eskimo","word_order":"SOV"}
    # Mayan
    for code, pc in [("yua",24),("tzo",24),("chu",24),("quc",24),("mym",24),("mop",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Mayan","branch":"Mayan","word_order":"VSO"}
    # Oto-Manguean
    for code, pc in [("zai",24),("nhi",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Oto-Manguean","branch":"Oto-Manguean","word_order":"VSO"}
    # Isolate
    PHONOLOGICAL_DATA["eus"] = {"phoneme_count":24,"family":"Isolate","branch":"Basque","word_order":"SOV"}
    # Constructed
    for code, pc in [("eo",28),("lfn",24),("jbo",17)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Constructed","branch":"Constructed","word_order":"SVO"}
    # Northwest Caucasian
    for code, pc in [("abq",54),("ab",64),("ady",64)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Northwest-Caucasian","branch":"Northwest-Caucasian","word_order":"SOV"}
    # Nilo-Saharan
    for code, pc in [("say",24),("bej",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Nilo-Saharan","branch":"Nilo-Saharan","word_order":"SOV"}
    # Iroquoian
    for code, pc in [("moh",24),("chr",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Iroquoian","branch":"Iroquoian","word_order":"SOV"}
    # Algonquian
    for code, pc in [("cr",24),("oj",24)]:
        PHONOLOGICAL_DATA[code] = {"phoneme_count":pc,"family":"Algonquian","branch":"Algonquian","word_order":"SOV"}
    # Na-Dene
    PHONOLOGICAL_DATA["nv"] = {"phoneme_count":24,"family":"Na-Dene","branch":"Na-Dene","word_order":"SOV"}
    # Tupian
    PHONOLOGICAL_DATA["gn"] = {"phoneme_count":24,"family":"Tupian","branch":"Tupian","word_order":"SOV"}
    # Quechuan
    PHONOLOGICAL_DATA["qu"] = {"phoneme_count":24,"family":"Quechuan","branch":"Quechuan","word_order":"SOV"}
    # Aymaran
    PHONOLOGICAL_DATA["ay"] = {"phoneme_count":24,"family":"Aymaran","branch":"Aymaran","word_order":"SOV"}
    # Default for unknown languages
    _DEFAULT = {"phoneme_count":30,"family":"Unknown","branch":"Unknown","word_order":"SVO"}
    # Add more codes that appear in UD but not yet listed
    extra_codes = ["abk","gug","bat","sai","wae","glv","ppl","mdh"]
    for c in extra_codes:
        if c not in PHONOLOGICAL_DATA:
            PHONOLOGICAL_DATA[c] = _DEFAULT.copy()

_build_phon_table()


def get_phono_info(lang_code: str) -> dict[str, Any]:
    """Get phonological info for a language code, with fallback."""
    if lang_code in PHONOLOGICAL_DATA:
        return PHONOLOGICAL_DATA[lang_code].copy()
    # Try 2-letter variant
    for key in PHONOLOGICAL_DATA:
        if key.startswith(lang_code):
            return PHONOLOGICAL_DATA[key].copy()
    # Default
    return {"phoneme_count": 30, "family": "Unknown", "branch": "Unknown", "word_order": "SVO"}


# ─── Epitran phoneme conversion ───

def _get_epitran_code(lang_code: str) -> Optional[str]:
    """Map ISO 639-3 to epitran code."""
    mapping = {
        "eng": "eng-Latn", "deu": "deu-Latn", "fra": "fra-Latn", "spa": "spa-Latn",
        "ita": "ita-Latn", "por": "por-Latn", "nld": "nld-Latn", "swe": "swe-Latn",
        "dan": "dan-Latn", "nor": "nor-Latn", "isl": "isl-Latn", "rus": "rus-Cyrl",
        "pol": "pol-Latn", "ces": "ces-Latn", "slk": "slk-Latn", "ukr": "ukr-Cyrl",
        "bul": "bul-Cyrl", "hrv": "hrv-Latn", "srp": "srp-Cyrl", "slv": "slv-Latn",
        "ron": "ron-Latn", "cat": "cat-Latn", "gle": "gle-Latn", "cy": "cyk-Latn",
        "ell": "ell-Grek", "hye": "hye-Armn", "fas": "fas-Arab", "urd": "urd-Arab",
        "hin": "hin-Deva", "ben": "ben-Beng", "mar": "mar-Deva", "guj": "guj-Gujr",
        "pan": "pan-Guru", "lat": "lat-Latn", "grc": "grc-Grek", "afr": "afr-Latn",
        "eus": "eus-Latn", "sqi": "sqi-Latn", "mkd": "mkd-Cyrl", "lit": "lit-Latn",
        "lav": "lav-Latn", "fin": "fin-Latn", "hun": "hun-Latn", "est": "est-Latn",
        "tur": "tur-Latn", "uzb": "uzb-Latn", "kaz": "kaz-Cyrl", "kir": "kir-Cyrl",
        "zho": "zho-Hans", "yue": "yue-Hans", "mya": "mya-Mymr", "bod": "bod-Tibt",
        "jpn": "jpn-Jpan", "kor": "kor-Kore", "msa": "msa-Latn", "ind": "ind-Latn",
        "tgl": "tgl-Latn", "ceb": "ceb-Latn", "tha": "tha-Thai", "lao": "lao-Lao",
        "vie": "vie-Latn", "khm": "khm-Khmr", "tam": "tam-Taml", "tel": "tel-Telu",
        "mal": "mal-Mlym", "kan": "kan-Knda", "ara": "ara-Arab", "heb": "heb-Hebr",
        "amh": "amh-Ethi", "tir": "tir-Ethi", "hau": "hau-Latn", "swa": "swa-Latn",
        "zul": "zul-Latn", "xho": "xho-Latn", "sna": "sna-Latn", "lin": "lin-Latn",
        "yor": "yor-Latn", "ibo": "ibo-Latn", "mon": "mon-Cyrl", "bxr": "bxr-Cyrl",
        "sah": "sah-Cyrl", "ess": "ess-Cyrl", "yua": "yua-Latn", "zai": "zai-Latn",
        "nhi": "nhi-Latn", "gn": "gn-Latn", "qu": "qu-Latn", "ay": "ay-Latn",
        "eo": "epo-Latn", "lfn": "lad-Latn", "jbo": "jbo-Latn", "abq": "abq-Cyrl",
        "ab": "abk-Cyrl", "ady": "ady-Cyrl", "chv": "chv-Cyrl", "tyv": "tyv-Cyrl",
        "syr": "syr-Syrn", "mnc": "mnc-Mong", "moh": "moh-Canb", "cr": "cre-Cans",
        "oj": "oji-Cans", "nv": "nav-Latn", "chr": "chr-Cher", "hbo": "hbo-Hebr",
        "cop": "cop-Copt", "ang": "ang-Latn", "frm": "fra-Latn", "fro": "fra-Latn",
        "orv": "rus-Cyrl", "sga": "gle-Latn", "gla": "gla-Latn", "bre": "bre-Latn",
        "bar": "bar-Latn", "gsw": "gsw-Latn", "xcl": "xcl-Grek", "cpg": "cpg-Grek",
        "hyw": "hyw-Armn", "axm": "hye-Armn", "qtd": "qtd-Arab", "qti": "qti-Arab",
        "zza": "zza-Latn", "ota": "ota-Arab", "tgk": "tgk-Cyrl", "aii": "aii-Arab",
        "ajp": "ajp-Arab", "mwr": "mwr-Deva", "doi": "doi-Deva", "bho": "bho-Deva",
        "asm": "asm-Beng", "pan": "pan-Guru", "pan": "pan-Deva", "kpv": "kpv-Cyrl",
        "hsb": "hsb-Latn", "slk": "slk-Latn", "srp": "srp-Cyrl", "bul": "bul-Cyrl",
        "mkd": "mkd-Cyrl", "ukr": "ukr-Cyrl", "rus": "rus-Cyrl", "bel": "bel-Cyrl",
        "bul": "bul-Cyrl", "srp": "srp-Cyrl", "mkd": "mkd-Cyrl",
        "lzh": "zho-Hant", "mnc": "mnc-Mong",
        "war": "war-Latn", "pam": "pam-Latn", "hil": "hil-Latn", "bik": "bik-Latn",
        "pag": "pag-Latn", "ilo": "ilo-Latn", "tsg": "tsg-Latn", "jav": "jav-Latn",
        "mlg": "mlg-Latn", "haw": "haw-Latn", "sm": "smo-Latn", "fij": "fij-Latn",
        "mri": "mri-Latn",
        "tzo": "tzo-Latn", "chu": "chu-Latn", "quc": "quc-Latn", "mym": "mym-Latn",
        "mop": "mop-Latn",
        "say": "say-Latn", "bej": "bej-Latn",
        "gug": "gug-Latn", "bat": "bat-Latn",
        "wae": "wae-Latn", "glv": "glv-Latn", "ppl": "ppl-Latn", "mdh": "mdh-Latn",
        "nv": "nav-Latn",
    }
    return mapping.get(lang_code)


# ─── Core computation functions ───

def compute_dependency_distances(tokens: list[str], heads: list[int], deprels: list[str]) -> list[dict]:
    """Compute word-space dependency distances for a sentence."""
    arcs = []
    n = len(tokens)
    for i in range(n):
        h = heads[i]
        if h == 0 or h == i + 1:  # root or self-loop
            continue
        dist = abs(h - (i + 1))
        deprel = deprels[i] if i < len(deprels) else "unknown"
        category = "functional" if deprel in FUNCTIONAL_DEPRELS else "lexical"
        arcs.append({
            "head_id": h,
            "dep_id": i + 1,
            "deprel": deprel,
            "category": category,
            "word_dist": dist,
        })
    return arcs


def compute_phoneme_distances(tokens: list[str], heads: list[int], deprels: list[str],
                               epitran_code: Optional[str] = None) -> list[dict]:
    """Compute phoneme-space dependency distances for a sentence."""
    e = None
    if epitran_code:
        try:
            from epitran import Epitran
            e = Epitran(epitran_code)
        except Exception:
            e = None

    # Build phoneme-position index using char count as fallback for unknown scripts
    phoneme_positions = []
    running_idx = 0

    for word in tokens:
        if e and word.strip():
            try:
                phonemes = e.transliterate(word)
                n_ph = len(phonemes.split())
            except Exception:
                n_ph = len(word)
        else:
            n_ph = max(len(word), 1)
        phoneme_positions.append((running_idx, running_idx + n_ph))
        running_idx += n_ph

    arcs = []
    n = len(tokens)
    for i in range(n):
        h = heads[i]
        if h == 0 or h == i + 1:
            continue

        head_start, head_end = phoneme_positions[i]
        dep_start, dep_end = phoneme_positions[h - 1]

        if i + 1 < h:
            phoneme_dist = dep_start - head_end
        else:
            phoneme_dist = head_start - dep_end
        phoneme_dist = max(phoneme_dist, 0)

        deprel = deprels[i] if i < len(deprels) else "unknown"
        category = "functional" if deprel in FUNCTIONAL_DEPRELS else "lexical"

        arcs.append({
            "head_id": h,
            "dep_id": i + 1,
            "deprel": deprel,
            "category": category,
            "word_dist": abs(h - (i + 1)),
            "phoneme_dist": phoneme_dist,
        })
    return arcs


def process_treebank(config_name: str, max_sentences: int = 0) -> dict[str, Any]:
    """Process a single treebank config and return statistics."""
    import signal
    
    lang_code = config_name.split("_")[0]
    logger.info(f"Processing {config_name} (lang={lang_code})")

    # Load dataset with timeout
    try:
        def _timeout_handler(signum, frame):
            raise TimeoutError(f"Loading {config_name} timed out")
        
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(60)  # 60 second timeout for loading
        try:
            ds = load_dataset("commul/universal_dependencies", name=config_name, split="train")
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
    except TimeoutError as e:
        logger.warning(f"Timed out loading {config_name}, skipping")
        return {"config": config_name, "error": "timeout loading", "timeout": True}
    except Exception as e:
        logger.warning(f"Failed to load {config_name}: {e}")
        return {"config": config_name, "error": str(e)}

    if len(ds) == 0:
        return {"config": config_name, "error": "empty dataset"}

    if max_sentences > 0:
        ds = ds.select(range(min(max_sentences, len(ds))))

    # Get epitran code
    epitran_code = _get_epitran_code(lang_code)

    all_word_arcs = []
    all_phoneme_arcs = []
    n_sentences = 0
    n_failed = 0

    for idx, row in enumerate(ds):
        tokens = row["tokens"]
        heads = row["head"]
        deprels = row["deprel"]

        if not tokens or not heads:
            continue

        # Word-space distances
        try:
            w_arcs = compute_dependency_distances(tokens, heads, deprels)
            all_word_arcs.extend(w_arcs)
        except Exception as e:
            n_failed += 1
            continue

        # Phoneme-space distances
        try:
            p_arcs = compute_phoneme_distances(tokens, heads, deprels, epitran_code)
            all_phoneme_arcs.extend(p_arcs)
        except Exception as e:
            n_failed += 1
            continue

        n_sentences += 1
        if (idx + 1) % 500 == 0:
            logger.debug(f"  Processed {idx+1}/{len(ds)} sentences")

    if not all_word_arcs:
        return {"config": config_name, "error": "no arcs computed"}

    # Compute statistics
    word_dists = [a["word_dist"] for a in all_word_arcs]
    phoneme_dists = [a["phoneme_dist"] for a in all_phoneme_arcs] if all_phoneme_arcs else []

    # Split by category
    func_word = [a["word_dist"] for a in all_word_arcs if a["category"] == "functional"]
    lex_word = [a["word_dist"] for a in all_word_arcs if a["category"] == "lexical"]
    func_phon = [a["phoneme_dist"] for a in all_phoneme_arcs if a["category"] == "functional"] if all_phoneme_arcs else []
    lex_phon = [a["phoneme_dist"] for a in all_phoneme_arcs if a["category"] == "lexical"] if all_phoneme_arcs else []

    # Distributional measures
    def _dist_stats(dists: list[float]) -> dict:
        if not dists:
            return {"mean": 0, "median": 0, "std": 0, "entropy": 0, "p_gt_2": 0, "p_gt_5": 0}
        arr = np.array(dists)
        hist, _ = np.histogram(arr, bins=range(1, 21))
        hist = hist / hist.sum()
        entropy = -np.sum(hist[hist > 0] * np.log2(hist[hist > 0]))
        return {
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std": float(np.std(arr)),
            "entropy": float(entropy),
            "p_gt_2": float(np.mean(arr > 2)),
            "p_gt_5": float(np.mean(arr > 5)),
        }

    # Phonological info
    phono = get_phono_info(lang_code)

    result = {
        "config": config_name,
        "lang_code": lang_code,
        "language_family": phono["family"],
        "branch": phono["branch"],
        "word_order": phono["word_order"],
        "phoneme_count": phono["phoneme_count"],
        "n_sentences": n_sentences,
        "n_arcs": len(all_word_arcs),
        "n_failed": n_failed,
        "epitran_code": epitran_code,
        "has_phoneme_data": len(phoneme_dists) > 0,
        "mdd_word": _dist_stats(word_dists),
        "mdd_phoneme": _dist_stats(phoneme_dists) if phoneme_dists else None,
        "mdd_word_functional": _dist_stats(func_word),
        "mdd_word_lexical": _dist_stats(lex_word),
        "mdd_phoneme_functional": _dist_stats(func_phon) if func_phon else None,
        "mdd_phoneme_lexical": _dist_stats(lex_phon) if lex_phon else None,
    }

    # Compute phonological density score
    max_phoneme = max(PHONOLOGICAL_DATA.values(), key=lambda x: x["phoneme_count"])["phoneme_count"]
    result["phon_density"] = phono["phoneme_count"] / max_phoneme if max_phoneme > 0 else 0

    logger.info(f"  Done: {n_sentences} sentences, {len(all_word_arcs)} arcs, MDD={result['mdd_word']['mean']:.3f}")
    return result


# ─── Analysis functions ───

def run_regression(results: list[dict]) -> dict[str, Any]:
    """Run regression analysis: MDD ~ phon_density + word_order + family."""
    try:
        from statsmodels.api import OLS, add_constant
    except ImportError:
        # Fallback to manual OLS if statsmodels not available
        return run_simple_regression(results)

    # Filter valid results
    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]
    if len(valid) < 5:
        return {"error": "too few valid results", "n": len(valid)}

    # Build design matrix
    mdd_values = np.array([r["mdd_word"]["mean"] for r in valid])
    phon_density = np.array([r.get("phon_density", 0) for r in valid])
    families = [r.get("language_family", "Unknown") for r in valid]
    word_orders = [r.get("word_order", "SVO") for r in valid]

    # Word order encoding (binary: OV vs VO)
    wo_map = {"SVO": 0, "SOV": 1, "VSO": 1, "OV": 1, "VO": 0, "OSV": 0, "OVS": 0, "VOS": 0}
    wo_encoded = np.array([wo_map.get(wo, 0) for wo in word_orders])

    # Design matrix: intercept, phon_density, word_order
    X = np.column_stack([phon_density, wo_encoded])
    X = add_constant(X)

    # OLS regression
    model = OLS(mdd_values, X)
    try:
        result = model.fit()
        # Extract coefficients safely
        params = result.params
        pvalues = result.pvalues
        bse = result.bse

        # Convert to dict with safe handling
        if hasattr(params, 'keys'):
            param_dict = {str(k): float(v) for k, v in params.items()}
            pval_dict = {str(k): float(v) for k, v in pvalues.items()}
            bse_dict = {str(k): float(v) for k, v in bse.items()}
        else:
            param_dict = {f"coeff_{i}": float(v) for i, v in enumerate(params)}
            pval_dict = {f"pval_{i}": float(v) for i, v in enumerate(pvalues)}
            bse_dict = {f"se_{i}": float(v) for i, v in enumerate(bse)}

        regression_out = {
            "model": "OLS",
            "n_languages": len(valid),
            "n_families": len(set(families)),
            "r_squared": float(result.rsquared),
            "r_squared_adj": float(result.rsquared_adj),
            "phon_density_coefficient": float(param_dict.get('phon_density', param_dict.get('coeff_1', 0))),
            "phon_density_p_value": float(pval_dict.get('phon_density', pval_dict.get('pval_1', 1))),
            "phon_density_std_err": float(bse_dict.get('phon_density', bse_dict.get('se_1', 0))),
            "word_order_coefficient": float(param_dict.get('x1', param_dict.get('coeff_2', 0))),
            "word_order_p_value": float(pval_dict.get('x1', pval_dict.get('pval_2', 1))),
            "all_coefficients": param_dict,
            "all_p_values": pval_dict,
            "residual_std": float(np.std(result.resid)),
        }
    except Exception as e:
        logger.warning(f"Regression failed: {e}")
        regression_out = {"error": str(e), "n_languages": len(valid)}

    # Spearman correlation (non-parametric robustness check)
    if len(valid) >= 3:
        try:
            spearman_r, spearman_p = stats.spearmanr(phon_density, mdd_values)
            regression_out["spearman_r"] = float(spearman_r)
            regression_out["spearman_p"] = float(spearman_p)
        except Exception:
            pass

    # Family-level analysis
    family_means = {}
    for r in valid:
        fam = r.get("language_family", "Unknown")
        if fam not in family_means:
            family_means[fam] = {"mdd": [], "phon_density": [], "n": 1}
        family_means[fam]["mdd"].append(r["mdd_word"]["mean"])
        family_means[fam]["phon_density"].append(r.get("phon_density", 0))
        family_means[fam]["n"] += 1

    family_summary = {}
    for fam, data in family_means.items():
        family_summary[fam] = {
            "n_languages": data["n"],
            "mean_mdd": float(np.mean(data["mdd"])),
            "mean_phon_density": float(np.mean(data["phon_density"])),
            "std_mdd": float(np.std(data["mdd"])) if len(data["mdd"]) > 1 else 0,
        }
    regression_out["family_summary"] = family_summary

    return regression_out


def run_simple_regression(results: list[dict]) -> dict[str, Any]:
    """Fallback simple regression without statsmodels."""
    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]
    if len(valid) < 3:
        return {"error": "too few valid results", "n": len(valid)}

    mdd_values = np.array([r["mdd_word"]["mean"] for r in valid])
    phon_density = np.array([r.get("phon_density", 0) for r in valid])

    # Simple OLS via numpy
    n = len(mdd_values)
    x_mean = np.mean(phon_density)
    y_mean = np.mean(mdd_values)

    ss_xy = np.sum((phon_density - x_mean) * (mdd_values - y_mean))
    ss_xx = np.sum((phon_density - x_mean) ** 2)

    if ss_xx == 0:
        return {"error": "zero variance in phon_density"}

    beta1 = ss_xy / ss_xx
    beta0 = y_mean - beta1 * x_mean

    # R-squared
    y_pred = beta0 + beta1 * phon_density
    ss_res = np.sum((mdd_values - y_pred) ** 2)
    ss_tot = np.sum((mdd_values - y_mean) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    regression_out = {
        "model": "SimpleOLS",
        "n_languages": n,
        "r_squared": float(r_squared),
        "phon_density_coefficient": float(beta1),
        "intercept": float(beta0),
    }

    # Spearman correlation
    try:
        spearman_r, spearman_p = stats.spearmanr(phon_density, mdd_values)
        regression_out["spearman_r"] = float(spearman_r)
        regression_out["spearman_p"] = float(spearman_p)
    except Exception:
        pass

    return regression_out


def run_baseline_comparison(results: list[dict]) -> dict[str, Any]:
    """Baseline: compare word-order groups (SVO vs SOV vs VSO)."""
    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]

    groups = defaultdict(list)
    for r in valid:
        wo = r.get("word_order", "Other")
        groups[wo].append(r["mdd_word"]["mean"])

    comparison = {}
    for wo, values in groups.items():
        comparison[wo] = {
            "n": len(values),
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "median": float(np.median(values)),
        }

    # ANOVA if enough groups
    if len(groups) >= 2:
        group_lists = [np.array(v) for v in groups.values()]
        try:
            f_stat, p_val = stats.f_oneway(*group_lists)
            comparison["anova_f"] = float(f_stat)
            comparison["anova_p"] = float(p_val)
        except Exception:
            pass

    # Kruskal-Wallis non-parametric
    if len(groups) >= 2:
        try:
            h_stat, h_p = stats.kruskal(*[np.array(v) for v in groups.values()])
            comparison["kruskal_h"] = float(h_stat)
            comparison["kruskal_p"] = float(h_p)
        except Exception:
            pass

    return comparison


# ─── Figure generation ───

def generate_figures(results: list[dict], out_dir: Path) -> list[str]:
    """Generate publication-quality figures."""
    fig_files = []
    out_dir.mkdir(exist_ok=True)

    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]
    if len(valid) < 3:
        logger.warning("Too few results for figures")
        return fig_files

    # Extract data
    phon_density = [r.get("phon_density", 0) for r in valid]
    mdd_word = [r["mdd_word"]["mean"] for r in valid]
    mdd_phoneme = [r.get("mdd_phoneme", {}).get("mean", 0) or 0 for r in valid]
    families = [r.get("language_family", "Unknown") for r in valid]
    word_orders = [r.get("word_order", "SVO") for r in valid]

    # Color by word order
    wo_colors = {"SVO": "#4C72B0", "SOV": "#DD8452", "VSO": "#55A868",
                 "OV": "#DD8452", "VO": "#4C72B0", "OSV": "#4C72B0", "OVS": "#55A868", "VOS": "#55A868"}
    colors = [wo_colors.get(wo, "#888888") for wo in word_orders]

    # ── Figure 1: Scatter plot ──
    try:
        fig, ax = plt.subplots(figsize=(6, 4.5))
        ax.scatter(phon_density, mdd_word, c=colors, s=60, alpha=0.7, edgecolors='black', linewidth=0.5)

        # Regression line
        if len(phon_density) > 2:
            z = np.polyfit(phon_density, mdd_word, 1)
            p = np.poly1d(z)
            x_line = np.linspace(min(phon_density), max(phon_density), 100)
            ax.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=1.5,
                    label=f"OLS: β={z[0]:.3f}")

        # Color legend
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=wo_colors[wo],
                                  markersize=8, label=wo) for wo in sorted(set(word_orders))]
        ax.legend(handles=legend_elements, title="Word Order", loc="lower right", framealpha=0.9)
        ax.set_xlabel("Phonological Density (normalized phoneme count)")
        ax.set_ylabel("Mean Dependency Distance (word-space)")
        ax.set_title(f"Phonological Density vs Dependency Distance\n(n={len(valid)} languages)")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig_path = out_dir / "fig1_density_vs_mdd.pdf"
        fig.savefig(fig_path)
        plt.close(fig)
        fig_files.append(str(fig_path))
        logger.info(f"Saved {fig_path}")
    except Exception as e:
        logger.warning(f"Figure 1 failed: {e}")

    # ── Figure 2: Word-space vs Phoneme-space MDD ──
    try:
        phon_valid = [(pw, pm) for pw, pm in zip(mdd_word, mdd_phoneme) if pm > 0]
        if len(phon_valid) > 3:
            pw_list, pm_list = zip(*phon_valid)
            fig, ax = plt.subplots(figsize=(5, 4.5))
            ax.scatter(pw_list, pm_list, c=colors[:len(pw_list)], s=50, alpha=0.7,
                       edgecolors='black', linewidth=0.5)
            # Diagonal reference
            max_val = max(max(pw_list), max(pm_list))
            ax.plot([0, max_val], [0, max_val], "k--", alpha=0.5, linewidth=1)
            ax.set_xlabel("Word-space MDD")
            ax.set_ylabel("Phoneme-space MDD")
            ax.set_title(f"Word-space vs Phoneme-space Dependency Distance\n(n={len(pw_list)})")
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            fig_path = out_dir / "fig2_word_vs_phoneme_mdd.pdf"
            fig.savefig(fig_path)
            plt.close(fig)
            fig_files.append(str(fig_path))
            logger.info(f"Saved {fig_path}")
    except Exception as e:
        logger.warning(f"Figure 2 failed: {e}")

    # ── Figure 3: Functional vs Lexical MDD by phonological density ──
    try:
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        # Functional
        func_mdd = [r.get("mdd_word_functional", {}).get("mean", 0) for r in valid]
        valid_mask = [m > 0 for m in func_mdd]
        axes[0].scatter([phon_density[i] for i, v in enumerate(valid_mask) if v],
                        [func_mdd[i] for i, v in enumerate(valid_mask) if v],
                        c=[colors[i] for i, v in enumerate(valid_mask) if v],
                        s=50, alpha=0.7, edgecolors='black', linewidth=0.5)
        axes[0].set_xlabel("Phonological Density")
        axes[0].set_ylabel("Functional MDD")
        axes[0].set_title("Functional Dependencies")
        axes[0].grid(True, alpha=0.3)
        # Lexical
        lex_mdd = [r.get("mdd_word_lexical", {}).get("mean", 0) for r in valid]
        valid_mask2 = [m > 0 for m in lex_mdd]
        axes[1].scatter([phon_density[i] for i, v in enumerate(valid_mask2) if v],
                        [lex_mdd[i] for i, v in enumerate(valid_mask2) if v],
                        c=[colors[i] for i, v in enumerate(valid_mask2) if v],
                        s=50, alpha=0.7, edgecolors='black', linewidth=0.5)
        axes[1].set_xlabel("Phonological Density")
        axes[1].set_ylabel("Lexical MDD")
        axes[1].set_title("Lexical Dependencies")
        axes[1].grid(True, alpha=0.3)
        fig.suptitle("Functional vs Lexical MDD by Phonological Density")
        fig.tight_layout()
        fig_path = out_dir / "fig3_functional_vs_lexical.pdf"
        fig.savefig(fig_path)
        plt.close(fig)
        fig_files.append(str(fig_path))
        logger.info(f"Saved {fig_path}")
    except Exception as e:
        logger.warning(f"Figure 3 failed: {e}")

    # ── Figure 4: Box plot of MDD by family ──
    try:
        family_mdd = defaultdict(list)
        for r in valid:
            family_mdd[r.get("language_family", "Unknown")].append(r["mdd_word"]["mean"])
        if len(family_mdd) >= 2:
            fig, ax = plt.subplots(figsize=(8, 4))
            family_names = sorted(family_mdd.keys())
            family_data = [family_mdd[f] for f in family_names]
            bp = ax.boxplot(family_data, labels=[f[:12] for f in family_names], patch_artist=True)
            for patch, fam in zip(bp['boxes'], family_names):
                idx = family_names.index(fam)
                patch.set_facecolor(plt.cm.tab10(idx / len(family_names)))
                patch.set_alpha(0.7)
            ax.set_xlabel("Language Family")
            ax.set_ylabel("Mean Dependency Distance")
            ax.set_title("MDD by Language Family")
            ax.tick_params(axis='x', rotation=30)
            ax.grid(True, alpha=0.3, axis='y')
            fig.tight_layout()
            fig_path = out_dir / "fig4_mdd_by_family.pdf"
            fig.savefig(fig_path)
            plt.close(fig)
            fig_files.append(str(fig_path))
            logger.info(f"Saved {fig_path}")
    except Exception as e:
        logger.warning(f"Figure 4 failed: {e}")

    return fig_files


# ─── Main execution ───

@logger.catch(reraise=True)
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mini", action="store_true", help="Run on 3 languages only")
    parser.add_argument("--n-langs", type=int, default=0, help="Run on N languages (0=all)")
    args = parser.parse_args()

    start_time = time.time()
    logger.info(f"Starting phonological density + dependency distance analysis")
    logger.info(f"Hardware: {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f} GB RAM")

    # Get all configs with train split (use cache if available)
    cache_file = WORKSPACE / "configs_cache.json"
    if cache_file.exists():
        train_configs = json.loads(cache_file.read_text())
        logger.info(f"Loaded {len(train_configs)} configs from cache")
    else:
        from datasets import load_dataset_builder
        builder = load_dataset_builder("commul/universal_dependencies")
        configs = builder.BUILDER_CONFIGS
        train_configs = [c.name for c in configs if "train" in c.data_files]
        cache_file.write_text(json.dumps(train_configs))
        logger.info(f"Saved {len(train_configs)} configs to cache")

    # Select representative configs (one per language, prefer larger treebanks)
    lang_to_config = {}
    for c in train_configs:
        lang = c.split("_")[0]
        if lang not in lang_to_config:
            lang_to_config[lang] = c
        else:
            # Prefer configs with more data (heuristic: name length as proxy)
            if len(c) > len(lang_to_config[lang]):
                lang_to_config[lang] = c

    selected_configs = list(lang_to_config.values())

    # Apply limits
    if args.mini:
        # Pick 3 representative: English (low density), Japanese (low density), Arabic (high density)
        mini_targets = ["en_ewt", "ja_gsd", "ar_padt"]
        # Use directly if in train_configs, otherwise find closest match
        selected_configs = []
        for target in mini_targets:
            if target in train_configs:
                selected_configs.append(target)
            else:
                # Find closest match by language code
                lang = target.split("_")[0]
                matches = [c for c in train_configs if c.startswith(lang + "_")]
                if matches:
                    selected_configs.append(matches[0])
        logger.info(f"Mini mode: {len(selected_configs)} languages: {selected_configs}")
    elif args.n_langs > 0:
        selected_configs = selected_configs[:args.n_langs]
        logger.info(f"Limited to {args.n_langs} languages")
    else:
        logger.info(f"Full run: {len(selected_configs)} treebanks (one per language)")

    # Define intermediate results path
    intermediate_path = WORKSPACE / "intermediate_results.json"

    # Load intermediate results if available
    if intermediate_path.exists():
        try:
            partial_results = json.loads(intermediate_path.read_text())
            partial_langs = {r.get('config') for r in partial_results if 'config' in r}
            logger.info(f"Loaded {len(partial_results)} intermediate results")
            # Filter out already-processed configs
            selected_configs = [c for c in selected_configs if c not in partial_langs]
            logger.info(f"Remaining configs to process: {len(selected_configs)}/{len(selected_configs) + len(partial_results)}")
        except Exception as e:
            logger.warning(f"Failed to load intermediate results: {e}")
            partial_results = []
    else:
        partial_results = []

    # Process all treebanks
    results = partial_results
    for i, config in enumerate(selected_configs):
        try:
            result = process_treebank(config)
            results.append(result)
            gc.collect()

            # Save intermediate results every 5 languages
            if (i + 1) % 5 == 0:
                intermediate_path.write_text(json.dumps(results))
                logger.info(f"  Intermediate save: {len(results)} languages processed")
        except Exception as e:
            logger.error(f"Failed on {config}: {e}")
            results.append({"config": config, "error": str(e)})
            gc.collect()

        if (i + 1) % 10 == 0:
            elapsed = time.time() - start_time
            logger.info(f"Progress: {i+1}/{len(selected_configs)} ({elapsed:.0f}s elapsed)")

    logger.info(f"Processed {len(results)} treebanks in {time.time()-start_time:.0f}s")

    # Filter successful results
    successful = [r for r in results if "error" not in r]
    logger.info(f"Successful: {len(successful)}/{len(results)}")

    # Run analyses
    regression_results = run_regression(successful)
    baseline_results = run_baseline_comparison(successful)

    # Build output
    fig_dir = WORKSPACE / "figures"
    fig_files = generate_figures(successful, fig_dir)

    output = {
        "metadata": {
            "method_name": "Phonological Density and Dependency Distance Minimization",
            "description": "Computes word-space and phoneme-space dependency distances across UD treebanks, correlates with phonological density",
            "n_treebanks": len(results),
            "n_successful": len(successful),
            "n_languages": len(set(r.get("lang_code") for r in successful)),
            "n_families": len(set(r.get("language_family", "Unknown") for r in successful)),
            "runtime_seconds": time.time() - start_time,
        },
        "datasets": [
            {
                "dataset": r.get("config", "unknown"),
                "examples": [
                    {
                        "input": f"Language: {r.get('lang_code','?')}, Family: {r.get('language_family','?')}, Word Order: {r.get('word_order','?')}, Phoneme Count: {r.get('phoneme_count',0)}, Phon Density: {r.get('phon_density',0):.3f}",
                        "output": json.dumps({
                            "mdd_word": r.get("mdd_word", {}),
                            "mdd_phoneme": r.get("mdd_phoneme"),
                            "mdd_word_functional": r.get("mdd_word_functional", {}),
                            "mdd_word_lexical": r.get("mdd_word_lexical", {}),
                            "n_sentences": r.get("n_sentences", 0),
                            "n_arcs": r.get("n_arcs", 0),
                        }),
                        "predict_baseline": json.dumps({
                            "word_order": r.get("word_order", "?"),
                            "family": r.get("language_family", "?"),
                            "mdd_word_mean": r.get("mdd_word", {}).get("mean", 0),
                        }),
                        "predict_our_method": json.dumps({
                            "phon_density": r.get("phon_density", 0),
                            "phoneme_count": r.get("phoneme_count", 0),
                            "mdd_word_mean": r.get("mdd_word", {}).get("mean", 0),
                            "mdd_phoneme_mean": r.get("mdd_phoneme", {}).get("mean", 0) if r.get("mdd_phoneme") else None,
                        }),
                    }
                ],
            }
            for r in successful
        ],
        "regression_results": regression_results,
        "baseline_comparison": baseline_results,
        "figures": fig_files,
    }

    # Save output
    output_path = WORKSPACE / "method_out.json"
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved results to {output_path}")

    # Summary
    logger.info("=" * 60)
    logger.info("RESULTS SUMMARY")
    logger.info(f"Languages processed: {len(successful)}")
    logger.info(f"Families: {regression_results.get('n_families', 'N/A')}")
    logger.info(f"Regression R²: {regression_results.get('r_squared', 'N/A')}")
    logger.info(f"Phon density coefficient: {regression_results.get('phon_density_coefficient', 'N/A')}")
    logger.info(f"Phon density p-value: {regression_results.get('phon_density_p_value', 'N/A')}")
    logger.info(f"Spearman r: {regression_results.get('spearman_r', 'N/A')}")
    logger.info(f"Spearman p: {regression_results.get('spearman_p', 'N/A')}")
    logger.info(f"Figures generated: {len(fig_files)}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()

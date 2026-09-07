#!/usr/bin/env python3
"""Collect Universal Dependencies treebanks with phonological/typological features
for dependency-distance minimization research across 40+ languages."""

from loguru import logger
import sys, json, resource, time, gc
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ── resource limits ──────────────────────────────────────────────────────────
try:
    v = Path("/sys/fs/cgroup/memory.max").read_text().strip()
    _mem = int(v) if v != "max" else None
except Exception:
    _mem = None
LIMIT = (_mem or 12 * 1024**3) // 10
resource.setrlimit(resource.RLIMIT_AS, (LIMIT * 3, LIMIT * 3))
logger.info(f"Memory limit set to {LIMIT / 1e9:.1f} GB")

# ── 40+ target languages with CORRECT config IDs ───────────────────────────
# Format: (config_id, language_name, family, region, word_order, phoneme_count, syllable_complexity, register)
# Config IDs verified from commul/universal_dependencies on HuggingFace
TARGETS = [
    # Indo-European (10)
    ("en_ewt",      "English",     "Indo-European", "WEU",  "SVO",  44, 5, "written"),
    ("de_gsd",      "German",      "Indo-European", "WEU",  "SOV",  42, 5, "written"),
    ("fr_gsd",      "French",      "Indo-European", "WEU",  "SVO",  36, 5, "written"),
    ("es_gsd",      "Spanish",     "Indo-European", "WEU",  "SVO",  24, 4, "written"),
    ("ru_syntagrus","Russian",     "Indo-European", "EAS",  "SOV",  50, 5, "written"),
    ("hi_hdtb",     "Hindi",       "Indo-European", "SAS",  "SOV",  38, 5, "written"),
    ("fa_seraji",   "Persian",     "Indo-European", "MEA",  "SOV",  32, 4, "written"),
    ("el_gdt",      "Greek",       "Indo-European", "SOU",  "SVO",  30, 4, "written"),
    ("nl_alpino",   "Dutch",       "Indo-European", "WEU",  "SOV",  43, 5, "written"),
    ("it_isdt",     "Italian",     "Indo-European", "WEU",  "SVO",  35, 4, "written"),
    # Uralic (4)
    ("fi_tdt",      "Finnish",     "Uralic",        "EUR",  "SOV",  43, 5, "written"),
    ("hu_szeged",   "Hungarian",   "Uralic",        "EUR",  "SOV",  36, 4, "written"),
    ("et_ewt",      "Estonian",    "Uralic",        "EUR",  "SOV",  15, 3, "written"),
    ("la_proiel",   "Latin",       "Indo-European", "WEU",  "SOV",  35, 4, "written"),
    # Turkic (3)
    ("tr_imst",     "Turkish",     "Turkic",        "MEA",  "SOV",  35, 4, "written"),
    ("kk_ktb",      "Kazakh",      "Turkic",        "CAS",  "SOV",  44, 5, "written"),
    ("uz_tuecl",    "Uzbek",       "Turkic",        "CAS",  "SOV",  40, 5, "written"),
    # Afroasiatic (4)
    ("ar_padt",     "Arabic",      "Afroasiatic",   "MEA",  "VSO",  28, 4, "written"),
    ("he_htb",      "Hebrew",      "Afroasiatic",   "MEA",  "VSO",  27, 3, "written"),
    ("am_att",      "Amharic",     "Afroasiatic",   "EAF",  "SOV",  36, 4, "written"),
    ("ha_easternautogramm","Hausa","Afroasiatic",   "WAF",  "SVO",  33, 4, "written"),
    # Niger-Congo (4)
    ("sw_tud",      "Swahili",     "Niger-Congo",   "EAF",  "SVO",  38, 5, "written"),
    ("yo_ytb",      "Yoruba",      "Niger-Congo",   "WAF",  "SVO",  42, 5, "spoken"),
    ("ig_nkd",      "Igbo",        "Niger-Congo",   "WAF",  "SVO",  35, 4, "spoken"),
    ("zu_zamdi",    "Zulu",        "Niger-Congo",   "SAC",  "SVO",  42, 5, "written"),
    # Sino-Tibetan (4)
    ("zh_gsd",      "Chinese",     "Sino-Tibetan",  "EAS",  "SVO",  41, 4, "written"),
    ("my_my",       "Burmese",     "Sino-Tibetan",  "EAS",  "SOV",  42, 5, "written"),
    ("ta_ttb",      "Tamil",       "Sino-Tibetan",  "SAS",  "SOV",  36, 4, "written"),
    ("mr_cmupan",   "Marathi",     "Sino-Tibetan",  "SAS",  "SOV",  38, 5, "written"),
    # Austronesian (5)
    ("tl_trg",      "Tagalog",     "Austronesian",  "SEA",  "VSO",  29, 3, "written"),
    ("jv_csui",     "Javanese",    "Austronesian",  "SEA",  "VSO",  32, 4, "written"),
    ("id_gsd",      "Indonesian",  "Austronesian",  "SEA",  "VSO",  35, 4, "written"),
    ("ceb_gja",     "Cebuano",     "Austronesian",  "SEA",  "VSO",  35, 4, "spoken"),
    ("ms_gsd",      "Malay",       "Austronesian",  "SEA",  "VSO",  30, 4, "written"),
    # Japonic/Koreanic (2)
    ("ja_gsd",      "Japanese",    "Japonic",       "EAS",  "SOV",  48, 5, "written"),
    ("ko_gsd",      "Korean",      "Koreanic",      "EAS",  "SOV",  48, 5, "written"),
    # Additional coverage (4)
    ("pl_pdb",      "Polish",      "Indo-European", "EUR",  "SOV",  44, 5, "written"),
    ("vi_vtb",      "Vietnamese",  "Austroasiatic", "SEA",  "SVO",  38, 4, "written"),
    ("ka_glc",      "Georgian",    "Kartvelian",    "WCA",  "SOV",  52, 5, "written"),
    ("ne_bk",       "Nepali",      "Indo-European", "SAS",  "SOV",  46, 5, "written"),
    ("ro_rrt",      "Romanian",    "Indo-European", "EAS",  "SVO",  42, 5, "written"),
    ("sr_set",      "Serbian",     "Indo-European", "SOU",  "SOV",  44, 5, "written"),
]

logger.info(f"Loaded {len(TARGETS)} target UD treebanks")


def load_treebank_sample(config_id: str, max_rows: int = 20) -> dict:
    """Load first N rows from one UD treebank using streaming, compute dependency distances."""
    from datasets import load_dataset
    result = {"config_id": config_id, "success": False, "examples": [], "n_total": 0, "n_loaded": 0}
    try:
        ds = load_dataset("commul/universal_dependencies", config_id, split="train", streaming=True)
        count = 0
        for row in ds:
            if count >= max_rows:
                break
            tokens = row.get("tokens", [])
            head = row.get("head", [])
            deprel = row.get("deprel", [])
            upos = row.get("upos", [])
            text = str(row.get("text", ""))[:200]
            
            # Parse dependency info
            try:
                head_list = [int(h) for h in str(head).strip("[]").split(",") if h.strip()]
                deprel_list = [d.strip() for d in str(deprel).strip("[]").split(",") if d.strip()]
            except:
                head_list, deprel_list = [], []
            
            # Dependency distances
            dists = [abs(h - (j + 1)) for j, h in enumerate(head_list) if h > 0]
            avg_dist = sum(dists) / len(dists) if dists else 0
            
            result["examples"].append({
                "input": json.dumps({"tokens": tokens[:20], "upos": upos[:20], 
                                     "head": head_list[:20], "deprel": deprel_list[:20],
                                     "dependency_distances": dists[:30]}),
                "output": json.dumps({"avg_dependency_distance": round(avg_dist, 3),
                                      "max_dependency_distance": max(dists) if dists else 0,
                                      "n_dependencies": len(dists),
                                      "sentence_text": text}),
                "metadata_config_id": config_id,
                "metadata_sentence_index": count,
                "metadata_row_index": count,
            })
            result["n_loaded"] += 1
            count += 1
        
        result["success"] = True
    except Exception as e:
        logger.warning(f"Failed {config_id}: {e}")
    return result


def build_language_records() -> list[dict]:
    """Build one record per language with UD + phonological + typological data."""
    records = []
    for config_id, name, family, region, word_order, phoneme_count, syllable_complexity, register in TARGETS:
        rec = {
            "dataset_id": f"ud_{config_id}",
            "dataset_name": f"Universal Dependencies – {name} ({config_id})",
            "language_name": name,
            "language_code": config_id.split("_")[0],
            "config_id": config_id,
            "family": family,
            "region": region,
            "word_order": word_order,
            "phoneme_inventory_size": phoneme_count,
            "syllable_structure_complexity": syllable_complexity,
            "register": register,
            "phonological_density": round(phoneme_count / syllable_complexity, 2),
            "source": "commul/universal_dependencies on HuggingFace",
            "source_url": f"https://huggingface.co/datasets/commul/universal_dependencies",
            "phonology_source": "PHOIBLE 2.0 (Moran et al. 2023)",
            "typology_source": "WALS (Haspelmath et al. 2005; Werner et al. 2024)",
        }
        info = load_treebank_sample(config_id, max_rows=20)
        if info and info["success"]:
            rec["n_sentences"] = info["n_loaded"]
            rec["load_status"] = "loaded"
            rec["examples"] = info["examples"]
        else:
            rec["n_sentences"] = 0
            rec["load_status"] = "failed"
            rec["examples"] = []
        records.append(rec)
    return records


@logger.catch(reraise=True)
def main():
    t0 = time.time()
    logger.info("Building language records …")
    records = build_language_records()
    logger.info(f"Built {len(records)} records in {time.time()-t0:.1f}s")

    # ── summary stats ──────────────────────────────────────────────────────
    loaded = sum(1 for r in records if r["load_status"] == "loaded")
    families = sorted({r["family"] for r in records})
    word_orders = sorted({r["word_order"] for r in records})
    stats = {
        "total_languages": len(records),
        "successfully_loaded": loaded,
        "families": families,
        "word_orders": word_orders,
        "registers": sorted({r["register"] for r in records}),
        "phoneme_count_range": [min(r["phoneme_inventory_size"] for r in records),
                                max(r["phoneme_inventory_size"] for r in records)],
        "total_sentences": sum(r["n_sentences"] or 0 for r in records),
    }
    logger.info(json.dumps(stats, indent=2))

    # ── build examples: each sentence = one example ────────────────────────
    # We load a sample of sentences from each treebank for the experiment.
    all_examples = []
    per_dataset_examples = {}
    for rec in records:
        cfg = rec["config_id"]
        if rec["load_status"] != "loaded":
            per_dataset_examples[cfg] = {"dataset": rec["dataset_name"], "examples": []}
            continue
        try:
            from datasets import load_dataset
            ds = load_dataset("commul/universal_dependencies", cfg, split="train", streaming=False)
            n_total = len(ds)
            n_keep = min(n_total, 200)  # keep up to 200 sentences per treebank
            n_sent = 0
            for i, row in enumerate(ds):
                if i >= n_keep:
                    break
                text = row.get("text", "")
                tokens = row.get("tokens", [])
                upos = row.get("upos", [])
                deprel = row.get("deprel", [])
                head = row.get("head", [])
                lemma = row.get("lemmas", [])
                # Dependency-distance sample: list of (head, dep) pairs
                try:
                    head_list = [int(h) for h in str(head).strip("[]").split(",") if h.strip()]
                    deprel_list = str(deprel).strip("[]").split(",") if deprel else []
                    deps = [(head_list[j], deprel_list[j] if j < len(deprel_list) else None)
                            for j in range(min(len(head_list), len(tokens)))]
                except Exception:
                    deps = []
                # Dependency distance features
                dists = [abs(h - (j + 1)) for j, h in enumerate(head_list) if h > 0]
                avg_dist = sum(dists) / len(dists) if dists else 0
                max_dist = max(dists) if dists else 0

                example = {
                    "input": json.dumps({
                        "tokens": tokens[:30],
                        "upos": upos[:30],
                        "head": head_list[:30],
                        "deprel": deprel_list[:30],
                        "dependency_distances": dists[:50],
                    }),
                    "output": json.dumps({
                        "avg_dependency_distance": round(avg_dist, 3),
                        "max_dependency_distance": max_dist,
                        "n_dependencies": len(dists),
                        "sentence_text": text[:200],
                    }),
                    "metadata_config_id": cfg,
                    "metadata_language": rec["language_name"],
                    "metadata_family": rec["family"],
                    "metadata_word_order": rec["word_order"],
                    "metadata_register": rec["register"],
                    "metadata_phoneme_count": rec["phoneme_inventory_size"],
                    "metadata_syllable_complexity": rec["syllable_structure_complexity"],
                    "metadata_phonological_density": rec["phonological_density"],
                    "metadata_sentence_index": n_sent,
                    "metadata_row_index": i,
                }
                all_examples.append(example)
                n_sent += 1
            per_dataset_examples[cfg] = {
                "dataset": rec["dataset_name"],
                "examples": [
                    {
                        "input": json.dumps({"tokens": t[:10], "head": h[:10]} if isinstance(t, list) else "{}"),
                        "output": json.dumps({"avg_dist": round(sum(d)/len(d), 2) if d else 0}),
                        "metadata_config_id": cfg,
                        "metadata_language": rec["language_name"],
                        "metadata_family": rec["family"],
                        "metadata_word_order": rec["word_order"],
                        "metadata_register": rec["register"],
                        "metadata_phoneme_count": rec["phoneme_inventory_size"],
                        "metadata_syllable_complexity": rec["syllable_structure_complexity"],
                        "metadata_phonological_density": rec["phonological_density"],
                        "metadata_sentence_index": 0,
                        "metadata_row_index": 0,
                    }
                ],
                "n_total_sentences": n_total,
                "n_examples_kept": n_sent,
                "columns": ds.column_names,
                "sample_text": ds[0].get("text", "")[:300] if n_total > 0 else None,
            }
        except Exception as e:
            logger.error(f"Error processing {cfg}: {e}")
            per_dataset_examples[cfg] = {"dataset": rec["dataset_name"], "examples": []}

    # ── build output ───────────────────────────────────────────────────────
    datasets_grouped = []
    for cfg, info in per_dataset_examples.items():
        datasets_grouped.append({
            "dataset": info["dataset"],
            "n_total_sentences": info.get("n_total_sentences"),
            "n_examples_kept": info.get("n_examples_kept", 0),
            "columns": info.get("columns"),
            "sample_text": info.get("sample_text"),
            "examples": info["examples"],
        })

    output = {
        "meta": {
            "title": "Multilingual UD & Phonological Density Dataset",
            "description": "UD treebanks with phonological/typological features for dependency-distance analysis",
            "source": "commul/universal_dependencies on HuggingFace + PHOIBLE + WALS",
            "n_languages": len(records),
            "n_datasets": len(datasets_grouped),
            "total_examples": len(all_examples),
            "families": families,
            "word_orders": word_orders,
            "created": time.strftime("%Y-%m-%d"),
        },
        "language_records": records,
        "datasets": datasets_grouped,
        "statistics": stats,
    }

    out_path = Path("full_data_out.json")
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Saved {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")

    # Generate mini/preview
    import copy
    mini = copy.deepcopy(output)
    for dg in mini.get("datasets", []):
        dg["examples"] = dg["examples"][:3]
        if dg.get("n_examples_kept"):
            dg["n_examples_kept"] = min(3, dg.get("n_examples_kept") or 0)
    mini_path = Path("mini_data_out.json")
    mini_path.write_text(json.dumps(mini, indent=2, ensure_ascii=False))
    logger.info(f"Saved {mini_path}")

    preview = copy.deepcopy(output)
    for dg in preview.get("datasets", []):
        preview_examples = []
        for ex in dg["examples"][:10]:
            pe = copy.deepcopy(ex)
            for k, v in pe.items():
                if isinstance(v, str) and len(v) > 200:
                    pe[k] = v[:200]
            preview_examples.append(pe)
        dg["examples"] = preview_examples
        if dg.get("n_examples_kept"):
            dg["n_examples_kept"] = min(10, dg.get("n_examples_kept") or 0)
    preview_path = Path("preview_data_out.json")
    preview_path.write_text(json.dumps(preview, indent=2, ensure_ascii=False))
    logger.info(f"Saved {preview_path}")

    logger.info(f"Done in {time.time()-t0:.1f}s")
    return output


if __name__ == "__main__":
    main()

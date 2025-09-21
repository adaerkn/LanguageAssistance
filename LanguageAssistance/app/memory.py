import json
from pathlib import Path
from datetime import date, datetime
from app.spaced_repetition import next_review_sm2

MEM_PATH = Path("data/memory.json")

def load_memory():
    if MEM_PATH.exists():
        with open(MEM_PATH, encoding="utf-8") as f:
            data = json.load(f)
            for item in data.values():
                if item.get("next_review"):
                    item["next_review"] = datetime.fromisoformat(item["next_review"]).date()
            return data
    return {}

def save_memory(mem):
    out = {}
    for k, v in mem.items():
        copy_v = dict(v)
        if copy_v.get("next_review"):
            copy_v["next_review"] = copy_v["next_review"].isoformat()
        out[k] = copy_v
    MEM_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MEM_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

def add_new_word(mem, word_obj):
    key = word_obj["word"]
    if key not in mem:
        mem[key] = {
            "word": key,
            "first_seen": date.today().isoformat(),
            "repetitions": 0,
            "interval": 0,
            "easiness": 2.5,
            "last_review": None,
            "next_review": date.today()
        }

def record_review(mem, word, quality):
    item = mem[word]
    reps, interval, easiness, next_date = next_review_sm2(
        item["repetitions"], item["interval"], item["easiness"], quality
    )
    item.update({
        "repetitions": reps,
        "interval": interval,
        "easiness": easiness,
        "last_review": date.today().isoformat(),
        "next_review": next_date
    })
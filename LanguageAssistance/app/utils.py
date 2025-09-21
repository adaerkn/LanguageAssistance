import json
from pathlib import Path

def load_vocab(path="data/vocabularies/turkish_basic.json"):
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
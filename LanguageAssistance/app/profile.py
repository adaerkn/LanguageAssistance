import json
from pathlib import Path

PROFILE_PATH = Path("data/profile.json")

def create_profile_interactive():
    p = {}
    print("Profil oluşturma:")
    p['language'] = input("Hangi dili öğrenmek istiyorsunuz? ")
    p['level'] = input("Seviyeniz (Başlangıç/Orta/İleri): ")
    p['daily_word_goal'] = int(input("Günde kaç kelime öğrenmek istiyorsunuz? ") or 5)
    p['goal'] = input("Hedefiniz nedir? (Seyahat, İş, vb.): ")
    p['interests'] = input("İlgi alanlarınız? (virgülle ayır): ").split(',')
    save_profile(p)
    return p

def save_profile(profile: dict):
    PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

def load_profile():
    if PROFILE_PATH.exists():
        with open(PROFILE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return None
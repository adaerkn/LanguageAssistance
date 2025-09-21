import json

# JSON dosya yolu
json_path = r"C:\Users\filiz\Desktop\LanguageAssistance\data\vocabularies\turkish_basic.json"

def generate_example_sentences(word):
    # Çok basit, kelimeyi kullanarak 3 örnek cümle üretelim
    return [
        f"{word} çok önemli bir kelimedir.",
        f"Bugün {word} hakkında konuşacağız.",
        f"{word} günlük hayatta sıkça kullanılır."
    ]

# JSON dosyasını oku
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Her kelimeye örnek cümle ekle
for entry in data:
    word = entry.get("word")
    if "examples" not in entry or not entry["examples"]:
        entry["examples"] = generate_example_sentences(word)

# JSON dosyasını tekrar yaz
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ Otomatik örnek cümleler JSON dosyasına eklendi.")

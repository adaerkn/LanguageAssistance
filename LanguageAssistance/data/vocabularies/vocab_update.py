import json
import requests
from bs4 import BeautifulSoup
import time

# --- 1. Dosya yolu
json_path = r"C:\Users\filiz\Desktop\LanguageAssistance\data\vocabularies\turkish_basic.json"

# --- 2. Wiktionary'den anlam ve örnekleri alma
def get_wiktionary_data(word):
    url = f"https://tr.wiktionary.org/wiki/{word}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    definition = None
    examples = []

    # Tanım (ilk <ol><li> altındaki içerik genelde tanım olur)
    ol = soup.find("ol")
    if ol:
        li = ol.find("li")
        if li:
            definition = li.get_text(strip=True)

    # Örnekler: sadece <ul><li> içinden çekmeye çalış
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            text = li.get_text()
            if word in text:
                examples.append(text)

    return {
        "meaning_from_wiktionary": definition,
        "examples_from_wiktionary": examples[:3]  # En fazla 3 örnek al
    }

# --- 3. JSON dosyasını oku
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- 4. Her kelime için veri çek ve güncelle
for entry in data:
    word = entry.get("word")
    print(f"⏳ Kelime işleniyor: {word}")
    result = get_wiktionary_data(word)
    time.sleep(1.5)  # sunucuyu yormamak için

    if result:
        entry.update(result)

# --- 5. Güncellenmiş JSON'u tekrar dosyaya yaz
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ Güncelleme tamamlandı ve dosyaya kaydedildi.")

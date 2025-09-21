import random
from app.llm import correct_sentence

# Basit kelime havuzu örneği
VOCAB = [
    {"word": "merhaba", "meaning": "hello, hi", "examples": ["Merhaba! Nasılsın?", "Merhaba, adın ne?"]},
    {"word": "kitap", "meaning": "book", "examples": ["Bu kitap çok ilginç.", "Okumak için bir kitap aldım."]},
    {"word": "ev", "meaning": "house, home", "examples": ["Evimiz büyük ve güzel.", "Akşamları evde dinleniyorum."]}
]


def run_daily_session(profile: dict):
    print("\n=== Günlük Oturum Başlıyor ===")

    word_entry = random.choice(VOCAB)
    word = word_entry["word"]
    meaning = word_entry["meaning"]
    examples = word_entry["examples"]

    print(f"\n📘 Yeni kelime: {word} → {meaning}")
    print("Örnek cümleler:")
    for ex in examples:
        print(" -", ex)

    correct_attempted = False
    while not correct_attempted:
        print(f"\nŞimdi '{word}' kelimesini kullanarak bir cümle yaz.")
        user_input = input("Senin cümlen: ")

        if user_input.lower() in ['exit', 'çıkış']:
            print("Oturumdan çıkılıyor.")
            return

        corrected_sentence = correct_sentence(user_input, method="grammar")

        if corrected_sentence.lower().strip() == user_input.lower().strip():
            print("✅ Harika! Cümlen dil bilgisi ve yazım açısından doğru görünüyor.")
            correct_attempted = True
        else:
            print(f"\n🤔 Cümle düzeltildi:")
            print(f"  - Senin yazdığın: '{user_input}'")
            print(f"  - Doğrusu:       '{corrected_sentence}'")
            confirmation = input(f"'{corrected_sentence}' mi yazmaya çalıştınız? Evet/Hayır: ").lower()
            if confirmation == "evet":
                print("✅ Harika! Anladığınızı görmek güzel.")
                correct_attempted = True
            else:
                print("Anladım, tekrar deneyelim.")

    print("\n📝 Mini Quiz: Bu kelimenin anlamı neydi?")
    answer = input("Cevabın: ")
    if meaning.lower() in answer.lower():
        print("✅ Doğru!")
    else:
        print(f"❌ Yanlış. Doğru cevap: {meaning}")

    print("\n=== Oturum bitti, yarın görüşürüz! 🚀 ===")
import re
from transformers import pipeline

# Düzeltme modelinin yüklenmesi *
grammar_corrector = pipeline(
    "text2text-generation",
    model="prithivida/grammar_error_correcter_v1",
    tokenizer="prithivida/grammar_error_correcter_v1"
)


COMMON_TYPOS = {
    "bug": "big",
    "yu": "you",
    "helo": "hello",
    "wher": "where",
    "is bug": "is big"
}


def get_corrected_sentence(user_sentence: str) -> str:
    """
    Kullanıcının cümlesini dil bilgisi ve yazım açısından düzeltir.
    """
    try:
        
        for wrong, correct in COMMON_TYPOS.items():
            if wrong in user_sentence.lower():
              
                user_sentence = re.sub(re.escape(wrong), correct, user_sentence, flags=re.IGNORECASE)

      
        if not user_sentence.strip().endswith('.'):
            user_sentence += '.'

        corrected = grammar_corrector(
            user_sentence,
            max_length=64,
            clean_up_tokenization_spaces=True
        )[0]["generated_text"].strip()

        
        if len(corrected.split()) > len(user_sentence.split()) * 2:
            return user_sentence  

        return corrected
    except Exception as e:
        print(f"Düzeltme hatası: {e}")
        return user_sentence


def get_correction_details(original: str, corrected: str) -> list:
    """
    Orijinal ve düzeltilmiş cümleler arasındaki farkları bulur.
    """
    details = []

    
    original_clean = re.sub(r'[,.?!]', '', original).lower().split()
    corrected_clean = re.sub(r'[,.?!]', '', corrected).lower().split()

    for i in range(min(len(original_clean), len(corrected_clean))):
        orig_word = original_clean[i]
        corr_word = corrected_clean[i]

        if orig_word != corr_word:
            
            if len(orig_word) == len(corr_word) and sum(1 for a, b in zip(orig_word, corr_word) if a != b) <= 1:
                details.append(f"Yazım hatası: '{orig_word}' yerine '{corr_word}' demek mi istediniz?")
            else:
                details.append(f"Düzeltme: '{orig_word}' kelimesi '{corr_word}' olarak değiştirildi.")

    return details


VOCAB = [
    {"word": "merhaba", "meaning": "hello, hi", "examples": ["Merhaba! Nasılsın?", "Merhaba, adın ne?"]},
    {"word": "kitap", "meaning": "book", "examples": ["Bu kitap çok ilginç.", "Okumak için bir kitap aldım."]},
    {"word": "ev", "meaning": "house, home", "examples": ["Evimiz büyük ve güzel.", "Akşamları evde dinleniyorum."]}
]

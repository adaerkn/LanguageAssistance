import streamlit as st
import random
from app.profile import load_profile, save_profile
from app.language_processing import get_corrected_sentence, get_correction_details, VOCAB

st.set_page_config(page_title="Language Assistance", page_icon="📘", layout="centered")
st.title("📘 Language Assistance")
st.write("Kelimelerle pratik yap ve cümlelerini kontrol ettir.")

profile = load_profile()
st.sidebar.header("👤 Profil")

language_options = ["İngilizce", "Türkçe"]
profile_language_lower = profile.get("language", "İngilizce").lower()
language_index = 0
try:
    language_index = [lang.lower() for lang in language_options].index(profile_language_lower)
except ValueError:
    language_index = 0

language = st.sidebar.selectbox(
    "Dil:", language_options, index=language_index
)

level_options = ["Başlangıç", "Orta", "İleri"]
profile_level_lower = profile.get("level", "Başlangıç").lower()
level_index = 0
try:
    level_index = [lvl.lower() for lvl in level_options].index(profile_level_lower)
except ValueError:
    level_index = 0

level = st.sidebar.selectbox(
    "Seviye:", level_options, index=level_index
)

daily_word_goal = st.sidebar.number_input(
    "Günlük Hedef (kelime):", min_value=1, max_value=50,
    value=profile.get("daily_word_goal", 10) if profile else 10
)
goal = st.sidebar.text_input(
    "Hedef:", profile.get("goal", "İş") if profile else "İş"
)

if st.sidebar.button("Profili Kaydet"):
    new_profile = {
        "language": language,
        "level": level,
        "daily_word_goal": daily_word_goal,
        "goal": goal
    }
    save_profile(new_profile)
    st.sidebar.success("✅ Profil kaydedildi!")

st.sidebar.markdown("**Güncel Profil Bilgileri:**")
st.sidebar.write(f"**Dil:** {language}")
st.sidebar.write(f"**Seviye:** {level}")
st.sidebar.write(f"**Günlük Hedef:** {daily_word_goal} kelime")
st.sidebar.write(f"**Hedef:** {goal}")

if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(VOCAB)

word_entry = st.session_state.current_word
word = word_entry["word"]
meaning = word_entry["meaning"]
examples = word_entry["examples"]

st.subheader(f"📘 Yeni kelime: **{word}** → {meaning}")
st.write("Örnek cümleler:")
for ex in examples:
    st.write(f"- {ex}")

user_sentence = st.text_input(f"'{word}' kelimesini kullanarak bir cümle yaz:")

if user_sentence:
    corrected = get_corrected_sentence(user_sentence)

    if corrected.lower().strip().replace(" ", "") == user_sentence.lower().strip().replace(" ", ""):
        st.success("✅ Harika! Cümlen doğru görünüyor.")
    else:
        st.warning("🤔 Cümlen düzeltildi:")
        st.write(f"- Senin yazdığın: **{user_sentence}**")
        st.write(f"- Doğrusu: **{corrected}**")

        st.info("💡 **Düzeltme Ayrıntıları:**")
        corrections = get_correction_details(user_sentence, corrected)
        if corrections:
            for detail in corrections:
                st.write(f" - {detail}")
        else:
            st.write("Belirtilen model, cümlenizi bu şekilde düzeltti.")

st.subheader("📝 Mini Quiz")
answer = st.text_input(f"'{word}' kelimesinin anlamı neydi? (virgülle ayırabilirsiniz)")

if answer:
    user_set = set(a.strip().lower() for a in answer.replace('/', ',').split(','))
    correct_set = set(m.strip().lower() for m in meaning.split(','))
    if user_set & correct_set:
        st.success("✅ Doğru!")
    else:
        st.error(f"❌ Yanlış. Doğru cevap: {meaning}")
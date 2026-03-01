import json
import streamlit as st
import joblib

# 1. Eğittiğimiz Yapay Zeka Modelini ve Vektörizeri Yükleme
try:
    intent_model = joblib.load('intent_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    st.error("HATA: Model dosyaları bulunamadı! Önce model_egitimi.py dosyasını çalıştırdığından emin ol.")


def veritabanini_yukle(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        return json.load(dosya)


# 2. Makine Öğrenmesi Tabanlı Niyet Analizi
def niyet_analizi(metin):
    # Oyuncunun metnini modelin anlayacağı matematiksel vektöre çevirme bölümü
    metin_vektoru = vectorizer.transform([metin])

    # Modeli kullanarak bu cümlenin hangi kategoriye ait olduğunu tahmin etme bölümü
    tahmin = intent_model.predict(metin_vektoru)[0]
    return tahmin


def stres_analizi(metin):
    metin = metin.lower()
    agresifler = ["yalan", "katil", "polis", "kamera", "kanıt", "itiraf", "hapis"]
    return sum(1 for k in agresifler if k in metin)


# --- STREAMLIT ARAYÜZÜ ---
st.set_page_config(page_title="Gerilim Odası", page_icon="🕵️")
st.title("Gerilim Odası: Sorgu Başlıyor")

if "arda_db" not in st.session_state:
    st.session_state.arda_db = veritabanini_yukle('arda_db.json')
if "panik" not in st.session_state:
    st.session_state.panik = 0
if "hafiza" not in st.session_state:
    st.session_state.hafiza = {}
if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = [
        {"role": "assistant", "content": "Arda: Bana ne soracaksanız çabuk sorun, menajerimi aramam lazım."}]

for mesaj in st.session_state.mesajlar:
    with st.chat_message(mesaj["role"]):
        st.markdown(mesaj["content"])

oyuncu_sorusu = st.chat_input("Arda'ya bir soru sor...")

if oyuncu_sorusu:
    with st.chat_message("user"):
        st.markdown(oyuncu_sorusu)
    st.session_state.mesajlar.append({"role": "user", "content": oyuncu_sorusu})

    kategori = niyet_analizi(oyuncu_sorusu)
    stres_etkisi = stres_analizi(oyuncu_sorusu)

    if stres_etkisi > 0:
        st.session_state.panik = min(2, st.session_state.panik + stres_etkisi)

    if kategori == "anlasilmadi":
        cevap = "Beni tehdit mi ediyorsun? Avukatım gelmeden konuşmam!" if stres_etkisi > 0 else "Ne demek istediğini anlamıyorum. Net sor."
    elif kategori in st.session_state.hafiza and st.session_state.hafiza[kategori] < st.session_state.panik:
        cevap = "Tamam yeter! Üstüme gelme! Evet... evet yalan söyledim. O kavgayı başlatmamalıydı..."
        st.error("SİSTEM UYARISI: Mantıksal çelişki yakalandı. İtiraf geldi! OYUN BİTTİ.")
    else:
        st.session_state.hafiza[kategori] = st.session_state.panik
        cevap = st.session_state.arda_db["soru_kategorileri"][kategori][f"panic_level_{st.session_state.panik}"]

    with st.chat_message("assistant"):
        st.markdown(cevap)

    st.session_state.mesajlar.append({"role": "assistant", "content": cevap})

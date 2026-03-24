import streamlit as st
import datetime
import google.generativeai as genai

# Ambil API Key dari Secrets (Aman)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_weton(tgl):
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    nilai_hari = [5, 4, 3, 7, 8, 6, 9]
    pasaran = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
    nilai_pasaran = [5, 9, 7, 4, 8]
    base_date = datetime.date(1900, 1, 1)
    delta_days = (tgl - base_date).days
    idx_h = (delta_days + 1) % 7 
    idx_p = (delta_days + 1) % 5 
    total_neptu = nilai_hari[idx_h] + nilai_pasaran[idx_p]
    return f"{hari[idx_h]} {pasaran[idx_p]}", total_neptu

st.title("🔮 Primbon AI Digital")

tab1, tab2 = st.tabs(["👫 Cek Jodoh", "🌟 Ramalan Nasib"])

with tab1:
    tgl_p = st.date_input("Lahir Pria", datetime.date(1996, 1, 14))
    tgl_w = st.date_input("Lahir Wanita")
    if st.button("Hitung Jodoh"):
        w_p, n_p = get_weton(tgl_p)
        w_w, n_w = get_weton(tgl_w)
        prompt = f"Analisis kecocokan pasangan Pria ({w_p}, neptu {n_p}) dan Wanita ({w_w}, neptu {n_w}) menurut Primbon Jawa."
        res = model.generate_content(prompt)
        st.write(res.text)

with tab2:
    tgl_lahir = st.date_input("Tanggal Lahirmu", key="nasib")
    if st.button("Terawang Nasib"):
        w, n = get_weton(tgl_lahir)
        prompt = f"Jelaskan watak weton {w} (neptu {n}) dan beri saran karir di bidang Asset Protection."
        res = model.generate_content(prompt)
        st.write(res.text)

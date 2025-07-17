import streamlit as st
import random
import time

st.set_page_config(page_title="Game asal jadi aja", page_icon="🅰️")

st.title("🅰️ Tangkap Huruf I-L-H-A-M!")
st.write("Mas Ilham lagi bosen kerja? Coba main ini, klik hanya jika huruf yang muncul termasuk dalam nama **ILHAM**. Jangan salah klik yh😋!")

# Huruf ILHAM
target_letters = list("ILHAM")

# Session State
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# Mulai permainan
if st.session_state.round <= 10:
    random_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    st.markdown(f"## 🔤 Huruf Muncul: **{random_letter}**")

    if st.button("🖱️ Klik jika termasuk ILHAM"):
        if random_letter in target_letters:
            st.session_state.score += 1
            st.success(f"✅ Benar! {random_letter} ada di ILHAM")
        else:
            st.session_state.score -= 1
            st.error(f"❌ Salah! {random_letter} ga ada ILHAM")
        st.session_state.round += 1
        st.experimental_rerun()
    else:
        st.info("⚠️ jangan klik sembarangan ya")
else:
    total_time = time.time() - st.session_state.start_time
    st.balloons()
    st.success(f"🎯 Selesai! Skor akhir mas ilham: **{st.session_state.score} / 10**")
    st.write(f"🕒 Total waktu: {total_time:.2f} detik")
    if st.button("🔁 Main Lagi"):
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.start_time = time.time()
        st.rerun()

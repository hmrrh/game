import streamlit as st
import random
import time

st.set_page_config(page_title="game mas ilham", page_icon="🅰️")

st.title("🅰️ Tangkap Huruf I-L-H-A-M!")
st.write("Mas Ilham lagi bosen kerja? Coba main ini👋🏻 Klik tombol hanya jika huruf yang muncul termasuk dalam nama **ILHAM**.\nKalo bukan klik **Lewati** ")

# Huruf ILHAM
target_letters = list("ILHAM")

# Inisialisasi Session State
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "current_letter" not in st.session_state:
    st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Game Loop
if st.session_state.round <= 10:
    st.markdown(f"## 🔤 Huruf Muncul: **{st.session_state.current_letter}**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🖱️ Klik jika termasuk ILHAM"):
            if st.session_state.current_letter in target_letters:
                st.session_state.score += 1
                st.success(f"✅ Benar! {st.session_state.current_letter} ada di ILHAM")
            else:
                st.session_state.score -= 1
                st.error(f"❌ Salah! {st.session_state.current_letter} ga ada di ILHAM")

            st.session_state.round += 1
            st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            st.rerun()

    with col2:
        if st.button("➡️ Lewati"):
            st.session_state.round += 1
            st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            st.info(f"⏭️ Huruf dilewati: {st.session_state.current_letter}")
            st.rerun()

else:
    total_time = time.time() - st.session_state.start_time
    st.balloons()
    st.success(f"🎯 Skor akhir mas Ilham: **{st.session_state.score} / 10**")
    st.write(f"🕒 Total waktu: {total_time:.2f} detik")

    if st.button("🔁 Mw main lagii"):
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.start_time = time.time()
        st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        st.rerun()

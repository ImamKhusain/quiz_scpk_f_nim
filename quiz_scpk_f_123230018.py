import streamlit as st
import pandas as pd

# Header
st.title("Aplikasi Quiz SCPK IF - F")
st.write("Selamat datang di aplikasi Quiz SCPK IF - F!")

# Tabel Data
st.subheader("Data Fakultas pada Kampus")
data = pd.DataFrame({
    "Fakultas": ["FTI", "Fasilkom", "FEB"],
    "Kampus": ["UPN", "UGM", "UI"],
    "Kota": ["Yogyakarta", "Yogyakarta", "Depok"]
})
st.table(data)

# Input data diri
nama = st.text_input("Nama:")
nim = st.text_input("NIM:")
kelas = st.text_input("Kelas:")

# Validasi input
if not nama or not nim or not kelas:
    st.warning("Silakan lengkapi data diri Anda terlebih dahulu.")
else:
    st.subheader("Data Diri Anda:")
    st.write(f"Nama: {nama}")
    st.write(f"NIM: {nim}")
    st.write(f"Kelas: {kelas}")

def main():
    st.title("Fitur Aplikasi Ini")

    # Membuat expander sebagai kotak fitur
    with st.expander("Fitur", expanded=True):
        tab1, tab2, tab3 = st.tabs(["🔺 Hitung Luas Segitiga", "🟦 Hitung Luas Persegi", "🌕 Hitung Luas Lingkaran"])
        
        with tab1:
            st.text("Ini fitur menghitung luas segitiga.")
            alas = st.number_input("Masukkan Panjang Alas : ", min_value=0)
            tinggi = st.number_input("Masukkan Panjang Tinggi : ", min_value=0)
            if st.button("Hitung Luas Segitiga"):
                luas = 0.5 * alas * tinggi
                st.write(f"Luas Segitiga = {luas}")

        with tab2:
            st.text("Ini fitur menghitung luas persegi.")
            sisi = st.number_input("Masukkan Panjang Sisi : ", min_value=0)
            if st.button("Hitung Luas Persegi"):
                luas = sisi * sisi
                st.write(f"Luas Persegi = {luas}")

        with tab3:
            st.text("Ini fitur menghitung luas lingkaran.")
            jari = st.number_input("Masukkan Panjang Jari-jari : ", min_value=0)
            if st.button("Hitung Luas Lingkaran"):
                luas = 3.14 * jari * jari
                st.write(f"Luas Lingkaran = {luas}")

if __name__ == "__main__":
    main()
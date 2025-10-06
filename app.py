import streamlit as st
import pickle
import numpy as np

# Judul aplikasi
st.title("Aplikasi Prediksi Status Performa Mahasiswa")

import streamlit as st

# Input fitur-fitur
Curricular_units_1st_sem_enrolled = st.number_input("Jumlah SKS yang Didaftarkan Mahasiswa pada Semester 1", min_value=0.0, max_value=26.0, value=0.0)
Curricular_units_1st_sem_approved = st.number_input("Jumlah SKS yang Lulus Mahasiswa pada Semester 1", min_value=0.0, max_value=40.0, value=0.0) 
Curricular_units_1st_sem_grade = st.number_input("Nilai Semester 1", min_value=0.0, max_value=4.0, value=0.0)

Curricular_units_2nd_sem_enrolled = st.number_input("Jumlah SKS yang Didaftarkan Mahasiswa pada Semester 2", min_value=0.0, max_value=26.0, value=0.0)
Curricular_units_2nd_sem_approved = st.number_input("Jumlah SKS yang Lulus Mahasiswa pada Semester 2", min_value=0.0, max_value=40.0, value=0.0)
Curricular_units_2nd_sem_grade = st.number_input("Nilai Semester 2", min_value=0.0, max_value=4.0, value=0.0)

# 1 Yes 0 No
Tuition_fees_up_to_date = st.radio("Pelunasan Uang Pendidikan (Iya (1); Tidak (0))", ("1", "0"))
# 1 Yes 0 No
Scholarship_holder = st.radio("Penerima Beasiswa (Iya (1); Tidak (0))", ("1", "0"))
Admission_grade = st.number_input("Nilai Penerimaan", min_value=0.0, max_value=200.0, value=0.0)
Displaced = st.radio("Apakah Mahasiswa Orang Terlantar? (Iya (1); Tidak (0))", ("1", "0"))


# Data dalam bentuk list
data = [
    [
        Curricular_units_2nd_sem_approved,
        Curricular_units_2nd_sem_grade,
        Curricular_units_1st_sem_approved,
        Curricular_units_1st_sem_grade,
        Tuition_fees_up_to_date,
        Scholarship_holder,
        Curricular_units_2nd_sem_enrolled,
        Curricular_units_1st_sem_enrolled,
        Admission_grade,
        Displaced
    ]
]

# Load model dan skaler yang telah disimpan sebelumnya
scaler = pickle.load(open('scaler.pkl', 'rb'))
best_model = pickle.load(open('model_rf.pkl', 'rb'))

# Ketika tombol "Prediksi" ditekan
if st.button("Prediksi"):
    # Standardisasi data
    data_scaled = scaler.transform(data)

    # Prediksi hasil Status
    hasil_prediksi = best_model.predict(data_scaled)
    hasil_prediksi = int(hasil_prediksi)

    # Mapping hasil prediksi ke label yang sesuai
    if hasil_prediksi == 0:
        status = "Dropout"
    elif hasil_prediksi == 1:
        status = "Enrolled"
    else:
        status = "Graduate"

    # Menampilkan hasil prediksi
    st.write(f"Hasil Prediksi Status: {status}")
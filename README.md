# 📊 AI Workplace Productivity & Burnout Analysis Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis bagaimana integrasi **Artificial Intelligence (AI)** di tempat kerja memengaruhi produktivitas karyawan dan risiko *burnout*. Dengan menggunakan data historis, dashboard ini memberikan wawasan mendalam (EDA) serta fitur prediksi berbasis Machine Learning untuk membantu manajemen SDM dalam mengambil keputusan yang berbasis data (*data-driven decision*).

## 🗂️ Struktur Direktori
ilt-datascience/
├── dashboard/
│   ├── dashboard.py
│   ├── df.csv
│   └── rf_model.joblib
├── notebook/
│   ├── [Hands_on]_ILT_4_Developing_Projects_for_Data_Analysis.ipynb
│   └── ai_productivity.zip
├── README.md
└── requirements.txt

## 🚀 Panduan Menjalankan Aplikasi
1. Persiapan Lingkungan (Virtual Environment)
Disarankan untuk menggunakan virtual environment agar tidak terjadi konflik library.

Windows:
Bash
python -m venv venv
venv\Scripts\activate

macOS/Linux:
Bash
python3 -m venv venv
source venv/bin/activate

2. Instalasi Library
Instal semua dependensi yang dibutuhkan menggunakan pip:
Bash
pip install -r requirements.txt

3. Menjalankan Dashboard
Jalankan perintah berikut pada terminal di dalam direktori proyek:
Bash
streamlit run dashboard/dashboard.py
Aplikasi akan secara otomatis terbuka di browser default Anda.
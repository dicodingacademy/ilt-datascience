# 📊 AI Workplace Productivity & Burnout Analysis Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis bagaimana integrasi **Artificial Intelligence (AI)** di tempat kerja memengaruhi produktivitas karyawan dan risiko *burnout*. Dengan menggunakan data historis, dashboard ini memberikan wawasan mendalam (EDA) serta fitur prediksi berbasis Machine Learning untuk membantu manajemen SDM dalam mengambil keputusan yang berbasis data (*data-driven decision*).

## 🗂️ Struktur Direktori
```bash
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
```

## 🚀 Panduan Menjalankan Aplikasi
### Clone Repositori
Langkah pertama, unduh proyek ini ke komputer lokal Anda menggunakan perintah berikut:
```
git clone https://github.com/dicodingacademy/ilt-datascience.git
```

### Instalasi Library
Instal semua dependensi yang dibutuhkan menggunakan pip:
```
pip install -r requirements.txt
```

### Menjalankan Dashboard
Jalankan perintah berikut pada terminal di dalam direktori proyek:
```
streamlit run dashboard/dashboard.py
```
atau
```
python -m streamlit run dashboard/dashboard.py
```
Aplikasi akan secara otomatis terbuka di browser default Anda.

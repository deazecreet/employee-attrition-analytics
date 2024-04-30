# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan telah berkembang menjadi sebuah entitas besar dengan lebih dari 1000 karyawan yang bekerja di berbagai lokasi di seluruh negeri. Meskipun telah mencapai ukuran dan cakupan yang signifikan, perusahaan menghadapi tantangan dalam mengelola sumber daya manusianya, yang tercermin dari tingginya attrition rate sebesar lebih dari 10%. Tingginya tingkat keluar karyawan ini menunjukkan adanya masalah dalam retensi karyawan yang dapat berdampak negatif pada stabilitas operasional dan pertumbuhan perusahaan.

### Permasalahan Bisnis

1. Tingginya *Attrition Rate*: Perusahaan mengalami *attrition rate* yang tinggi, yang berarti banyak karyawan memilih untuk meninggalkan perusahaan. Hal ini menimbulkan biaya rekrutmen yang tinggi dan potensi kehilangan talenta.

2. Identifikasi Faktor Penyebab *Attrition*: Manajemen HR membutuhkan wawasan mendalam tentang faktor-faktor yang mendorong karyawan untuk keluar agar dapat mengembangkan strategi yang tepat untuk meningkatkan retensi karyawan.

3. Kebutuhan akan Dashboard untuk Monitoring: Adanya kebutuhan untuk alat bantu yang memungkinkan manajemen HR untuk memonitor dan menganalisis data karyawan secara *real-time* untuk mengidentifikasi tren dan pola yang berkaitan dengan *attrition*.

### Cakupan Proyek

1. *Exploratory Data Analysis*: Melakukan pemeriksaan dan analisis mendalam terhadap dataset karyawan untuk memahami karakteristik demografis dan perilaku kerja karyawan yang mungkin berkontribusi terhadap attrition rate tinggi.

2. *Data Preprocessing*: Mengidentifikasi dan memilih fitur yang paling relevan yang berkorelasi dengan attrition, menggunakan teknik seperti encoding kategorikal, handling missing data, dan *engineering* fitur baru.

3. *Predictive Modelling*: Mengembangkan model machine learning menggunakan algoritma AdaBoost untuk memprediksi kemungkinan seorang karyawan akan keluar berdasarkan fitur-fitur yang relevan.

4. *Model Evaluation*: Menggunakan data terpisah untuk mengevaluasi efektivitas model dalam memprediksi attrition, termasuk melaporkan metrik performa seperti precision, recall, dan f1-score.

5. *Interactive Dashboard*: Pembuatan dashboard menggunakan Metabase yang akan menampilkan visualisasi data karyawan yang memungkinkan HR untuk mengambil tindakan pencegahan sebelum *attrition* terjadi.

### Persiapan

Sumber data: [Link Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment:

```
python -m venv venv
.\venv\Scripts\activate
pip install pandas plotly scikit-learn joblib
jupyter notebook
python prediction.py
```

## Business Dashboard

*Business Dashboard* berisi visualisasi-visualisasi data dari 7 variabel kategorik (`OverTime`, `EnvironmentSatisfaction`, `JobInvolvement`, `JobSatisfaction`, `MaritalStatus`, `WorkLifeBalance`, `JobLevel`) dan 5 variabel numerik (`Age`, `TotalWorkingYears`, `YearsAtCompany`, `MonthlyIncome`, `DistanceFromHome`)

*Username* Metabase: azelpetrov@mail.com
*Password* Metabase: azelpetrov123
*Dashboard Link*: [Kunjungi Link Dashboard](http://localhost:3001/public/dashboard/caf864ac-cb91-492f-9f3c-27f1785c5649)

## Conclusion

Beberapa hal penting mengenai faktor-faktor yang mempengaruhi tingginya *attrition rate* di perusahaan Jaya Jaya Maju, yaitu:

1. Faktor Demografis: Usia dan status pernikahan memiliki pengaruh terhadap keputusan karyawan untuk meninggalkan perusahaan. Karyawan muda dan lajang cenderung memiliki *attrition rate* yang lebih tinggi.

2. Faktor Pekerjaan: Beban kerja, seperti lembur yang berlebihan, dan kurangnya keseimbangan antara pekerjaan dan kehidupan pribadi secara signifikan berkorelasi dengan kepuasan kerja yang rendah dan keputusan untuk keluar.

3. Kepuasan Kerja: Kepuasan terhadap lingkungan kerja, keterlibatan dalam pekerjaan, dan tingkat kepuasan secara umum terbukti mempengaruhi keputusan *attrition*.

4. Faktor Keuangan: Gaji dan kenaikan gaji tahunan, serta level jabatan juga berpengaruh terhadap *attrition*, dengan karyawan yang memiliki gaji rendah lebih cenderung untuk keluar.

### Rekomendasi Action Items

1. Menyesuaikan Kebijakan Lembur: Mengevaluasi dan jika memungkinkan mengurangi kebutuhan akan lembur berlebihan, serta memastikan kompensasi yang adil untuk jam kerja tambahan untuk mengurangi tekanan kerja dan meningkatkan keseimbangan hidup-kerja.

2. Program Kesejahteraan Karyawan: Mengimplementasikan atau memperkuat program kesejahteraan karyawan yang mendukung baik aspek fisik maupun mental, seperti fasilitas kebugaran, konseling, dan aktivitas sosial untuk meningkatkan kepuasan kerja dan keterlibatan karyawan.

3. Meningkatkan Komunikasi dan Feedback: Membuat saluran komunikasi yang lebih efektif antara karyawan dan manajemen untuk mendengarkan dan menanggapi masukan karyawan secara regular, termasuk survey kepuasan karyawan secara berkala.

4. Menyesuaikan Struktur Gaji: Meninjau dan menyesuaikan struktur gaji dan insentif untuk memastikan bahwa perusahaan tetap kompetitif dalam pasar tenaga kerja dan dapat mempertahankan talenta terbaik.

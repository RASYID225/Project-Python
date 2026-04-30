# 📊 Analisis Performa Penjualan E-commerce

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-150458.svg)](https://pandas.pydata.org/)
[![Data-Analysis](https://img.shields.io/badge/Main--Task-Data%20Analysis-orange.svg)]()

Laporan ini disusun sebagai bagian dari praktikum analisis data untuk mengidentifikasi performa penjualan, segmentasi pelanggan, dan efisiensi strategi pemasaran pada platform e-commerce.

---

## 🎯 1. Business Question
Analisis ini bertujuan untuk menjawab permasalahan bisnis berikut:
* [cite_start]**Produk Underperformer:** Mengidentifikasi produk dengan harga tinggi namun volume penjualan rendah[cite: 86, 87].
* [cite_start]**Segmentasi Pelanggan:** Menentukan pelanggan prioritas untuk program loyalitas menggunakan metode **RFM (Recency, Frequency, Monetary)**[cite: 96, 102].
* [cite_start]**Efisiensi Kategori:** Mengevaluasi perbandingan pendapatan kategori terhadap anggaran iklan yang dihabiskan[cite: 103, 106].
* [cite_start]**Analisis Prediktif:** Menguji pengaruh biaya iklan terhadap total penjualan melalui model regresi linear[cite: 109, 140].

---

## 🛠️ 2. Data Wrangling
[cite_start]Tahapan pembersihan data dilakukan untuk memastikan validitas hasil analisis[cite: 58, 59]:
1. [cite_start]**Inspeksi Data:** Mengecek tipe data dan nilai yang hilang (*missing values*) menggunakan `df.info()`[cite: 60, 61].
2. [cite_start]**Pembersihan Anomali:** Menghapus entri dengan harga negatif atau nol (`Price > 0`)[cite: 62].
3. [cite_start]**Standarisasi Waktu:** Mengonversi kolom `Order_Date` menjadi format *datetime* untuk analisis tren dan waktu[cite: 63].

---

## 📈 3. Insights (Temuan Utama)
* [cite_start]**Visualisasi Tren:** Penggunaan *Line Chart* menunjukkan pola fluktuasi penjualan bulanan yang membantu prediksi stok di masa depan[cite: 66, 71].
* [cite_start]**Korelasi Antar Variabel:** Berdasarkan *Heatmap*, dapat dilihat sejauh mana biaya iklan dan diskon memengaruhi angka penjualan[cite: 74, 77].
* [cite_start]**Peta Produk:** Melalui *Scatter Plot*, ditemukan produk yang membebani arus kas (Harga > Rata-rata, Kuantitas Rendah)[cite: 88, 90].
* [cite_start]**Segmentasi Loyalitas:** Pelanggan dengan skor RFM tertinggi diidentifikasi sebagai target utama retensi[cite: 115, 116].

---

## 💡 4. Recommendation
Berdasarkan hasil analisis, langkah strategis yang direkomendasikan adalah:
* [cite_start]**Optimasi Stok:** Melakukan penyesuaian harga atau promosi cuci gudang untuk kategori produk *underperformer*[cite: 88, 95].
* [cite_start]**Program Loyalitas:** Memberikan voucher eksklusif kepada pelanggan di segmen skor RFM tertinggi (misal: R_Score 5, F_Score 5, M_Score 5)[cite: 102, 134].
* [cite_start]**Alokasi Anggaran:** Mengalihkan anggaran iklan dari kategori yang tidak efisien ke kategori dengan kontribusi pendapatan lebih besar[cite: 107].
* [cite_start]**Strategi Pemasaran:** Jika model regresi menunjukkan akurasi tinggi, perusahaan dapat meningkatkan `Ad_Budget` secara terukur untuk menaikkan `Total_Sales`[cite: 158, 159].

---

## 💻 5. Implementasi Kode (Snippet)

### Analisis RFM
```python
# Agregasi data RFM
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days, # Recency
    'Order_ID': 'count',                                   # Frequency
    'Total_Sales': 'sum'                                   # Monetary
})
# Tugas 10 SIG - Spatial AI & Computer Vision Object Detection

Proyek ini merupakan implementasi **GeoAI (Geospatial Artificial Intelligence)** memanfaatkan model arsitektur *Deep Learning* **YOLOv8** dan **OpenCV** untuk mendeteksi entitas fisik (seperti bangunan, jalan, dan objek kendaraan) dari citra foto udara (*Remote Sensing*) secara massal (*Batch Processing*). Koordinat piksel bounding box lokal otomatis dtranslasi menjadi bentuk data spasial koordinat bumi asli (Polygon Bounding Box) berstandar **EPSG:4326** dan diekspor ke dalam format **GeoJSON**.

## 👥 Identitas Mahasiswa
* **Nama:** Gohan Tua Jeremia Ambarita
* **NIM:** 123140160
* **Afiliasi:** Teknik Informatika - Institut Teknologi Sumatera (ITERA)
* **Kelas/Mata Kuliah:** Praktikum Sistem Informasi Geografis (SIG) - Pertemuan 10

---

## 🚀 Fitur Utama Sistem

1. **Automated Dependency Injection:** Skrip otomatis mendeteksi dan mengunduh berkas bobot model pre-trained `yolov8n.pt` langsung dari server resmi menggunakan library standar Python jika belum tersedia secara lokal.
2. **High-Sensitivity Satelite Detection:** Optimasi parameter ambang batas keyakinan (`conf=0.15`) dan ukuran pemrosesan internal (`imgsz=640`) untuk mengenali objek-objek kecil khas sudut pandang tegak lurus satelit (*Nadir View*).
3. **Geo-Calibration / Kelas Koreksi Spasial:** Menyediakan logika otomatis untuk memetakan objek-objek salah klasifikasi akibat sudut pandang udara (seperti atap bundar stadion yang terdeteksi sebagai `clock` atau `umbrella` otomatis diubah menjadi kategori `building`).
4. **Batch Processing Automation:** Mampu melahap dan mengekstrak banyak gambar sekaligus (`.png`, `.jpg`, `.jpeg`) yang berada di dalam direktori input, memprosesnya secara bergantian, dan memisahkan setiap *output* berkas spasialnya.
5. **Linear Interpolation Matematika Spasial:** Mengonversi letak piksel grafik $X$ dan $Y$ pada monitor komputer ke derajat koordinat asli lintang (Latitude) dan bujur (Longitude) wilayah **Lampung Selatan**.

---

## 📂 Struktur Direktori Proyek

```text
tugas10sig_123140160_gohan/
├── data/
│   ├── ITERA.png                     # Citra satelit kompleks kampus
│   ├── lalu lintas.jpeg              # Citra satelit area jalan raya
│   ├── perkotaan.png                 # Citra satelit area pemukiman padat
│   └── Stadion.png                   # Citra satelit area megastruktur olahraga
├── output/
│   ├── deteksi_ITERA.geojson         # Hasil ekstraksi koordinat spasial ITERA
│   ├── deteksi_lalu lintas.geojson   # Hasil ekstraksi koordinat spasial jalan raya
│   ├── hasil_ITERA.jpg               # Gambar visual bboxes hijau objek ITERA
│   └── hasil_lalu lintas.jpg         # Gambar visual bboxes hijau objek jalan raya
├── requirements.txt                  # Daftar library (ultralytics, opencv, shapely)
├── spatial_ai.py                     # Script Python Utama Pemrosesan GeoAI
└── yolov8n.pt                        # File bobot model deep learning lokal

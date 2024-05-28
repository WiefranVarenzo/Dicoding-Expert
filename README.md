# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan dari JayaJaya Maju adalah perusahaan multinatsion yang memiliki 1470 karyawan, dimana terdapat 179 orang yang keluar dari perusahaan. Sehingga, karyawan yang saat ini masih aktif hanya berjumlah 1291 orang saja. Dari perhitungan angka karyawan yang keluar dan jumlah total karyawan, maka bisa kita dapatkan bahwa attrition ratenya mencapai 12,18 persen yang merupakan attrition yang cukup besar untuk sebuah perusahaan. Jika tingkat attrition tinggi, maka perusahaan akan sulit berkembang dikarenakan harus merekrut karyawan baru, dimana karyawan tersebut diharuskan untuk beradaptasi kembali di perusahaan JayaJayaMaju. Hal ini bisa memakan waktu dan menghambat pertumbuhan dan stabilitas perusahan.

### Permasalahan Bisnis

Jika stabilitas perusahaan terganggu dengan tingkat attrition karyawan yang tinggi, hal ini bisa menjadi masalah karena dibutuhkan waktu adaptasinya karyawan baru yang membuang waktu perusahaan hanya untuk membantu karyawan baru ini bisa menyesuaikan diri dengan pekerjaan dan budaya perusahaan. Hal ini dapat membuat perusahaan lamban dalam melakukan pemrosesan pengembangan produk. Terutama salah satu Job role yang mengalami attrition tertinggi adalah Research Scientist dan sales representatif. Kedua Job role ini bisa mengakibatkan perusahaan sulit untuk melakukan pengembangan produk atau jasa dengan lebih baik lagi (kurangnya Research Scientist), serta sulit untuk menjual produk mereka (kurangnya Sales Representative)

Jika pengembangan dan penjualan produk berkurang, maka Perusahan Jaya Jaya Maju akan mengalami penurunan dalam kinerja penjualan mereka, serta perusahaan ini bisa saja akan di geser pasar customernya dengan saingan dari perusahaan lain yang berkecimpung di sektor bisnis yang sama. 

### Cakupan Proyek
Proyek ini bertujuan untuk menganalisis dan mengatasi masalah tingkat attrition yang tinggi di perusahaan JayaJaya Maju. Dengan mengidentifikasi faktor-faktor yang mempengaruhi keluarnya karyawan, proyek ini berusaha untuk mengembangkan strategi yang dapat mengurangi tingkat attrition dan meningkatkan retensi karyawan. Berikut adalah rincian cakupan proyek:

1. Analisis Data Attrition:
(1) Mengumpulkan dan membersihkan data karyawan yang mencakup informasi seperti umur, jenis kelamin, gaji, lama bekerja, divisi, dan alasan keluar dari perusahaan. M
(2) Menganalisis data untuk menemukan pola dan tren yang mungkin berkontribusi terhadap tingginya tingkat attrition.
2. Identifikasi Faktor Utama:
(1)Mengidentifikasi faktor-faktor utama yang mempengaruhi tingkat attrition, seperti gaji, lembur, peluang kenaikan jabatan, dan tingkat kepuasan kerja.
(2)Menggunakan teknik statistik dan machine learning untuk menentukan faktor yang paling signifikan.
3. Model Prediksi:
(1) Mengembangkan model prediksi untuk mengidentifikasi karyawan yang berisiko tinggi untuk keluar dari perusahaan.
(2) Model ini akan membantu manajemen dalam mengambil tindakan proaktif untuk mencegah keluarnya karyawan.
4. Dashboard Visualisasi Data:
(1) Membangun dashboard interaktif yang menampilkan data KPI terkait attrition dan faktor-faktor yang mempengaruhinya.
(2) Dashboard ini akan membantu manajemen dalam memantau tingkat attrition dan efektivitas strategi yang diimplementasikan.
5. Rekomendasi Strategi:
(1) Memberikan rekomendasi berbasis data untuk mengurangi tingkat attrition, seperti penyesuaian gaji, pengurangan lembur, dan peningkatan program apresiasi karyawan.
(2) Mengusulkan kebijakan dan program baru untuk meningkatkan kepuasan dan retensi karyawan.

Output dari proyek ini meliputi:

1. Model Prediksi: Model machine learning yang dapat memprediksi faktor yang memperbesar kemungkinan keluarnya karyawan dengan akurasi tinggi.
2. Dashboard Visualisasi Data: Dashboard interaktif yang menampilkan data terkait attrition dan faktor-faktor penyebabnya.
3. Rekomendasi Strategi: Daftar rekomendasi strategi berbasis data untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan.
4. Laporan Analisis: Laporan komprehensif yang mencakup analisis data, temuan utama, dan rekomendasi tindakan.

Dengan proyek ini, diharapkan perusahaan JayaJaya Maju dapat mengurangi tingkat attrition, meningkatkan retensi karyawan, dan pada akhirnya, meningkatkan stabilitas dan pertumbuhan perusahaan.

### Persiapan
Sumber Data: 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv'

Setup environment:
```
!pip install imbalanced-learn
```

## Business Dashboard

Pada Business Dashboard HR Attrition Analysis, terdapat 7 bagan atau grafik yang merupakan analisa akhir dari proses analisa menggunakan Google Collab. Business dashboard di bawah dengan menggunakan pola Zigzag, dimana sebelah kiri akan menjadi pembuka awal masalah, sedangkan bagian kanan merupakan puncak dari analisa. Lalu, di baris bawah Business dashboard akan terdapat 3 bagan yang saling menjelaskan faktor-faktor yang mempengaruhi tingkat atrisi. Lalu,Dengan fitur dashboard yang dinamis, maka penggunaa bisa berinteraksi dengan melakukan hover pada bagan sehingga dapat melihat detail data yang ditampilkan. 

Hasil Analisa Business Dashboard:
Pada bagan pertama, data KPI menunjukkan bahwa 179 dari 1470 total pegawai mengalami atrisi, yang berarti tingkat atrisi di perusahaan Jaya Jaya Maju adalah sekitar 12,18% — cukup tinggi untuk sebuah perusahaan (>10%). Dashboard mengidentifikasi beberapa faktor penyebab atrisi tinggi ini, yang pertama adalah tingkat lembur pegawai. Pegawai yang sering lembur mengalami atrisi sekitar 19% lebih tinggi dibandingkan mereka yang tidak lembur.

Selanjutnya, bagan rata-rata pendapatan bulanan per Job Role menunjukkan beberapa peran dengan gaji terendah, seperti Laboratory Technician, Research Scientist, dan Sales Representative, semuanya memiliki rata-rata gaji di bawah 5 ribu dolar per bulan. Ketiga peran ini mendominasi angka atrisi: Laboratory Technician (27,37%), Research Scientist (21,23%), dan Sales Representative (13,97%). Meskipun Sales Executive juga memiliki angka atrisi tinggi, gaji bulanan mereka tidak serendah Job Role lainnya, menunjukkan adanya faktor lain yang berperan. Kesimpulannya, semakin rendah rata-rata gaji bulanan, semakin tinggi angka atrisi. Ketiga Job Role ini menyumbang 62,57% dari total atrisi, menguatkan kesimpulan tersebut.

Data atrisi berdasarkan apresiasi perusahaan (job involvement) dalam bentuk saham menunjukkan bahwa pegawai yang tidak menerima saham memiliki angka atrisi tertinggi, lebih dari 121 orang (sekitar 67%). Pegawai dengan kontribusi cukup baik (job involvement bernilai 3) tetapi tidak menerima saham, paling berkemungkinan mengalami atrisi.

Bagan sebaran data antara gaji dan umur menunjukkan bahwa pegawai muda (20-30 tahun) dengan gaji di bawah 5 ribu dolar mendominasi angka atrisi. Ini menegaskan bahwa gaji rendah meningkatkan kemungkinan atrisi, terutama bagi pegawai muda yang mencari peluang gaji lebih baik.

Bagan terakhir menunjukkan bahwa persentase kenaikan gaji yang rendah juga meningkatkan kemungkinan atrisi pegawai.
## Conclusion
Teradapat beberapa konklusi yang bisa diambil:
1. Lembur dapat meningkatkan angka attrition, dibandingkan karyawan yang tidak lembur, jumlah karyawan yang ingin keluar paling banyak merupakan karyawan yang sering atau pernah melakukan lembur
2. Beberapa JobRole mendapatkan gaji yang rendah, hal ini membuat banyak karyawan pada jobRole tersebut keluar dari perusahaan
3. Pegawai yang memiliki kontribusi baik, namun tidak diapresiasi akan cenderung ingin keluar dari perusahaan dibandingkan mereka yang mendapatkan kesempatan untuk mendapat sebagian saham perusahaan sebagai bentuk apresiasi
4. Semakin rendah peningkatan gaji yang di dapat karyawan, maka karyawan akan semakin berkemungkinan untuk keluar dari perusahaan 


### Rekomendasi Action Items (Optional)

Ada beberapa hal yang perlu dilakukan oleh perusahaan Jaya Jaya Maju agar tingkat attrition tidak semakin tinggi:
1. Meningkatkan gaji beberapa Job role yang mendapatkan gaji yang rendah (seperti Research Scientist, sales representative, dan Laboratory Technician), serta untuk gaji bulanan juga dapat ditingkatkan terutama untuk mempertahankan karyawan muda yang memiliki kontribusi yang baik.
2. Mengurangi lembur karyawan agar karyawan tidak merasa jenuh terhadap pekerjaan
3. Mengapresiasi mereka yang melakukan kontribusi yang baik kepada perusahaan dengan memberikan mereka Opsi pemberian saham perusahaan, hal ini bisa membantu perusahaan mempertahankan karyawan yang bekerja dengan baik
4. Memberikan peningkatan gaji yang stabil dan sesuai (tidak rendah). 

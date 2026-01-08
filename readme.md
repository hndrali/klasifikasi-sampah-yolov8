# Klasifikasi Sampah dengan YOLOv8 dan Streamlit

Repo ini berisi implementasi klasifikasi sampah menggunakan model YOLOv8 dan antarmuka web interaktif dengan Streamlit. 

## Langkah-langkah Instalasi

1.  **Download atau Clone Repository:**

    ```bash
    git clone https://github.com/hndrali/klasifikasi-sampah-yolov8.git
    cd klasifikasi-sampah-yolov8
    ```

2.  **Buat Virtual Environment:**

    Sangat disarankan untuk menggunakan virtual environment agar dependensi proyek Anda terisolasi.

    ```bash
    python -m venv venv
    ```

    Aktifkan virtual environment Anda:

    * **Untuk Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    * **Untuk Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3.  **Install Dependencies:**

    Install semua package yang dibutuhkan dari file `requirements.txt` (pastikan file ini ada di root direktori repo Anda).

    ```bash
    pip install -r requirements.txt
    ```


## Cara Penggunaan

1.  **Jalankan Aplikasi Streamlit:**

    Pastikan Anda berada di dalam direktori root repository Anda dan virtual environment Anda aktif. Jalankan aplikasi Streamlit dengan perintah:

    ```bash
    streamlit run app.py
    ```

    Perintah ini akan secara otomatis membuka aplikasi web di browser Anda (biasanya di `http://localhost:8501`).

2.  **Menggunakan Aplikasi Web:**

    * **Jepret Gambar dengan Webcam:** Pada antarmuka web, Anda akan melihat opsi untuk mengunggah gambar sampah yang ingin Anda klasifikasikan.
    * **Proses Klasifikasi:** Setelah Anda mengunggah gambar, aplikasi akan menggunakan model YOLOv8 untuk mendeteksi dan mengklasifikasikan objek sampah yang terdeteksi dalam gambar.
    * **Hasil Klasifikasi:** Hasil klasifikasi (organik atau anorganik) akan ditampilkan pada layar. Gambar dengan bounding box di sekitar objek yang terdeteksi juga akan ditampilkan.

## Struktur Repository (Contoh)

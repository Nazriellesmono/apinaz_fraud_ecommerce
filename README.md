# 🛒 E-commerce Fraud Detection API

API ini dirancang untuk mendeteksi potensi aktivitas penipuan dalam transaksi e-commerce menggunakan machine learning. Model dilatih menggunakan dataset e-commerce dan fokus pada 10 fitur paling berpengaruh yang dipilih melalui analisis feature importance dengan XGBoost.

---

## 🚀 Fitur
- Prediksi apakah transaksi termasuk fraud
- Memberikan probabilitas penipuan
- Level risiko: Low / Medium / High
- Otentikasi menggunakan API Key
- Batas maksimum request per menit (rate limit)

---

## 📦 Endpoint

### `POST /v1/predict`
- **Deskripsi**: Memprediksi kemungkinan penipuan berdasarkan data transaksi.
- **Headers**:
  - `x-api-key`: API key milik pengguna
- **Body (JSON)**:
```json
{
  "data": {
    "avg_item_price": 150000,
    "avg_order_value": 450000,
    "avg_response_time_min": 15,
    "checkout_time_sec": 25,
    "has_voucher": 1,
    "location_match_Normal": 1,
    "min_purchase": 100000,
    "return_rate": 0.1,
    "status_completed": 1,
    "voucher_discount": 50000
  }
}
```

- **Respons**:
```json
{
  "is_fraud": true,
  "fraud_probability": 0.9969,
  "risk_level": "high"
}
```

### `GET /v1/health`
- Mengecek status kesehatan API

---

## 🐳 Dukungan Docker
### Build
```bash
docker build -t apinaz-fraud-ecommerce .
```

### Jalankan
```bash
docker run -d -p 8888:8888 apinaz-fraud-ecommerce
```

---

## 🔐 API Key dan Rate Limiting
Untuk mengakses endpoint prediksi, tambahkan header berikut:
```bash
x-api-key: your_api_key_here
```

> ⚠️ Pembatasan jumlah request telah diterapkan di `main.py`. Secara default, pengguna hanya dapat mengirim **30 request per menit** untuk predict/v1. Anda dapat mengubah nilai ini sesuai kebutuhan.

---

## 🧪 Swagger UI

Dokumentasi interaktif tersedia di Swagger UI setelah container berjalan:

👉 [http://localhost:8889/docs](http://localhost:8889/docs)

Isi dokumentasi meliputi:
- Skema input (JSON)
- Contoh payload transaksi
- Output prediksi fraud dengan probabilitas
- Rate limit status per user

---

## ⚙️ Stack Teknologi
- FastAPI
- XGBoost
- Joblib
- Docker
- Pydantic
- SlowAPI (untuk rate limit)

---

## 👨‍💻 Author
- **Nazriellesmono**
- GitHub: [@Nazriellesmono](https://github.com/Nazriellesmono)

---

## 📌 Status
🚀 **Stable MVP** – Siap untuk demo dan uji coba internal. Cocok untuk showcase profesional dan portofolio AI di bidang fraud detection.

> Powered by FastAPI, XGBoost, and mentorship feedback.

# 🛒 E-commerce Fraud Detection API

This API is designed to detect potential fraudulent activities in e-commerce transactions using machine learning. The model is trained on an e-commerce dataset and focuses on the top 10 most influential features selected through feature importance analysis using XGBoost.

---

## 🚀 Features
- Predict whether a transaction is fraudulent  
- Returns fraud probability  
- Risk level: Low / Medium / High  
- API Key authentication  
- Maximum request limit per minute (rate limit)

---

## 📦 Endpoint

### `POST /v1/predict`
- **Description**: Predicts the likelihood of fraud based on transaction data.  
- **Headers**:  
  - `x-api-key`: User's API key  
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

- **Response**:
```json
{
  "is_fraud": true,
  "fraud_probability": 0.9969,
  "risk_level": "high"
}
```

### `GET /v1/health`
- Checks the health status of the API

---

## 🐳 Docker Support
### Build
```bash
docker build -t apinaz-fraud-ecommerce .
```

### Run
```bash
docker run -d -p 8888:8888 apinaz-fraud-ecommerce
```

---

## 🔐 API Key & Rate Limiting
To access the prediction endpoint, include the following header:
```bash
x-api-key: your_api_key_here
```

> ⚠️ Request rate limiting has been implemented in `main.py`. By default, users can only send **30 requests per minute** to the `predict/v1` endpoint. You may adjust this value as needed.

---

## 🧪 Swagger UI

Interactive documentation is available via Swagger UI once the container is running:

👉 [http://localhost:8889/docs](http://localhost:8889/docs)

The documentation includes:
- Input schema (JSON)
- Sample transaction payloads
- Fraud prediction output with probability
- Per-user rate limit status

---

## ⚙️ Tech Stack
- FastAPI  
- XGBoost  
- Joblib  
- Docker  
- Pydantic  
- SlowAPI (for rate limiting)

---

## 👨‍💻 Author
- **Nazriellesmono**  
- GitHub: [@Nazriellesmono](https://github.com/Nazriellesmono)  
- LinkedIn: [@Nazriellesmono](https://www.linkedin.com/in/nazriel-lesmono-8b8b8a359/)

---

## 📌 Status
🚀 **Stable MVP** – Ready for demo and internal testing. Ideal for professional showcase and AI fraud detection portfolio.

> Powered by FastAPI, XGBoost, and mentorship feedback.

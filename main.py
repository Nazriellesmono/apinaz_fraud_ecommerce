# app/main.py

from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import uvicorn

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Setup rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="E-Commerce Fraud Detection API – Free Tier",
    version="1.0.0",
    description="API ini menggunakan 10 fitur terpenting untuk mendeteksi penipuan transaksi e-commerce(promo abuse). Cocok untuk integrasi ringan & skenario evaluasi awal.",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Load model dan fitur
model = joblib.load("model_top10.joblib")
top10_features = joblib.load("top10_features.joblib")

# API Key
API_KEY = "b6e9ff7542abbd81a0a47b6e76c9d2a30ec89f39f772edc7196e3fbf37dd74e6"

class FraudRequest(BaseModel):
    data: dict = Field(
        ...,
        example={
            "checkout_time_sec": 25,
            "status_completed": 1,
            "avg_order_value": 450000,
            "location_match_Normal": 1,
            "voucher_discount": 50000,
            "return_rate": 0.1,
            "has_voucher": 1,
            "min_purchase": 100000,
            "avg_item_price": 150000,
            "avg_response_time_min": 15
        }
    )


@app.post("/v1/predict")
@limiter.limit("30/minute")
def predict_fraud(req: FraudRequest, request: Request, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        df = pd.DataFrame([req.data])
        df = df[top10_features]

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        if prob >= 0.8:
            risk_level = "high"
        elif prob >= 0.5:
            risk_level = "medium"
        else:
            risk_level = "low"

        return {
            "is_fraud": bool(pred),
            "fraud_probability": round(float(prob), 4),
            "risk_level": risk_level
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/v1/health")
@limiter.limit("5/minute")
def health_check(request: Request):
    return {
        "status": "ok",
        "message": "E-Commerce Fraud Detection API is healthy.",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8889, reload=True)

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create FastAPI app
app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts customer churn probability",
    version="1.0"
)

# Load trained model (full pipeline)
model = joblib.load("app/churn_model.pkl")


# Input schema (MUST match training features)
class CustomerData(BaseModel):
    credit_score: int
    city: str
    gender: str
    age: int
    tenure: int
    balance: float
    num_products: int
    has_credit_card: int
    is_active: int
    estimated_salary: float


@app.post("/predict")
def predict_churn(data: CustomerData):
    # Convert request to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict probability
    churn_probability = model.predict_proba(input_df)[0][1]
    prediction = int(churn_probability >= 0.5)

    return {
        "churn_probability": round(float(churn_probability), 4),
        "prediction": prediction
    }

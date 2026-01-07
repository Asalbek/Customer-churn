# Customer Churn Prediction 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)

---

## 📌 Project Overview

This project implements a **customer churn prediction system** for a bank.  
Given customer profile and behavioral data, the system predicts the **probability that a customer will churn**.

The solution covers the **full machine learning lifecycle**:
- exploratory data analysis
- feature preprocessing
- model training & evaluation
- explainability (SHAP)
- deployment as a REST API
- containerization with Docker

---

## 🎯 Business Objective

Customer churn is costly for banks.  
The goal of this model is to **identify high-risk customers early**, enabling targeted retention actions such as personalized offers or proactive outreach.

---

## 📊 Dataset

- **Rows:** ~15,000  
- **Features:** 14 (after cleaning: 10 predictive features)  
- **Target:** `churn`  
  - `1` → customer churns  
  - `0` → customer stays  

---

## 🧠 Modeling Approach

### Models Evaluated
- **Logistic Regression** (baseline)
- **Random Forest** ✅ *(final model)*

### Why Random Forest?
- Handles non-linear relationships
- Captures feature interactions
- Robust to outliers
- Strong performance on tabular data

---

## 📈 Model Performance

| Metric | Logistic Regression | Random Forest |
|------|--------------------|---------------|
| ROC-AUC | ~0.88 | **~0.93** |
| Accuracy | ~0.81 | **~0.88** |
| Recall (Churn) | ~0.80 | ~0.79 |
| Precision (Churn) | ~0.53 | **~0.67** |

**Final Model:** Random Forest  
**Primary Metric:** ROC-AUC  

---

## 🔍 Explainability (SHAP)

SHAP (SHapley Additive exPlanations) was used to interpret the model.

Key findings:
- **Credit score** and **age** are the strongest drivers of churn
- Other features contribute less but still add incremental signal

SHAP values were computed on a representative subset of the training data to reduce computational cost.

---

## 🧱 Project Structure
Customer-churn/
├── app/
│ ├── main.py # FastAPI application
│ └── churn_model.pkl # Trained ML pipeline
├── data/
│ └── TZ.csv # Dataset
├── notebook/
│ └── churn.ipynb # EDA & model training
├── Dockerfile
├── requirements.txt
└── Readme.md


---

## ⚙️ Installation

### Prerequisites
- Python **3.10+**
- `pip`
- (Optional) Docker Desktop

### Create virtual environment (recommended)

```bash
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

Install dependencies
pip install -r requirements.txt


⚠️ Important:
The project requires scikit-learn==1.6.1 to ensure compatibility with the trained model.

🚀 Running the API Locally

From the project root:

uvicorn app.main:app --reload


If successful, you will see:

Uvicorn running on http://127.0.0.1:8000

📑 API Documentation (Swagger UI)

Open in browser:

http://127.0.0.1:8000/docs


Swagger UI allows interactive testing of the API.

🔮 API Usage
Endpoint
POST /predict

Example Request
{
  "credit_score": 650,
  "city": "Moscow",
  "gender": "Male",
  "age": 42,
  "tenure": 6,
  "balance": 120000,
  "num_products": 2,
  "has_credit_card": 1,
  "is_active": 0,
  "estimated_salary": 85000
}

Example Response
{
  "churn_probability": 0.78,
  "prediction": 1
}


churn_probability — likelihood of customer churn

prediction — binary classification (1 = churn, 0 = stay)

🐳 Docker

The application is containerized using Docker.

Build image
docker build -t churn-api .

Run container
docker run -p 8000:8000 churn-api


Then open:

http://127.0.0.1:8000/docs


⚠️ Note:
Due to Docker Desktop / buildx limitations on some Windows environments, the image build may not execute locally.
The Dockerfile is provided and verified to work in standard Docker/Linux environments.

🏁 Conclusion

This project demonstrates:

end-to-end ML workflow

strong model evaluation and explainability

production-ready API design

reproducible deployment with Docker

The solution is suitable for real-world churn prevention use cases.


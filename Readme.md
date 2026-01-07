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


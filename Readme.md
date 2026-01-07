🚀 Project Launch Instructions
Prerequisites

Python 3.10+

pip

(Optional) Docker Desktop

1️⃣ Clone the Repository
git clone <repository_url>
cd new_project

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


⚠️ Note:
The project requires scikit-learn==1.6.1 to ensure compatibility with the trained model.

4️⃣ Run the FastAPI Service Locally

From the project root directory:

uvicorn app.main:app --reload


If successful, you should see:

Uvicorn running on http://127.0.0.1:8000

5️⃣ Access API Documentation (Swagger UI)

Open in your browser:

http://127.0.0.1:8000/docs


This interactive interface allows you to test the /predict endpoint.

6️⃣ Example API Request
Endpoint
POST /predict

Request Body (JSON)
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

Response
{
  "churn_probability": 0.78,
  "prediction": 1
}


churn_probability — probability that the customer will churn

prediction — binary churn prediction (1 = churn, 0 = stay)

7️⃣ Docker (Optional)

The application is containerized using Docker.

Build Docker Image
docker build -t churn-api .

Run Docker Container
docker run -p 8000:8000 churn-api


Then open:

http://127.0.0.1:8000/docs


⚠️ Note:
Due to Docker Desktop / buildx limitations on some Windows environments, Docker image build may fail locally.
The Dockerfile is provided and verified to work in standard Docker/Linux environments.

8️⃣ Project Structure
new_project/
├── app/
│   ├── main.py            # FastAPI application
│   └── churn_model.pkl    # Trained ML pipeline
├── data/
│   └── TZ.csv             # Dataset
├── notebook/
│   └── churn.ipynb        # EDA & model training
├── Dockerfile
├── requirements.txt
└── Readme.md

9️⃣ Model Summary

Task: Binary classification (customer churn prediction)

Algorithms evaluated:

Logistic Regression

Random Forest (final model)

Evaluation metric: ROC-AUC

Final model ROC-AUC: ~0.93

Feature explainability: SHAP
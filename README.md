# ❤️ Heart Disease Prediction App

A machine learning web application that predicts the likelihood of heart disease based on clinical parameters — built with **XGBoost** and deployed via **Streamlit**.

> ⚠️ **Disclaimer:** This project is for educational purposes only and should not replace professional medical diagnosis or treatment.

---

## 🚀 Overview

Heart disease is one of the leading causes of death worldwide. Early detection can significantly improve outcomes. This app lets users input medical parameters into a simple web interface and instantly receive a risk prediction.

---

## 🧠 Model & Workflow

The model uses **XGBoost**, a high-performance gradient boosting algorithm.

1. Data preprocessing & feature scaling
2. Model training with XGBoost
3. Evaluation & serialization via `joblib`
4. Deployment with Streamlit

---

## 📊 Dataset

Trained on **`heart.csv`** — a standard heart disease dataset with the following features:

| Feature | Description |
|---|---|
| `age` | Age of the patient |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `restecg` | Resting ECG results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression (exercise vs. rest) |
| `slope` | Slope of peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia |

**Target:** `0` = No heart disease · `1` = Heart disease present

---

## 📂 Project Structure

```
Heart_Disease_App/
├── app.py                # Streamlit web application
├── heart_model.joblib    # Trained ML model
├── heart.csv             # Dataset
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ▶️ Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Heart_Disease_App.git
cd Heart_Disease_App

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

App will be available at `http://localhost:8501`

---

## 🌐 Deployment (Streamlit Cloud)

1. Push the project to GitHub
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Select the repository and set `app.py` as the entry point
4. Deploy

---

## ⚙️ Tech Stack

`Python` · `XGBoost` · `scikit-learn` · `pandas` · `NumPy` · `Streamlit` · `Joblib`

---

## 👨‍💻 Author

Built as an end-to-end ML project demonstrating model building, preprocessing, and deployment.

⭐ *If you found this useful, consider starring the repo on GitHub!*

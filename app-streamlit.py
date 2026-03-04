import streamlit as st
import pandas as pd
import joblib

model = joblib.load("hear_model.joblib")

st.title("Heart Disease Prediction")

age = st.number_input("Age", 20, 90, 40)

cp = st.selectbox("Chest pain type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting blood pressure (trestbps)", 80, 210, 120)
chol = st.number_input("Cholesterol (chol)", 100, 650, 200)

restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max heart rate (thalach)", 70, 220, 140)
exang = st.selectbox("Exercise induced angina (exang)", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

if st.button('predict'):
    df = pd.DataFrame([{
        "age": age,
        "cp":cp,
        "trestbps":trestbps,
        "chol":chol,
        "restecg":restecg,
        "thalach":thalach,
        "exang":exang,
        "oldpeak":oldpeak,
        "slope":slope,
        "ca":ca,
        "thal":thal
    }])

    pred = model.predict(df)[0]

    if pred == 1:
        st.error("Prediction: Heart Disease risk detected.")
    else:
        st.success("Prediction: No Heart Disease risk detected.")


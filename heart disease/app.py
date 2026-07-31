import streamlit as st
import joblib

# -------------------------------
# Load Trained Model
# -------------------------------
model = joblib.load("heart_disease_model.pkl")

# -------------------------------
# App Title
# -------------------------------
st.title("❤️ Heart Disease Prediction System")
st.write("Enter the patient details below.")

# -------------------------------
# Patient Details
# -------------------------------
st.header("Patient Details")

age = st.number_input("Age", min_value=1, max_value=120, value=40)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    ["No", "Yes"]
)
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG",
    [0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    min_value=60,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input(
    "Old Peak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels (ca)",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    [0, 1, 2, 3]
)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Predict"):

    input_data = [[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]]

    prediction = model.predict(input_data)

    st.header("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
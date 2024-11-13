import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'model.pkl'  # Replace with your actual file name
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the app
st.title("Diabetes Risk Prediction Tool")
st.write("Please fill in the following information to estimate your diabetes risk.")

# Input fields for the required features
st.subheader("Personal Information")
gender = st.selectbox("Select Gender:", ["Male", "Female"])
age = st.number_input("Enter Age (years):", min_value=0, max_value=120, step=1)

st.subheader("Medical History")
hypertension = st.selectbox("Hypertension History:", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease History:", ["No", "Yes"])
smoking_history = st.selectbox("Smoking History:", ["Never", "Former", "Current", "Ever", "Not Current"])

st.subheader("Health Metrics")
bmi = st.number_input("Body Mass Index (BMI):", min_value=0.0, max_value=70.0, step=0.1)
hba1c_level = st.number_input("HbA1c Level (%):", min_value=0.0, max_value=20.0, step=0.1)
blood_glucose_level = st.number_input("Blood Glucose Level (mg/dL):", min_value=0, max_value=500, step=1)

# Convert categorical variables to numeric values
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
smoking_history_dict = {"Never": 0, "Former": 1, "Current": 2, "Ever": 3, "Not Current": 4}
smoking_history = smoking_history_dict[smoking_history]

# Button to make prediction
if st.button("Calculate Diabetes Risk"):
    # Prepare input data in the required shape
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
    prediction = model.predict(input_data)

    # Display the prediction result
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.write("**The model predicts a high risk of diabetes.**")
    else:
        st.write("**The model predicts a low risk of diabetes.**")

import streamlit as st
import pandas as pd
import joblib
import urllib.request
import numpy as np

model_url = 'https://raw.githubusercontent.com/Neelkanth-khithani/Disease-Prediction-Using-ML/main/logistic-trained-model'
model_filename = 'logistic-trained-model'
urllib.request.urlretrieve(model_url, model_filename)

model = joblib.load(model_filename)

dataset_url = "https://raw.githubusercontent.com/Neelkanth-khithani/Disease-Prediction-Using-ML/main/training_dataset.csv"

df = pd.read_csv(dataset_url)

symptoms = df.columns[0:132].tolist()

symptom_binary = {symptom: 0 for symptom in symptoms}

st.title('Disease Prediction using Machine Learning')
st.caption('Dataset Courtesy: https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning')
st.write('-----------------------------------')
st.write("""
    This application uses a machine learning model to predict potential diseases based on the symptoms you select.
    Please note that this is not a substitute for professional medical advice, diagnosis, or treatment.
""")


patients_symptoms = st.multiselect('Select your symptoms', symptoms)

for symptom in patients_symptoms:
    symptom_binary[symptom] = 1

input_data = pd.DataFrame([symptom_binary])

if len(patients_symptoms) == 0:
    st.write('Please select at least one symptom.')
else:
    prediction = model.predict(input_data)
    predicted_disease = prediction[0]
    st.subheader('Prediction Result')
    st.write(f'Based on the symptoms you selected, the predicted disease is: **{predicted_disease}**')

st.warning("""
    **Disclaimer:** This prediction is for informational purposes only and should not be considered as medical advice. 
    Always seek the guidance of a qualified healthcare provider with any questions you may have regarding a medical condition.
""")
st.markdown("[GitHub Project Link - Neelkanth Khithani](https://github.com/Neelkanth-khithani/Disease-Prediction-Using-ML)")

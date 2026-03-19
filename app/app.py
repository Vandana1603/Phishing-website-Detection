import streamlit as st
import joblib
import numpy as np
import sys
import os

# Fix import path
sys.path.append(os.path.abspath("src"))
from feature_extraction import extract_features

# Load model + features
model = joblib.load("models/model.pkl")
feature_names = joblib.load("models/features.pkl")

st.title(" Phishing Website Detection")

mode = st.radio("Choose Input Method:", ["Manual Input", "Enter URL"])

inputs = []

# ------------------ MANUAL ------------------
if mode == "Manual Input":
    st.subheader("Enter Feature Values")

    for feature in feature_names:
        value = st.number_input(feature, value=0.0)
        inputs.append(value)

# ------------------ URL ------------------
else:
    st.subheader("Enter URL")

    url = st.text_input("Website URL")

    if url:
        inputs = extract_features(url)

        st.write("Extracted Features:")
        st.write(dict(zip(feature_names, inputs)))

# ------------------ PREDICTION ------------------
if st.button("Predict"):

    if len(inputs) != len(feature_names):
        st.error(" Please provide valid input")
    else:
        # ✅ DEFINE features HERE
        features = np.array(inputs).reshape(1, -1)

        # ✅ Prediction
        prediction = model.predict(features)[0]

        # ✅ Probability (FIXED)
        proba = model.predict_proba(features)[0][1]

        st.write(f"🔍 Phishing Probability: {proba:.2f}")

        if prediction == 1:
            st.error(" Phishing Website")
        else:
            st.success(" Legitimate Website")
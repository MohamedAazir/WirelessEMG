import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import joblib

# Load the pre-trained model
clf = joblib.load("D:\\sem 3\\BM device design\\ecg\\ML part\\code testing\\random_forest_updated_model.joblib")

# Function to extract 7 features (consistent with training)
def extract_features(raw_signal):
    mean_val = np.mean(raw_signal)
    std_val = np.std(raw_signal)
    max_val = np.max(raw_signal)
    min_val = np.min(raw_signal)
    range_val = max_val - min_val
    median_val = np.median(raw_signal)
    rms_val = np.sqrt(np.mean(raw_signal**2))
    
    # Combine the 7 features
    features = [mean_val, std_val, max_val, min_val, range_val, median_val, rms_val]
    return features

# Streamlit interface
st.title("Wrist Flexion Signal Classifier")
st.write("Upload a CSV file to detect whether it contains a wrist flexion signal.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV data
    data = pd.read_csv(uploaded_file)
    
    # Ensure the CSV contains an 'Amplitude' column
    if 'Amplitude' not in data.columns:
        st.error("The uploaded CSV must contain an 'Amplitude' column.")
    else:
        # Extract the Amplitude column as the raw signal
        raw_signal = data['Amplitude'].values
        
        # Extract features from the raw signal
        features = extract_features(raw_signal)
        features = np.array(features).reshape(1, -1)
        
        # Predict the class
        prediction = clf.predict(features)[0]
        
        # Display the result
        if prediction == 1:
            st.success("Wrist Flexion Detected")
        else:
            st.info("No Wrist Flexion Detected")


#streamlit run "d:/sem 3/BM device design/ecg/ML part/code testing/app_updated.py"
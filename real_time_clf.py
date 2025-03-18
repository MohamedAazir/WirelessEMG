import joblib
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis  # Import skew and kurtosis functions

# Load the pre-trained model
clf = joblib.load("D:\\sem 3\\BM device design\\ecg\\ML part\\code testing\\random_forest_updated_model.joblib")

# Function to extract 9 features (example with 9 features)
def extract_features(raw_signal):
    # Use only the features included during training
    mean_val = np.mean(raw_signal)
    std_val = np.std(raw_signal)
    max_val = np.max(raw_signal)
    min_val = np.min(raw_signal)
    range_val = max_val - min_val
    median_val = np.median(raw_signal)
    rms_val = np.sqrt(np.mean(raw_signal**2))
    
    # Combine only these 7 features (to match the training script)
    features = [mean_val, std_val, max_val, min_val, range_val, median_val, rms_val]
    
    return features

def classify_signal_from_csv(csv_file):
    # Load the CSV data
    data = pd.read_csv(csv_file)
    
    # Extract the Amplitude column as the raw signal
    raw_signal = data['Amplitude'].values  # Ensure the column name matches your dataset
    
    # Extract features from the raw signal
    features = extract_features(raw_signal)
    
    # Reshape the features to match the input format for the classifier (1 sample with multiple features)
    features = np.array(features).reshape(1, -1)
    
    # Predict the class (1 for flexion, 0 for non-flexion)
    prediction = clf.predict(features)
    
    # Output the prediction for wrist flexion or not
    if prediction == 1:
        print("Wrist Flexion Detected")
    else:
        print("No Flexion")


# Example usage:
csv_file = "D:\sem 3\BM device design\ecg\ML part\code testing\sine_wave_data.csv"  # Provide the path to your CSV file
classify_signal_from_csv(csv_file)

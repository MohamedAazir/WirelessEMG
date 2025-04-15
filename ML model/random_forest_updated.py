import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.preprocessing import StandardScaler
from scipy.signal import welch
import matplotlib.pyplot as plt
import joblib

# Load the dataset
data = pd.read_csv('D:\sem 3\BM device design\ecg\ML part\code testing\converted_data.csv')

# Feature Engineering: Extract Statistical and Frequency Features
def extract_features(row):
    features = {}
    
    # Statistical features
    features['mean'] = row.mean()
    features['std'] = row.std()
    features['max'] = row.max()
    features['min'] = row.min()
    features['range'] = row.max() - row.min()
    
    # Frequency-domain features (adjust nperseg for short signals)
    nperseg = min(len(row), 8)  # Use a maximum of 8 or the length of the row
    freqs, psd = welch(row, fs=100, nperseg=nperseg)
    features['dominant_freq'] = freqs[np.argmax(psd)] if len(freqs) > 0 else 0
    features['power'] = np.sum(psd) if len(psd) > 0 else 0
    
    return pd.Series(features)

# Apply feature extraction for each sample (row-wise)
X = data.drop(columns=['channel4']).apply(lambda row: extract_features(row), axis=1)

# Ensure target variable matches the number of rows in X
y = (data['channel4'] > 0).astype(int)  # Binary classification

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Initialize and train the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print(f"F1 Score: {f1:.2f}")

# Visualize feature importances
feature_importances = clf.feature_importances_
plt.barh(X.columns, feature_importances, color='skyblue')
plt.xlabel('Feature Importance')
plt.ylabel('Feature Names')
plt.title('Feature Importance in Random Forest')
plt.show()



# Save the model
file_path = "D:\\sem 3\\BM device design\\ecg\\ML part\\code testing\\random_forest_updated_model.joblib"
joblib.dump(clf, file_path)
print("Model saved as 'random_forest_updated_model.joblib'")

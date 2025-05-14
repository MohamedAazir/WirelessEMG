import requests
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.signal import iirnotch, filtfilt
import pandas as pd

# ESP32 IP address
ESP32_IP = "http://192.168.4.1/"

# Function to fetch EMG data from ESP32
def fetch_emg_signal():
    try:
        response = requests.get(ESP32_IP)
        response.raise_for_status()  # Raise an error for bad status codes
        emg_signal_data = response.json()  # Parse JSON response
        return emg_signal_data
    except requests.RequestException as e:
        print(f"Error fetching data from ESP32: {e}")
        return []

# Save sine wave data to a CSV file
def save_to_csv(time, amplitude, filename="emg_signal_data.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Time (s)", "Amplitude"])
            writer.writerows(zip(time, amplitude))
        print(f"Sine wave data saved to {filename}")
    except IOError as e:
        print(f"Error saving to CSV file: {e}")

# Apply a notch filter to remove 50 Hz noise
def apply_notch_filter(signal, fs, f0=50, Q=5):
    b, a = iirnotch(f0 / (fs / 2), Q)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Fetch sine wave data
emg_signal = fetch_emg_signal()

# Check if data is valid
if emg_signal:
    # Generate time axis for plotting
    sample_count = len(emg_signal)
    sampling_rate = 2000  # Adjusted sampling rate in Hz (e.g., 2 kHz)
    time = np.linspace(0, sample_count / sampling_rate, sample_count)

    # Save data to a CSV file
    save_to_csv(time, emg_signal)

    # Apply a 50 Hz notch filter
    emg_signal_fil = np.array(emg_signal)
    filtered_emg_signal = apply_notch_filter(emg_signal_fil, sampling_rate)

    # Plot the original and filtered sine wave
    plt.figure(figsize=(12, 6))
    plt.plot(time[5000:5500], emg_signal[5000:5500], label='Original Sine Wave', color='red', alpha=0.6)
    plt.plot(time[5000:5500], filtered_emg_signal[5000:5500], label='Filtered Sine Wave (50 Hz Removed)', color='blue', linewidth=1)
    plt.title("Sine Wave from ESP32 (Before and After Filtering)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()
    plt.show()
else:
    print("No data received from ESP32.")

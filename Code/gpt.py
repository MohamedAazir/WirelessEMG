import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import iirnotch, filtfilt

# Apply a notch filter to remove 50 Hz noise
def apply_notch_filter(signal, fs, f0=50, Q=30):
    b, a = iirnotch(f0 / (fs / 2), Q)  # Normalize frequency
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Load sine wave data from CSV file
csv_file = "sine_wave_50hz.csv"  # Path to your CSV file
try:
    data = pd.read_csv(csv_file)
    time = data["Time (s)"].values
    sine_wave = data["Amplitude"].values
except FileNotFoundError:
    print(f"Error: {csv_file} not found.")
    time, sine_wave = None, None

# Check if data is valid
if time is not None and sine_wave is not None:
    sampling_rate = 2000  # Sampling rate in Hz (adjust as needed)

    # Apply a 50 Hz notch filter
    filtered_sine_wave = apply_notch_filter(sine_wave, sampling_rate)

    # Plot the original and filtered sine wave
    plt.figure(figsize=(12, 6))
    plt.plot(time, sine_wave, label='Original Sine Wave', color='red', alpha=0.6)
    plt.plot(time, filtered_sine_wave, label='Filtered Sine Wave (50 Hz Removed)', color='blue', linewidth=1)
    plt.title("Sine Wave Before and After Filtering")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()
    plt.show()
else:
    print("No data available to process.")

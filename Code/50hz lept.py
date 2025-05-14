import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt

# Load the EMG data with noise from the CSV file
file_path = 'D:\Aazir\EMG_total\sine_waves.csv'
emg_dataset = pd.read_csv(file_path)

# Extract time and signal values
t = emg_dataset["Time"].values
emg_signal_with_noise = emg_dataset["Summed_Signal"].values

# Parameters for the notch filter
fs = 10000  # Sampling frequency in Hz
f0 = 50    # Powerline frequency to be removed
Q = 5     # Quality factor

# Design the notch filter
b, a = iirnotch(f0, Q, fs)

# Apply the notch filter to the EMG signal with noise
filtered_emg_signal = filtfilt(b, a, emg_signal_with_noise)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(t, emg_signal_with_noise, label='Original EMG Signal with Noise', color='red', alpha=0.6)
plt.plot(t, filtered_emg_signal, label='Filtered EMG Signal (50 Hz Removed)', color='blue', linewidth=1)
plt.title('EMG Signal Before and After Notch Filtering')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

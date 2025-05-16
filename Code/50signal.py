import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set parameters
frequency1 = 50  # 50 Hz sine wave
frequency2 = 100  # 100 Hz sine wave
sampling_rate = 10000  # 1000 samples per second
duration = 0.3  # 1 second total duration

# Create time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine waves
sine1 = np.sin(2 * np.pi * frequency1 * t)
sine2 = np.sin(2 * np.pi * frequency2 * t)

# Sum the sine waves
summed_signal = sine1 + sine2

# Create DataFrame
df = pd.DataFrame({
    'Time': t,
    '50Hz_Sine': sine1,
    '100Hz_Sine': sine2,
    'Summed_Signal': summed_signal
})

# Save to CSV
df.to_csv('sine_waves.csv', index=False)

print("Sine wave data has been saved to sine_waves.csv")

plt.figure(figsize=(12, 6))
plt.plot(t, summed_signal, label='Original EMG Signal with Noise', color='red', alpha=0.6)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
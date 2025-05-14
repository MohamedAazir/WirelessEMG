import requests
import matplotlib.pyplot as plt
import numpy as np
import csv

# ESP32 IP address (replace with the correct one from your Serial Monitor)
ESP32_IP = "http://192.168.4.1/"

# Function to fetch sine wave data from ESP32
def fetch_sine_wave():
    try:
        response = requests.get(ESP32_IP)
        response.raise_for_status()  # Raise an error for bad status codes
        sine_wave_data = response.json()  # Parse JSON response
        return sine_wave_data
    except requests.RequestException as e:
        print(f"Error fetching data from ESP32: {e}")
        return []

# Save sine wave data to a CSV file
def save_to_csv(time, amplitude, filename="sine_wave_data.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(fileC:/Python312/python.exe "d:/Aazir/EMG_total/all together.py")
            writer.writerow(["Time (s)", "Amplitude"])
            writer.writerows(zip(time, amplitude))
        print(f"Sine wave data saved to {filename}")
    except IOError as e:
        print(f"Error saving to CSV file: {e}")

# Fetch sine wave data
sine_wave = fetch_sine_wave()

# Check if data is valid
if sine_wave:
    # Generate time axis for plotting
    sample_count = len(sine_wave)
    sampling_rate = 10  # Adjusted sampling rate in Hz (e.g., 2 kHz)
    time = np.linspace(0, sample_count / sampling_rate, sample_count)

    # Save data to a CSV file
    save_to_csv(time, sine_wave)

    # Plot the sine wave
    plt.plot(time[100:1000], sine_wave[100:1000])  # Plot only the first 500 samples for clarity
    plt.title("Sine Wave from ESP32")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
else:
    print("No data received from ESP32.")

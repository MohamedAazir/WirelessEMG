# Wireless sEMG Monitoring Device

<div align="center">
  <img src="https://github.com/user-attachments/assets/6518390a-a886-490f-900e-de0ceeaffaa8" alt="Breadboard Implementation" height="400"/>
</div>



This is the repository of a wireless EMG device built for our module **BM2210-Bio Medical Device Design**. The device senses the forearm muscle signals on flexion and extension and then goes through an amplification and filtering part which at last will be transmitted to a laptop where the classification happens. The speciality of the device is that most of the main circuitry of the device was developed using analog electronic components.

## Repository Contents

- 🔌 **Circuit Design**
- 🧪 **Simulation Results**  
- 🔧 **Breadboard Implementation** 
- 🧩 **PCB Design**  
- 🧱 **Enclosure Design**   
- 📡 **Wireless Transmission**  
- 🤖 **ML Model Development**  
- 📄 **Documentation**

## 🔌 Circuit Design

The circuit design consists of four main parts: an **instrumentation amplifier**, a h**igh-pass filter**, a **low-pass filter**, and a **notch filter**. Each part plays a critical role in conditioning the raw bioelectrical signals before further processing or analysis.

### 1. 🎛️ Instrumentation Amplifier

This stage is responsible for amplifying the weak differential signal received from the electrodes while rejecting common-mode noise. It ensures that even very small biopotential signals are amplified to a usable level without being distorted by environmental interference. This is crucial in biomedical applications where the signal strength is often in the microvolt range and needs clean amplification before filtering.
<div align="center">
  <img src=https://github.com/user-attachments/assets/f8319dda-f469-44f4-a1bd-92cc7c474d31 alt="Instrumentation Amplifier" height="400"/>
</div>

### 2. 🔼 1st Order Active High Pass Filter

We use a **first-order active high-pass filter** with a cut-off frequency of **15.4 Hz**. The main purpose of this filter is to remove low-frequency components from the signal, including **DC offsets and motion artifacts** that can otherwise distort the meaningful parts of the bioelectrical signal. By using an active filter design, we ensure better performance and minimal signal attenuation in the passband.

<div align="center">
  <img src=https://github.com/user-attachments/assets/f3ef3027-d3fa-47bf-b726-5b52eb408bc8 alt="HPF" height="400"/>
</div>

### 3. 🔽 5th Order Bessel Low Pass Filter

To preserve the integrity of the signal's shape while eliminating high-frequency noise, we implement a **fifth-order Bessel low-pass filter**. This is achieved using a cascaded system comprising one 1st order active low-pass filter and two 2nd order active low-pass filters. The overall cut-off frequency is around **450 Hz to 460 Hz**. The Bessel filter is chosen for its linear phase response, which helps maintain the waveform fidelity of the signal—an important factor for downstream analysis and visualization.

<div align="center">
  <img src=https://github.com/user-attachments/assets/3d2a56df-bdc9-4575-9532-30455f28a576 alt="LPF" height="400"/>
</div>

### 4. 🚫 Twin-T Notch Filter

To eliminate **powerline interference at 50 Hz**, we use a twin-T notch filter. This type of filter is highly effective at attenuating a narrow frequency band, in this case, the frequency commonly introduced by electrical noise in power systems. Our implementation includes five potentiometers to fine-tune the filter: three are used to precisely set the notch frequency, and two are used to adjust the desired roll-off. This allows for flexibility in tuning and ensures that the filter performs effectively in different environments.

<div align="center">
  <img src=https://github.com/user-attachments/assets/794e0190-1e76-483f-b026-380064e9bbf6 alt="Notch Filter" height="400"/>
</div>

## Simulation Results

We simulated our designed circuit using LT spice software where we able to visualize the frequency response of each filtering stage.  

<div align="center">
  <img src=https://github.com/user-attachments/assets/fb5f9f4b-d5e0-421c-ae32-5d763c1a61bf alt="HP Filter" height="200"/>
</div>

The frequency response after the High pass filter

<div align="center">
  <img src= https://github.com/user-attachments/assets/ac570e15-65d8-4dfc-a82d-c50d4409dde5 alt="HP Filter" height="200"/>
</div>

The frequency response after the Low pass filter

<div align="center">
  <img src= https://github.com/user-attachments/assets/ecf51b56-bbdf-43ff-bea1-b7727f43250b alt="HP Filter" height="200"/>
</div>

The frequency response after the Notch filter

## Breadboard Implementation

The breadboard implementation was used in the early stages for prototyping and testing the EMG signal acquisition, filtering, and wireless transmission before finalizing the PCB. It serves as a reference for understanding the initial circuit layout and testing procedure.

<div align="center">
  <img src="https://github.com/user-attachments/assets/362a04dd-55c9-49be-b13d-9621e3c1e66e" alt="breadboard" width="50%"/>
</div>

## PCB Design

When designing the printed circuit board (PCB) for our wireless sEMG monitoring device, we utilized EasyEDA
software to design a **4-layer PCB**. This tool allowed us to efficiently create and simulate the PCB layout, ensuring optimal design for
signal conditioning, sampling, and wireless transmission. EasyEDA’s user-friendly interface and extensive
library of components made it well-suited for the development of this biomedical application. By leveraging
its advanced features, we were able to streamline the PCB design process and ensure the circuit met the
requirements of the wireless sEMG monitoring system.

<div align="center">
  <img src=https://github.com/user-attachments/assets/72d18e03-74e4-42ce-88a3-555db2d10891 alt="PCB Layout" width="60%"/>
</div>

After finalizing the PCB, we choosed JLC PCB which is a professional PCB Manufacturer for the production of our PCBs.

<div align="center">
  <img src=https://github.com/user-attachments/assets/d6ac227b-d0c8-41f8-a2c0-dd463844fb84 alt="PCB 3D Layout" width="60%"/>
</div>

## Enclosure Design

We used SOLIDWORKS software for the designing of the enclosure. The enclosure consists of a top lid, bottom part, and a battery compartment. The device is designed as a compact wearable design which makes it easy to fetch the EMG signals.
<div align="center">
  <img src=https://github.com/user-attachments/assets/b75b1b76-8e1c-490c-a5a1-8108e27f88ea alt="Enclosure1" width="60%"/>
</div>

<div align="center">
  <img src=https://github.com/user-attachments/assets/0a7b4cf1-9c11-4b72-8637-51e068bed8ba alt="Enclosure2" width="60%"/>
</div>

<div align="center">
  <img src=https://github.com/user-attachments/assets/2de5788f-dc87-41e4-9e29-473907e608f8 alt="Enclosure3" width="60%"/>
</div>

## Coding & Wireless Transmission

The final filtered signal is transmissed using Wifi through an ESP32 micro controller to the host computer. The computer then samples the signal and sends it through a digital filtering process using the **scipy** library. Then the final values are saved as a .csv file to be classified in the ML model.

## ML Model Development

A detailed description of the ML model is shown [here](./ML-model)

## Our Team 

- Praveen Samuditha
- Hansani Kaumadhi
- Mohamed Aazir

<div align="center">
  <img src= https://github.com/user-attachments/assets/cc2a8ca3-5ec8-4fba-922c-86cd6e676983 alt="Enclosure3" width="60%"/>
</div>

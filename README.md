# Wireless sEMG Monitoring Device

<div align="center">
  <img src="https://github.com/user-attachments/assets/6518390a-a886-490f-900e-de0ceeaffaa8" alt="Breadboard Implementation" width="40%" height="400"/>
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

### 2. 🔼 1st Order Active High Pass Filter

We use a **first-order active high-pass filter** with a cut-off frequency of **15.4 Hz**. The main purpose of this filter is to remove low-frequency components from the signal, including **DC offsets and motion artifacts** that can otherwise distort the meaningful parts of the bioelectrical signal. By using an active filter design, we ensure better performance and minimal signal attenuation in the passband.

### 3. 🔽 5th Order Bessel Low Pass Filter

To preserve the integrity of the signal's shape while eliminating high-frequency noise, we implement a **fifth-order Bessel low-pass filter**. This is achieved using a cascaded system comprising one 1st order active low-pass filter and two 2nd order active low-pass filters. The overall cut-off frequency is around **450 Hz to 460 Hz**. The Bessel filter is chosen for its linear phase response, which helps maintain the waveform fidelity of the signal—an important factor for downstream analysis and visualization.

### 4. 🚫 Twin-T Notch Filter

To eliminate **powerline interference at 50 Hz**, we use a twin-T notch filter. This type of filter is highly effective at attenuating a narrow frequency band, in this case, the frequency commonly introduced by electrical noise in power systems. Our implementation includes five potentiometers to fine-tune the filter: three are used to precisely set the notch frequency, and two are used to adjust the desired roll-off. This allows for flexibility in tuning and ensures that the filter performs effectively in different environments.








## Breadboard Implementation

The breadboard implementation was used in the early stages for prototyping and testing the EMG signal acquisition, filtering, and wireless transmission before finalizing the PCB. It serves as a reference for understanding the initial circuit layout and testing procedure.

<div align="center">
  <img src="https://github.com/user-attachments/assets/362a04dd-55c9-49be-b13d-9621e3c1e66e" alt="breadboard" width="50%"/>
</div>

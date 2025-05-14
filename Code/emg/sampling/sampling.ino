// Arduino Code
const int analogPin = 34; // Analog input pin
const int sampleCount = 15000; // Collect samples for 15 seconds at 1 kHz
float analogValues[sampleCount]; // Array to hold analog readings

// Function to collect analog readings
void collectAnalogReadings() {
  for (int i = 0; i < sampleCount; i++) {
    float rawValue = analogRead(analogPin); // Read raw ADC value
    analogValues[i] = (rawValue / 4095.0) * 3.3; // Scale to 0-3.3V (ESP32 ADC range)
    delayMicroseconds(1000); // 1 kHz sampling rate
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("Sine Wave Data Plotting Started");
}

void loop() {
  collectAnalogReadings();

  // Send analog readings to Serial for plotting
  for (int i = 0; i < sampleCount; i++) {
    Serial.println(analogValues[i]);
  }
}

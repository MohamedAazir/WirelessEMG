// Analog input pin
const int analogPin = 34;

// Number of samples to collect
const int sampleCount = 10000;
float analogValues[sampleCount]; // Array to hold analog readings

// Function to collect analog readings
void collectAnalogReadings() {
  for (int i = 0; i < sampleCount; i++) {
    analogValues[i] = analogRead(analogPin);
    delay(0.01); // Small delay to space out readings
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("Sine Wave Data Plotting Started");
}

void loop() {
  // Collect analog readings
  collectAnalogReadings();

  // Plot analog readings on Serial Plotter
  for (int i = 0; i < sampleCount; i++) {
    Serial.println(analogValues[i]);
  }
}

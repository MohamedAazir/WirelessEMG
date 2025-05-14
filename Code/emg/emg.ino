#include <WiFi.h>
#include <WebServer.h>
#include <math.h>

// Wi-Fi Access Point credentials
const char* ssid = "Medicore";
const char* password = "12345678";

// Create an HTTP server instance
WebServer server(80);

// Sine wave sampling parameters
const int sampleCount = 10000;  // Number of samples to transmit (time duration)
const int analogPin = 34;     // Analog input pin
const int offset = 1.6;
float analogValues[sampleCount];  // Array to hold sampled analog values

// Function to collect analog readings
void collectAnalogReadings() {
  for (int i = 0; i < sampleCount; i++) {
    analogValues[i] = (analogRead(analogPin) * 3.3) / 4095.0 - offset; // Convert ADC value to voltage
    delayMicroseconds(500); // 100 kHz sampling rate
  }
}

// Function to handle root page requests
void handleRoot() {
  collectAnalogReadings(); // Collect sine wave samples from analog pin

  String jsonResponse = "[";

  // Convert sampled analog data to JSON format
  for (int i = 0; i < sampleCount; i++) {
    jsonResponse += String(analogValues[i]);
    if (i < sampleCount - 1) {
      jsonResponse += ",";
    }
  }
  jsonResponse += "]";

  // Send JSON response
  server.send(200, "application/json", jsonResponse);
}

void setup() {
  Serial.begin(115200);

  // Start Wi-Fi as Access Point
  WiFi.softAP(ssid, password);
  Serial.println("Wi-Fi Access Point started");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());

  // Configure HTTP server routes
  server.on("/", handleRoot);

  // Start the HTTP server
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}

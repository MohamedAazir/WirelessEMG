#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <WiFi.h>
#include <WebServer.h>
#include <math.h>

// Define OLED display dimensions
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define SSD1306_I2C_ADDRESS 0x3C // in Adafruit_SSD1306.h
// Define OLED reset pin (set to -1 if not used)
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Battery level pin and variables
#define BATTERY_PIN 35
#define BUTTON_PIN 15
int batteryLevel = 0;
bool isRecording = false;

// Wi-Fi Access Point credentials
const char* ssid = "Medicore";
const char* password = "12345678";

// Create an HTTP server instance
WebServer server(80);

// EMG signal sampling parameters
const int sampleCount = 10000;  // Number of samples to transmit (time duration)
const int analogPin = 34;     // Analog input pin
const int offset = 2;
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
  collectAnalogReadings(); // Collect EMG signal samples from analog pin

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
  // Initialize serial communication
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

  // Initialize OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }

  // Set up button pin
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  // Clear the display buffer
  display.clearDisplay();

  // Display the welcome screen
  //displayWelcomeScreen();
  delay(3000); // Wait for 3 seconds

  // Clear the screen for the next message
  display.clearDisplay();
  display.display();
}

void loop() {
  // // Read battery level
  // batteryLevel = analogRead(BATTERY_PIN);

  // // Check if the button is pressed
  // if (digitalRead(BUTTON_PIN) == LOW && !isRecording) {
  //   isRecording = true;

  //   server.handleClient();
    
  //   displayRecordingScreen();
  //   delay(3000); // Simulate recording time
  //   displayDoneScreen();
  //   delay(2000); // Wait before turning off the display
  //   display.clearDisplay();
  //   display.display();
  //   isRecording = false;
  // } else if (!isRecording) {
  //   // Display the message and battery indicator
  //   displayMessageWithBattery("Click the button to start recording");
  displayWelcomeScreen();
  delay(1000);
  }



void displayWelcomeScreen() {
  // Display welcome message
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10, 20);
  display.setTextSize(2);
  display.println("WiEMG");
  display.setTextSize(1);
  display.setCursor(50, 45);
  display.println("by Medicore ");

  // Update the display with the buffer
  display.display();
}

void displayMessageWithBattery(const char* message) {
  // Clear the display buffer
  display.clearDisplay();

  // Display battery level indicator
  displayBatteryIndicator();

  // Display the main message
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 30);
  display.println(message);

  // Update the display with the buffer
  display.display();
}

void displayRecordingScreen() {
  // Clear the display buffer
  display.clearDisplay();

  // Display "Recording..." message
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 30);
  display.println("Recording......");

  // Update the display with the buffer
  display.display();
}

void displayDoneScreen() {
  // Clear the display buffer
  display.clearDisplay();

  // Display "Done" message
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 30);
  display.println("Done");

  // Update the display with the buffer
  display.display();
}

void displayBatteryIndicator() {
  // Map battery level to a percentage
  int batteryPercent = map(batteryLevel, 0, 4095, 0, 100);

  // Draw the battery outline
  display.drawRect(110, 5, 16, 8, SSD1306_WHITE);
  display.drawRect(126, 7, 2, 4, SSD1306_WHITE); // Battery positive terminal

  // Fill the battery level
  int fillWidth = map(batteryPercent, 0, 100, 0, 14);
  display.fillRect(112, 7, fillWidth, 4, SSD1306_WHITE);

  // Display the percentage value (optional)
  display.setCursor(90, 5);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.print(batteryPercent);
  display.print("%");
}

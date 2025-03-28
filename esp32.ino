#include <Arduino.h>

#define LED1 2  // LED for Button 1
#define LED2 4  // LED for Button 2
#define LED3 5  // LED for Button 3

void setup() {
    Serial.begin(115200);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char state = Serial.read();
        
        // Turn off all LEDs first
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        
        // Blink the corresponding LED
        if (state == '1') {
            blinkLED(LED1);  
        } else if (state == '2') {
            blinkLED(LED2);  
        } else if (state == '3') {
            blinkLED(LED3);  
        }
    }
}

// Function to blink LED
void blinkLED(int ledPin) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
}
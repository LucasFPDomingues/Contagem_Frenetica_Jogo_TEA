// C++ code
//
void setup()
{
  pinMode(2, INPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
}
        
void loop()
{
  if (digitalRead(2) == 1) {
    tone(6, 349, 200); // play tone 53 (F4 = 349 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("Q");
  }
  if (digitalRead(3) == 1) {
    tone(6, 349, 50); // play tone 53 (F4 = 349 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("W");
  }
  if (digitalRead(4) == 1) {
    tone(6, 349, 50); // play tone 53 (F4 = 349 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("E");
  }
  if (digitalRead(5) == 1) {
    tone(6, 349, 50); // play tone 53 (F4 = 349 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("R");
  }
  if (digitalRead(8) == 1) {
    tone(6, 277, 50); // play tone 49 (C#4 = 277 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("A");
  }
  if (digitalRead(9) == 1) {
    tone(6, 277, 50); // play tone 49 (C#4 = 277 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("S");
  }
  if (digitalRead(10) == 1) {
    tone(6, 277, 50); // play tone 49 (C#4 = 277 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("D");
  }
  if (digitalRead(11) == 1) {
    tone(6, 277, 50); // play tone 49 (C#4 = 277 Hz)
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("F");
  }
  if (digitalRead(12) == 1) {
    digitalWrite(6, HIGH);
    delay(200); // Wait for 200 millisecond(s)
    Serial.println("espaco");
  }
}
// Initialise pins and variables
int led1 = 2; 
int sensor1 = A0;
float value1 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(sensor1, INPUT);
  digitalWrite(led1, HIGH);
  delay(500);
}

void loop() {
  //Serial.print("Moisture level: ");
  value1 = analogRead(sensor1);
  Serial.println(value1);
  if(value1 > 500)
  {
    digitalWrite(led1, HIGH);
  }
  else
    digitalWrite(led1, LOW);
  delay(5000);
}

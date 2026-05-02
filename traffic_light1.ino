// C++ code
void setup(){
  pinMode(12,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(7,OUTPUT);
}
void loop(){
  digitalWrite(12,HIGH);
  delay(5000);
  digitalWrite(12,LOW);
  delay(1000);
  digitalWrite(9,HIGH);
  delay(2000);
  digitalWrite(9,LOW);
  delay(1000);
  digitalWrite(7,HIGH);
  delay(5000);
  digitalWrite(7,LOW);
  delay(1000);
}
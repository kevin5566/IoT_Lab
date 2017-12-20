int bottom = 3;       //instead water sensor
int signal_pi = 13;   //hard wire 

void setup() {
  pinMode(bottom, INPUT);
  pinMode(signal_pi, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(bottom)==HIGH){
    digitalWrite(signal_pi,HIGH);
  }
  else{
    digitalWrite(signal_pi,LOW);
  }
}

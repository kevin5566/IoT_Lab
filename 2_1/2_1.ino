int bottom = 3;
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(bottom, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(bottom)==HIGH){
    digitalWrite(led,HIGH);
  }
  else{
    digitalWrite(led,LOW);
  }
}

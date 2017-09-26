int bottom = 3;
int R = 11;
int G = 12;
int B = 13;
int count = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(bottom, INPUT);
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(bottom)==HIGH){
    count++;
  }
  count = count%3;
  switch (count){
    case 0:
      digitalWrite(R,HIGH);
      digitalWrite(G,LOW);
      digitalWrite(B,LOW);
      break;
    case 1:
      digitalWrite(R,LOW);
      digitalWrite(G,HIGH);
      digitalWrite(B,LOW);
      break;
    case 2:
      digitalWrite(R,LOW);
      digitalWrite(G,LOW);
      digitalWrite(B,HIGH);
      break;
  }
}

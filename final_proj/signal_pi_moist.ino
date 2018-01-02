int signal_pi = 13;   //hard wire 

void setup() {
  pinMode(A0, INPUT);
  pinMode(signal_pi, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  int moist;
  moist = analogRead(A0);
  Serial.println(moist);
  
  if(moist < 50){
    digitalWrite(signal_pi,HIGH);
  }
  else{
    digitalWrite(signal_pi,LOW);
  }

  delay(10000);
}

// Ref //
// http://atceiling.blogspot.tw/2017/06/arduinoyl-38-yl-69.html?m=1

#include <Servo.h>

Servo cameraPan, cameraTilt;
int pan = 90, tilt = 150;
int x = 0, y = 0;
 
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  cameraPan.attach(8);
  cameraTilt.attach(9);
  cameraPan.write(90);
  cameraTilt.write(150);
  while(!Serial.available()){
    Serial.println("waiting to connect");
    delay(500);
  }
  Serial.flush();
  Serial.println("ready...");
}

void loop() {
  processLine();
  output_motor();
}

void processLine(){
  if(Serial.available()){
    String line = Serial.readStringUntil('/n');
    x = line.substring(0, line.indexOf('b')).toInt();
    y = line.substring(line.indexOf('b')+1, line.length()).toInt();
  }
  /*Serial.print("pan= ");
  Serial.print(pan);
  Serial.print(" tilt= ");
  Serial.println(tilt);*/
}

void output_motor(){
  if(y > 30){
    tilt--;
  } else if(y < -30){
    tilt++;
  } 
  cameraPan.write(pan);
  delay(15);
  cameraTilt.write(tilt);
  delay(15);
}

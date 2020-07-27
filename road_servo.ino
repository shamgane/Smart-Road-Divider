#include <Servo.h>             //Servo library
 
Servo servo_test;        //initialize a servo object for the connected servo  
                
int angle;   
int buzz = 11;
int motor = 9;
int red = 13;
int green = 8;
int road_area;
int road_input;
float time_now;

void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(red, OUTPUT); //make the LED pin (13) as output
  pinMode(green, OUTPUT); //make the LED pin (13) as output
  pinMode(buzz,OUTPUT); //buzzer pin
  digitalWrite(red, LOW);
  digitalWrite(green,HIGH);
  //Serial.println("Divider movement (Y/N)?");

   servo_test.attach(9);      // attach the signal pin of servo to pin9 of arduino
   servo_test.write(0);
}

void loop() {
if (Serial.available()>0){
  road_area = Serial.read();
  //Serial.println(road_area);
      if(road_area=='A')
      {
      
      
      if (angle!=0)
      {
        digitalWrite(green,LOW);
        delay(100);
        digitalWrite(red,HIGH);
        tone(buzz,1000);
        //digitalWrite(buzz,HIGH);
        for(angle = 180; angle>=1; angle-=1)     // command to move from 180 degrees to 0 degrees 
        {                                
          servo_test.write(angle);              //command to rotate the servo to the specified angle
          delay(15);                       
        } 
        
        noTone(buzz);
        delay(5);
        digitalWrite(red,LOW);
        delay(100);
        digitalWrite(green,HIGH);
      }
      
      }
      
      if(road_area=='B')
      {
      
      if (angle!=180)
      {
          digitalWrite(green,LOW);
          delay(100);
          digitalWrite(red,HIGH);
          tone(buzz,1000);
          //digitalWrite(buzz,HIGH);
          for(angle = 0; angle < 180; angle += 1)    // command to move from 0 degrees to 180 degrees 
          {                                  
              servo_test.write(angle);                 //command to rotate the servo to the specified angle
              delay(15);                       
          } 
          noTone(buzz);
          delay(5);
          digitalWrite(red,LOW);
          delay(100);
          digitalWrite(green,HIGH);
      }
      }
//delay(1000);
}
}

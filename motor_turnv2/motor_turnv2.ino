#include <LiquidCrystal.h>

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
String commandString = "";
String commandName = "";
String dataString = "";

int led1Pin = 19;
int led2Pin = 20;
int led3Pin = 21;

boolean isConnected = false;

const int RS=47;
const int RD=45;
const int RP=43;

const int LS=53;
const int LD=51;
const int LP=49;

const int US=46;
const int UD=44;
const int UP=42;

const int DS=52;
const int DD=50;
const int DP=48;

const int FS=24;
const int FD=23;
const int FP=22;

const int BS=27;
const int BD=26;
const int BP=25;


void setup() {
  
  Serial.begin(9600);
  pinMode(RP, OUTPUT);
  pinMode(LP, OUTPUT); 
  pinMode(UP, OUTPUT); 
  pinMode(DP, OUTPUT); 
  pinMode(FP, OUTPUT); 
  pinMode(BP, OUTPUT); 
  
  pinMode(RS, OUTPUT);
  pinMode(LS, OUTPUT);
  pinMode(US, OUTPUT);
  pinMode(DS, OUTPUT);
  pinMode(FS, OUTPUT);
  pinMode(BS, OUTPUT);
  
  pinMode(RD, OUTPUT);
  pinMode(LD, OUTPUT);
  pinMode(UD, OUTPUT);
  pinMode(DD, OUTPUT);
  pinMode(FD, OUTPUT);
  pinMode(BD, OUTPUT);
  
//  digitalWrite(RP, HIGH);
//  digitalWrite(LP, HIGH);
//  digitalWrite(UP, HIGH);
//  digitalWrite(DP, HIGH);
//  digitalWrite(FP, HIGH);
//  digitalWrite(BP, HIGH);
}

void loop() {
if(stringComplete)
{
  while (true) {
    getNextCommand();
    Serial.println(commandName);
    // ============-POWER-=================
      // POWER ON
      if (commandName.equals("a"))
      {
          digitalWrite(RP, LOW);
          digitalWrite(LP, LOW);
          digitalWrite(UP, LOW);
          digitalWrite(DP, LOW);
          digitalWrite(FP, LOW);
          digitalWrite(BP, LOW);
      }
      // POWER OFF
      else if (commandName.equals("b"))
      {
          delay(1000);
          digitalWrite(RP, HIGH);
          digitalWrite(LP, HIGH);
          digitalWrite(UP, HIGH);
          digitalWrite(DP, HIGH);
          digitalWrite(FP, HIGH);
          digitalWrite(BP, HIGH);
      }
    // ============-POWER-=================


    // ============-DIRECTION-=================
      // CLOCKWISE
      else if (commandName.equals("c"))
      {
          digitalWrite(RD, LOW);
          digitalWrite(LD, LOW);
          digitalWrite(UD, LOW);
          digitalWrite(DD, LOW);
          digitalWrite(FD, LOW);
          digitalWrite(BD, LOW);
      }
      // COUNTER CLOCKWISE
      else if (commandName.equals("d"))
      {
          digitalWrite(RD, HIGH);
          digitalWrite(LD, HIGH);
          digitalWrite(UD, HIGH);
          digitalWrite(DD, HIGH);
          digitalWrite(FD, HIGH);
          digitalWrite(BD, HIGH);
      }
    // ============-DIRECTION-=================


    // ==============-TURN-====================
      // RIGHT
      else if (commandName.equals("e"))
      {
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(RS, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(RS, LOW);
                  delayMicroseconds(110);
          
              }
      }
      // LEFT
      else if (commandName.equals("f"))
      {
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(LS, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(LS, LOW);
                  delayMicroseconds(110);
          
              }
      }
      // UP
      else if (commandName.equals("g"))
      {
          Serial.println("ready2");
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(US, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(US, LOW);
                  delayMicroseconds(110);
          
              }
      }
      // DOWN
      else if (commandName.equals("h"))
      {
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(DS, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(DS, LOW);
                  delayMicroseconds(110);
          
              }
      }
      // FRONT
      else if (commandName.equals("i"))
      {
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(FS, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(FS, LOW);
                  delayMicroseconds(110);
          
              }
      }
      // BACK
      else if (commandName.equals("j"))
      {
          for (int i = 0; i < 200; i++)
              {
                  digitalWrite(BS, HIGH);
                  delayMicroseconds(120);
                  digitalWrite(BS, LOW);
                  delayMicroseconds(110);
          
              }
      }
    // ==============-TURN-====================

    
    if(inputString.equals("|")) {
      stringComplete = false;
      inputString = "";
      Serial.println("ready");
      break;
    }
  }
}

}

void getNextCommand() {
    commandName = inputString.substring(0, 1);
    inputString = inputString.substring(1, inputString.indexOf("|") + 1); 
}

void getCommandName()
{
  if(inputString.length()>0)
  {
     commandName = commandString.substring(1, commandString.indexOf('['));
  }
}

void getData()
{
  if(inputString.length()>0)
  {
     dataString = commandString.substring(commandString.indexOf('[') + 1, (commandString.indexOf(']')));
  }
}



void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '|') {
      stringComplete = true;
    }
  }
}

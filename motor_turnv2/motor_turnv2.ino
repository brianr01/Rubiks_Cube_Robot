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
  getNextCommand();
  getCommandName();
  getData();
  if(commandName.equals("3"))
  {
    turn();
  }
  if (commandName.equals("1"))
  {
    power();
  }
  if (commandName.equals("2"))
  {
    changeDirection();
  }

  if(inputString.equals("|")) {
    stringComplete = false;
    inputString = "";
    Serial.println(inputString);
  }

}

}

void getNextCommand() {
    commandString = inputString.substring(0, inputString.indexOf(">") + 1);
    inputString = inputString.substring(inputString.indexOf(">") + 1, inputString.indexOf("|") + 1); 
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

void power()
{
    if (dataString.equals("1"))
    {
        digitalWrite(RP, LOW);
        digitalWrite(LP, LOW);
        digitalWrite(UP, LOW);
        digitalWrite(DP, LOW);
        digitalWrite(FP, LOW);
        digitalWrite(BP, LOW);
    }
    if (dataString.equals("0"))
    {
        digitalWrite(RP, HIGH);
        digitalWrite(LP, HIGH);
        digitalWrite(UP, HIGH);
        digitalWrite(DP, HIGH);
        digitalWrite(FP, HIGH);
        digitalWrite(BP, HIGH);
    }
}

void turn()
{
    if (dataString.equals("0"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(RS, HIGH);
                delayMicroseconds(110);
                digitalWrite(RS, LOW);
                delayMicroseconds(110);
        
            }
    }
    if (dataString.equals("1"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(LS, HIGH);
                delayMicroseconds(110);
                digitalWrite(LS, LOW);
                delayMicroseconds(110);
        
            }
    }
    if (dataString.equals("2"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(US, HIGH);
                delayMicroseconds(110);
                digitalWrite(US, LOW);
                delayMicroseconds(110);
        
            }
    }
    if (dataString.equals("3"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(DS, HIGH);
                delayMicroseconds(110);
                digitalWrite(DS, LOW);
                delayMicroseconds(110);
        
            }
    }
    if (dataString.equals("4"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(FS, HIGH);
                delayMicroseconds(110);
                digitalWrite(FS, LOW);
                delayMicroseconds(110);
        
            }
    }
    if (dataString.equals("5"))
    {
        for (int i = 0; i < 200; i++)
            {
                digitalWrite(BS, HIGH);
                delayMicroseconds(110);
                digitalWrite(BS, LOW);
                delayMicroseconds(110);
        
            }
    }
}

void changeDirection()
{
    if (dataString.equals("1"))
    {
        digitalWrite(RD, LOW);
        digitalWrite(LD, LOW);
        digitalWrite(UD, LOW);
        digitalWrite(DD, LOW);
        digitalWrite(FD, LOW);
        digitalWrite(BD, LOW);
    }
    if (dataString.equals("0"))
    {
        digitalWrite(RD, HIGH);
        digitalWrite(LD, HIGH);
        digitalWrite(UD, HIGH);
        digitalWrite(DD, HIGH);
        digitalWrite(FD, HIGH);
        digitalWrite(BD, HIGH);
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

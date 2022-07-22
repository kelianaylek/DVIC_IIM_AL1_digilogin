#include <Keypad.h>
#define LDR A1 // composante photorésistance sur la pin A1

const int ROW_NUM = 4;    // four rows
const int COLUMN_NUM = 4; // three columns

char keys[ROW_NUM][COLUMN_NUM] = {
    {'1', '2', '3', 'A'},
    {'4', '5', '6', 'B'},
    {'7', '8', '9', 'C'},
    {'*', '0', '#', 'D'}};

byte pin_rows[ROW_NUM] = {9, 8, 7, 6};      // connect to the row pinouts of the keypad
byte pin_column[COLUMN_NUM] = {5, 4, 3, 2}; // connect to the column pinouts of the keypad

Keypad keypad = Keypad(makeKeymap(keys), pin_rows, pin_column, ROW_NUM, COLUMN_NUM);

String password = "";
String input_password;

void setup()
{
  Serial.begin(9600);
  input_password.reserve(32);

  pinMode(LDR, INPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  char key = keypad.getKey();

  if (key)
  {
    input_password += key;

    Serial.println(input_password + "/" + analogRead(LDR));

    if (analogRead(LDR) < 300)
    {
      digitalWrite(13, HIGH);
    }
    else
    {
      digitalWrite(13, LOW);
    }
  }
}
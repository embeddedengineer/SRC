#include <Adafruit_GFX.h>
#include <MCUFRIEND_kbv.h>
#include <TouchScreen.h>
#include <EEPROM.h>

#define MINPRESSURE 200
#define MAXPRESSURE 1000

MCUFRIEND_kbv tft;

// ALL Touch panels and wiring is DIFFERENT
// copy-paste results from TouchScreen_Calibr_native.ino
const int XP = 8, XM = A2, YP = A3, YM = 9; //ID=0x9341
const int TS_LEFT = 139, TS_RT = 870, TS_TOP = 922, TS_BOT = 111;


TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

// Setup Mode to set the 2 teams & the squad . 
Adafruit_GFX_Button SetupMode , RunningMode  , Team1 , Team2;
Adafruit_GFX_Button *buttons[] = {&SetupMode , &RunningMode , NULL};
Adafruit_GFX_Button Team_Squad_1[11];
Adafruit_GFX_Button Team_Squad_2[11];
Adafruit_GFX_Button *Teamsbuttons[] = { &Team1, &Team2 , NULL};
Adafruit_GFX_Button *Team_Squad_1_buttons[] = { &*Team_Squad_1 , NULL};
Adafruit_GFX_Button *Team_Squad_2_buttons[] = { &*Team_Squad_1 , NULL};

bool Mode;
bool DataRestoredFromEEPROM = 0;
const int EEPROM_MIN_ADDR = 0;
const int EEPROM_MAX_ADDR = 511;

int pixel_x, pixel_y;     //Touch_getXY() updates global vars

#define BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

void setup(void)
{
    Serial.begin(115200);
    delay(1000);
    //Serial.setTimeout(90);
    uint16_t ID = tft.readID();
    if (ID == 0xD3D3) ID = 0x9486; // write-only shield
    tft.begin(ID);
    tft.setRotation(0);            //PORTRAIT
    tft.fillScreen(BLACK);
    Mode = SelectMode();
}


void loop(void)
{
    if(Serial.available() > 0) {
      String IncomingReading = Serial.readString() ;
      // Setup Mode 
       if ( Mode == 0 ){
        // Team Setup
          if (getValue( IncomingReading , ',' , 0 ) == "ST" ) {
            byte str_len_Team1 = getValue(IncomingReading , ',' , 1 ).length() + 1; 
            byte str_len_Team2 = getValue(IncomingReading , ',' , 2 ).length() + 1; 
            // Prepare the character array (the buffer) 
            char Team_1[str_len_Team1];
            char Team_2[str_len_Team2];
            // Copy it over 
            getValue(IncomingReading , ',' , 1 ).toCharArray(Team_1, str_len_Team1);
            getValue(IncomingReading , ',' , 2 ).toCharArray(Team_2, str_len_Team2); 
            // Save To EEPROM
            EEPROM.write(0 , str_len_Team1);  // Team 1 # of letters
            EEPROM.write(1 , str_len_Team2);  // Team 2 # of letters
            EEPROM.write(2 , str_len_Team1 + str_len_Team2 + 3); // End Address of Teams
            eeprom_write_string(4 , Team_1);
            eeprom_write_string(str_len_Team1 + 4 , Team_2);
            Serial.println("Done");
          }
        // Squad Setup
          else if (getValue(IncomingReading , ',' , 0 ) == "SS" ) {
            byte TeamsEndAddress = EEPROM.read(2) + 1;
            for(int i = 0 ; i < 22 ; i++ ){
                EEPROM.write(TeamsEndAddress + i ,  getValue(IncomingReading , ',' , i + 1 ).toInt());
            }
          }
       }
     }
     if ( Mode == 1   && ! DataRestoredFromEEPROM) {
//       SetupMode.drawButton(false);
//       RunningMode.drawButton(false);
//       update_button_list(buttons);
       tft.fillScreen(BLACK);
       tft.setTextColor(WHITE);
       tft.setCursor(50, 30);
       tft.setTextSize(3);
       tft.println(F("Choose teams "));
       byte str_len_Team1 = EEPROM.read(0);
       byte str_len_Team2 = EEPROM.read(1);
       byte TeamsEndAddress = EEPROM.read(2) + 1;
       char Team_1[str_len_Team1];
       char Team_2[str_len_Team2];
       byte Team_1_Squad[11];
       byte Team_2_Squad[11];
       eeprom_read_string(4 , Team_1 , str_len_Team1 );
       eeprom_read_string(4 + str_len_Team1 , Team_2 , str_len_Team2 - 2 );
       for(int i = 0 ; i < 11 ; i++ ){
          Team_1_Squad[i] = EEPROM.read(TeamsEndAddress + i);
       }
       for(int i = 0 ; i < 11 ; i++ ){
          Team_2_Squad[i] = EEPROM.read(TeamsEndAddress + 11 + i);
       }
       Team1.initButton(&tft,  160, 200, 150, 70, WHITE, CYAN, BLACK, Team_1, 3);
       Team2.initButton(&tft, 160, 300, 150, 70, WHITE, CYAN, BLACK,  Team_2, 3);
       Team1.drawButton(false);
       Team2.drawButton(false);
       while( ! Team1.justPressed() && ! Team2.justPressed() ) {
         update_button_list(Teamsbuttons);
        if (Team1.justPressed()) {
          tft.fillScreen(BLACK);
          tft.setTextColor(WHITE);
          tft.setCursor(50, 30);
          tft.setTextSize(3);
          tft.println(F("Select player "));
          int Spacer = 0;
          for(int i = 0 ; i < 11 ; i++) {
            char PlayerNumber[2];
            sprintf(PlayerNumber ,"%d",Team_1_Squad[i]);
            Team_Squad_1[i].initButton(&tft,  160, 80 + Spacer, 80, 30, WHITE, CYAN, BLACK, PlayerNumber , 2);
            Team_Squad_1[i].drawButton(false);
            Spacer += 37;
            update_button_list(Team_Squad_1_buttons);
          }
      }
        if (Team2.justPressed()) {
          tft.fillScreen(BLACK);
          tft.setTextColor(WHITE);
          tft.setCursor(50, 30);
          tft.setTextSize(3);
          tft.println(F("Select player "));
          int Spacer = 0;
          for(int i = 0 ; i < 11 ; i++) {
            char PlayerNumber[2];
            sprintf(PlayerNumber ,"%d",Team_2_Squad[i]);
            Team_Squad_2[i].initButton(&tft,  160, 80 + Spacer, 80, 30, WHITE, CYAN, BLACK, PlayerNumber , 2);
            Team_Squad_2[i].drawButton(false);
            Spacer += 37;
            update_button_list(Team_Squad_2_buttons);
          }
        }   
       }
        DataRestoredFromEEPROM = 1;
  }
}
bool Touch_getXY(void)
{
    TSPoint p = ts.getPoint();
    pinMode(YP, OUTPUT);      //restore shared pins
    pinMode(XM, OUTPUT);
    digitalWrite(YP, HIGH);   //because TFT control pins
    digitalWrite(XM, HIGH);
    bool pressed = (p.z > MINPRESSURE && p.z < MAXPRESSURE);
    if (pressed) {
        pixel_x = map(p.x, TS_LEFT, TS_RT, 0, tft.width()); //.kbv makes sense to me
        pixel_y = map(p.y, TS_TOP, TS_BOT, 0, tft.height());
    }
    return pressed;
}

bool update_button(Adafruit_GFX_Button *b, bool down)
{
    b->press(down && b->contains(pixel_x, pixel_y));
    if (b->justReleased())
        b->drawButton(false);
    if (b->justPressed())
        b->drawButton(true);
    return down;
}

bool update_button_list(Adafruit_GFX_Button **pb)
{
    bool down = Touch_getXY();
    for (int i = 0 ; pb[i] != NULL; i++) {
        update_button(pb[i], down);
    }
    return down;
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

bool SelectMode() {
  tft.setCursor(30, 30);
  tft.setTextSize(2.5);
  tft.println(F("Choose operation mode "));
  bool OperationMode;
  SetupMode.initButton(&tft,  160, 200, 150, 70, WHITE, CYAN, BLACK, "Setup", 4);
  RunningMode.initButton(&tft, 160, 300, 150, 70, WHITE, CYAN, BLACK, "Match", 4);
  SetupMode.drawButton(false);
  RunningMode.drawButton(false);
  update_button_list(buttons);
  while( ! SetupMode.justPressed() && ! RunningMode.justPressed() ) {
    update_button_list(buttons);
    if (SetupMode.justPressed()) {
        OperationMode = 0;
    }
    if (RunningMode.justPressed()) {
         OperationMode = 1;
    }
  }
  return OperationMode;
}


boolean eeprom_is_addr_ok(int addr) {
  return ((addr >= EEPROM_MIN_ADDR) && (addr <= EEPROM_MAX_ADDR));
}


boolean eeprom_write_bytes(int startAddr, const byte* array, int numBytes) {
  // counter
  int i;
  // both first byte and last byte addresses must fall within
  // the allowed range 
  if (!eeprom_is_addr_ok(startAddr) || !eeprom_is_addr_ok(startAddr + numBytes)) {
    return false;
  }
  for (i = 0; i < numBytes; i++) {
    EEPROM.write(startAddr + i, array[i]);
  }
  return true;
}


boolean eeprom_write_string(int addr, const char* string) {
  int numBytes; // actual number of bytes to be written
  //write the string contents plus the string terminator byte (0x00)
  numBytes = strlen(string) + 1;
  return eeprom_write_bytes(addr, (const byte*)string, numBytes);
}

boolean eeprom_read_string(int addr, char* buffer, int bufSize) {
  byte ch; // byte read from eeprom
  int bytesRead; // number of bytes read so far
  if (!eeprom_is_addr_ok(addr)) { // check start address
    return false;
  }

  if (bufSize == 0) { // how can we store bytes in an empty buffer ?
    return false;
  }
  // is there is room for the string terminator only, no reason to go further
  if (bufSize == 1) {
    buffer[0] = 0;
    return true;
  }
  bytesRead = 0; // initialize byte counter
  ch = EEPROM.read(addr + bytesRead); // read next byte from eeprom
  buffer[bytesRead] = ch; // store it into the user buffer
  bytesRead++; // increment byte counter
  
  while ( (ch != 0x00) && (bytesRead < bufSize) && ((addr + bytesRead) <= EEPROM_MAX_ADDR) ) {
  // if no stop condition is met, read the next byte from eeprom
    ch = EEPROM.read(addr + bytesRead);
    buffer[bytesRead] = ch; // store it into the user buffer
    bytesRead++; // increment byte counter
  }
  // make sure the user buffer has a string terminator, (0x00) as its last byte
  if ((ch != 0x00) && (bytesRead >= 1)) {
    buffer[bytesRead - 1] = 0;
  }
  return true;
}

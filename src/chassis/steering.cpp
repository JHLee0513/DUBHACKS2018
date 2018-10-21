#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <termios.h>
#include <time.h>
#include <JHPWMPCA9685.h>
#include <common_functs.h>

#define SERVO_MIN 120
#define SERVO_MAX 720

int servoMin = 120 ;
int servoMax = 720 ;
//map(0,0,180,servoMin, servoMax)

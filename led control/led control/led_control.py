import RPi.GPIO as GPIO
import time
import Switch
import os
import LED


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

redLED = LED.LED_Class(20)
greenLED = LED.LED_Class(21)
brightGreenLED = LED.LED_Class(19)
blueLED = LED.LED_Class(13)
commonLED = LED.LED_Class(16)
switch1 = Switch.SwitchClass(26)
switchOff = bool
check = bool

def blinkLoop(speed):
    redLED.switch_On_LED(), greenLED.switch_On_LED()
    time.sleep(speed)

    if (GPIO.input(26) == False):
        return True

    redLED.switch_Off_LED(), greenLED.switch_Off_LED()

    if (GPIO.input(26) == False):
        return True

    time.sleep(speed)

    if (GPIO.input(26) == False):
        return True

def greenLight():
    commonLED.switch_On_LED()
    blueLED.switch_Off_LED()
    brightGreenLED.switch_On_LED()

def blueLight():
    commonLED.switch_On_LED()
    brightGreenLED.switch_Off_LED()
    blueLED.switch_On_LED()

def switchOffAllLED():
    redLED.switch_Off_LED(), greenLED.switch_Off_LED(), commonLED.switch_Off_LED(), brightGreenLED.switch_Off_LED(), blueLED.switch_Off_LED()

def my_callback(channel):
    if (GPIO.input(26)):
        print 'Rising edge'
    else:
        print 'Falling edge'

def checkHold():
    if (switch1.readPin()==True):
        time.sleep(0.3)
        if (GPIO.input(26) == False):
            return True
        else:
            return False
    else:
        return False


while True:
        if (checkHold() == True):
            if (check == True):
                continue

            else:
                time.sleep(0.5)
                redLED.switch_On_LED() , greenLED.switch_On_LED()
                time.sleep(1)

            if (checkHold()==True):
                switchOffAllLED()
                check = True
                continue

            else:

                try:
                    GPIO.wait_for_edge(26, GPIO.RISING)

                    while True:
                        greenLight()
                        buttonCheck = blinkLoop(0.1)

                        if (buttonCheck):
                            buttonCheck = False

                            while True:
                                blueLight()
                                buttonCheck = blinkLoop(0.3)
                                if (buttonCheck):
                                    time.sleep(0.2)

                                    if (GPIO.input(26) == False):
                                        switchOffAllLED()
                                        time.sleep(1)
                                        switchOff = True
                                        break

                                    else:
                                        switchOff = False
                                        break

                            if (switchOff):
                                break

                except KeyboardInterrupt:
                    GPIO.cleanup()

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')




import time
import serial

#this script need a serial translator sketch to be uploaded to the arduino board. the sketch is a cpp file that is included in the repository. -ABQ

#this establishes a serial connection to the arduino uno board. COM3 is the port that the arduino is connected to. 9600 is the baud rate -ABQ
arduino = serial.Serial("COM3", 9600)

#this sets the timespan bewtween each blink of the built-in L led on the arduino board. -ABQ
BLINK_INTERVAL_IN_SECONDS = 1

#this is a loop that sends the arduino a "H" to turn the LED on and then sends an "L" to turn the LED off. The loop will continue until the user presses ctrl+c, finishing the program runtime in the terminal -ABQ
try:
    while True:
        arduino.write(b"H")
        time.sleep(BLINK_INTERVAL_IN_SECONDS)
        arduino.write(b"L")
        time.sleep(BLINK_INTERVAL_IN_SECONDS)

#this is a catch for the KeyboardInterrupt exception that is raised when the user presses ctrl+c, it closes the program and makes the led stop blinking -ABQ
except KeyboardInterrupt:
    arduino.write(b"LOW") #this line guarantees that the LED is off when the program is terminated. -ABQ
    arduino.close()
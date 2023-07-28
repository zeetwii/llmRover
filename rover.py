import pi_servo_hat # needed for servo control
import sys
import math
import qwiic_scmd # needed for motor control
import RPi.GPIO as GPIO # needed to controller smoke machine
import time

class Rover:

    def __init__(self):
        
        # Smoke Machine
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT) # Smoke Machine Trigger
        GPIO.setup(21, GPIO.OUT) # Air Pump Trigger
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)

        # Motor stuff
        self.myMotor = qwiic_scmd.QwiicScmd()
        self.R_MTR = 0
        self.L_MTR = 1
        self.FWD = 1
        self.BWD = 0
        self.myMotor.begin()
        time.sleep(.250) # Zero Motor Speeds
        self.myMotor.set_drive(0,0,0)
        self.myMotor.set_drive(1,0,0)
        self.myMotor.enable()

        # Servo stuff
        self.servo = pi_servo_hat.PiServoHat()
        self.servo.restart()
        self.servo.move_servo_position(0, 90, 180)

        # Check that tells if the rover is busy
        self.busy = False

    def parseCommand(self, commandType, commandString):

        if commandType == 'drive': # movement command
            print("do something")

    def reset(self):
        
        self.servo.move_servo_position(0, 90, 180) # face camera forward
        GPIO.output(20, GPIO.LOW) # turn off smoke machine
        GPIO.output(21, GPIO.LOW) # turn off air pump
        self.myMotor.set_drive(0,0,0)
        self.myMotor.set_drive(1,0,0)
        self.busy = False

    def setCameraAngle(self, angle):

        if angle > 180:
            angle = 180
        elif angle < 0:
            angle = 0

        self.servo.move_servo_position(0, math.floor(angle), 180)

    def adjustCameraAngle(self, angle):

        currentAngle = self.get_servo_position(0, 180)
        newAngle = currentAngle + angle

        if newAngle > 180: 
            newAngle = 180
        elif newAngle < 0:
            newAngle = 0

        self.servo.move_servo_position(0, math.floor(newAngle), 180)



    
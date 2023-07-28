import pi_servo_hat # needed for servo control
import sys
import math
import qwiic_scmd # needed for motor control
import RPi.GPIO as GPIO # needed to controller smoke machine
import time
import socket

class Rover:

    def __init__(self):

        # UDP Socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind(('0.0.0.0', 7331))
        
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
        self.FWD = 0
        self.BWD = 1
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
            self.busy = True

            for line in str(commandString).splitlines():
                command = line.split(',')

                if len(command) >= 3:

                    if command[0] == 'Forward':
                        self.myMotor.set_drive(self.R_MTR, self.FWD, 255)
                        self.myMotor.set_drive(self.L_MTR, self.FWD, 255)
                        
                        sleepTime = command[2].split()[0]

                        time.sleep(float(sleepTime))
                        self.myMotor.set_drive(self.R_MTR, self.FWD, 0)
                        self.myMotor.set_drive(self.L_MTR, self.FWD, 0)
                            
                    elif command[0] == 'Reverse':
                        self.myMotor.set_drive(self.R_MTR, self.BWD, 255)
                        self.myMotor.set_drive(self.L_MTR, self.BWD, 255)
                        
                        sleepTime = command[2].split()[0]

                        time.sleep(float(sleepTime))
                        self.myMotor.set_drive(self.R_MTR, self.FWD, 0)
                        self.myMotor.set_drive(self.L_MTR, self.FWD, 0)

                    
                    elif command[0] == 'Turn':

                        angle = command[1].split()[0]

                        runTime =  (abs(float(angle)) / 180) * 2.0
                        print(str(runTime))

                        if angle > 0: # Turn Right
                            self.myMotor.set_drive(self.R_MTR, self.BWD, 255)
                            self.myMotor.set_drive(self.L_MTR, self.FWD, 255)
                        else: # Turn Left
                            self.myMotor.set_drive(self.R_MTR, self.FWD, 255)
                            self.myMotor.set_drive(self.L_MTR, self.BWD, 255)
                        
                        time.sleep(runTime)
                        self.myMotor.set_drive(self.R_MTR, self.FWD, 0)
                        self.myMotor.set_drive(self.L_MTR, self.FWD, 0)

            self.busy = False


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

    def socketListener(self):

        while True:
            data, addr = self.serverSocket.recvfrom(1024)

            reply = data.decode()

            msg = ""

            for line in str(reply).splitlines():
                    data = line.split(']')[0]
                    msg = msg + data[1:] + '\n'
            #print(msg) 

            self.parseCommand('drive', msg)


if __name__ == "__main__":

    print("starting rover")

    rover = Rover()
    rover.socketListener()
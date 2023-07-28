# Python script to control a helper bot that will generate example traffic on the twitch channel

import time # needed to keep track of time between posts
import random # needed to randomize messages
from threading import Thread # needed for multithreading

class OtterBot:
    """
    A Class to handle generating custom chat messages
    """

    def __init__(self):
        """
        Initialization method
        """
        self.lastTransmissionTime = time.time()

    def generateMessage(self):

        commandType = random.randint(0, 1) # choice between movement and camera command

        if commandType == 0: # do a movement command
            
            msg = "!drive " # beginning of a drive command

            messageLength = random.randint(1, 4) # how many commands are within the message

            for i in range(messageLength): 
                
                movementType = random.randint(1,4) 

                if movementType == 1: # Go Forward
                    moveTime = random.randint(5, 15)
                    msg = msg + f"Go Forward for {str(moveTime)} seconds.  "
                
                elif movementType == 2: # Turn Left
                    angle = random.randint(0, 180)
                    direction = random.randint(0, 1)
                    moveTime = random.randint(5, 15)

                    if direction == 0:
                        msg = msg + f"Turn Left {str(angle)} degrees and move forward {str(moveTime)} seconds.  "
                    else:
                        msg = msg + f"Turn Left {str(angle)} degrees and move in reverse {str(moveTime)} seconds.  "

                elif movementType == 3: # Turn Right
                    angle = random.randint(0, 180)
                    direction = random.randint(0, 1)
                    moveTime = random.randint(5, 15)

                    if direction == 0:
                        msg = msg + f"Turn Right {str(angle)} degrees and move forward {str(moveTime)} seconds.  "
                    else:
                        msg = msg + f"Turn Right {str(angle)} degrees and move in reverse {str(moveTime)} seconds.  "

                else: # Reverse
                    moveTime = random.randint(5, 15)
                    msg = msg + f"Reverse and travel for {str(moveTime)} seconds.  "

        else:
            print("test")
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

        commandType = random.randint(0, 100) # choice between movement and camera command

        if commandType <= 90: # do a movement command
            
            msg = "!move " # beginning of a move command

            messageLength = random.randint(1, 4) # how many commands are within the message

            for i in range(messageLength): 
                
                movementType = random.randint(1,100) 

                if movementType <= 25: # Go Forward
                    moveTime = random.randint(5, 15)
                    msg = msg + f"Go Forward for {str(moveTime)} seconds.  "
                
                elif movementType <= 50: # Turn Left
                    angle = random.randint(0, 180)
                    direction = random.randint(0, 1)
                    moveTime = random.randint(5, 15)

                    if direction == 0:
                        msg = msg + f"Turn Left {str(angle)} degrees and move forward {str(moveTime)} seconds.  "
                    else:
                        msg = msg + f"Turn Left {str(angle)} degrees and move in reverse {str(moveTime)} seconds.  "

                elif movementType <= 75: # Turn Right
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

        
        else: # do a camera command
            msg = "!look " # beginning of a look command

            cameraChoice = random.randint(0, 100)

            if cameraChoice <= 80: # set angle
                cameraAngle = random.randint(0, 180)
                msg = msg + f"Set camera angle to {str(cameraAngle)}"
            else:
                cameraAngle = random.randint(0, 180)
                cameraDirection = ""
                if random.randint(0,1) == 0: # set the adjustment to be to the right of the current angle
                    cameraDirection = "right"
                else:
                    cameraDirection = "left"
                msg = msg + f"Adjust camera angle by {str(cameraAngle)} to the {cameraDirection}"
        
        return msg
    



if __name__ == "__main__":

    print("Starting OtterBot")

    otter = OtterBot()

    while True:
        print(otter.generateMessage())

        time.sleep(1)
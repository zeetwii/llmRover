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

        messageLength = random.randint(1, 4) # how many commands are within the message

        msg = ""

        for i in range(messageLength): 

            commandType = random.randint(0, 1) # choice between movement and camera command

            if commandType == 0: # do a movement command
                print("do something")
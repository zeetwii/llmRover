# Chatbot Take the Wheel


## Introduction

Welcome to the development repo for the DEFCON31 workshop ***Chatbot Take The Wheel***, developed in support of the [AI Village](https://aivillage.org/).  This workshop is designed to teach the good, bad, and ugly of using LLMs to control and direct physical systems.  For this workshop, you the player will take control of a small rover using twitch chat and ChatGPT.  Everything you type in the [twitch channel](https://www.twitch.tv/defensedigitalrover) will be processed by ChatGPT and turned into commands for the rover to follow.  This means rather than pushing forward on a joystick, simply type *!move Go Forward for five seconds* and the rover will obey.  You can even chain commands together.  For example, typing *!move turn right 45 degrees, then go forward 3 seconds, then turn left and reverse for 10 seconds* will have the rover turn 45 degrees relative to its current position, move forward for three seconds, turn 90 degrees to the left and then reverse for ten seconds.  

## Background

Large Language Models (LLMs) have taken the world by storm due to their ability to rapidly and easily parse and translate human languages.  This has made them ideal for acting as an interface between humans and other systems, whether that be an image generator, text document, or robots.  One of the main areas of research with LLMs currently is pairing them with Computer Vision systems to control physical robots.  [PaLM-E](https://palm-e.github.io/) is great example of this, where multiple systems combine to allow a human to easily command a robot without the need of complicated controllers.  

However, using an LLM with your robot isn't quite as simple as just adding an OpenAI API key to your system.  LLMs are naturally very flexible in how and what data they process, meaning that adding them to a system also adds the vulnerabilities associated with LLMs to the system, mainly hallucinations and prompt injections.  That's what spawned the desire to make this workshop as a way to show what happens when you do not account for those vulnerabilities in your system.  

## Game Play

All of the game play for the workshop takes place on our Twitch channel [Defense Digital Rover](https://www.twitch.tv/defensedigitalrover).  Players take control of the rover by issuing commands via the channels stream chat.  All commands are prefaced by the ***!*** symbol.  The full list of commands are:

- !move
  - This command tells the rover to parse whatever you say after it as movement instructions.  You can tell it to move forwards, backwards, and turn, as well as chain multiple instructions together.  An example use would be *!move Go Forward 5 seconds* 
- !look
  - This command tells the rover to parse whatever you say after it as instructions on where to point the camera.  The camera can pan 180 degrees, and you can either set it to a specific angle or one relative to its current facing.  An example command would be *!look set camera to 90 degrees* which will set the camera to be facing straight ahead regardless of its current position.   
- !music 
  - This command will change the background music...whenever I add it.  
- !help
  - This command will give you a link to this page.  

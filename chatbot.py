# Code for running the chatbot controller for the defcon31 rover

from twitchio.ext import commands # needed for twitchIO chatbot
import openai # needed for ChatGPT API
import threading # needed for threading
import yaml # needed for config
import socket # needed for udp



class ChatBot(commands.Bot):

    def __init__(self, accessToken, prefix, channelList, openAIkey, driveContext):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...

        self.roverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.roverAddress = ('rover.local', 7331)

        openai.api_key = openAIkey
        self.driveContext = driveContext

        super().__init__(token=accessToken, prefix=prefix, initial_channels=channelList)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

        

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        # print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    # Hello command, kept in for the lulz
    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

    # Drive command, used to tell the rover where to go
    @commands.command()
    async def drive(self, ctx: commands.Context):

        #print(ctx.message.content[6:]) # cut off the command part of the message
        userMessage = ctx.message.content[6:] # cut off the command part of the message

        # if user message not empty
        if len(userMessage) > 0:
            # Chat GPT stuff
            messages = [ {"role": "system", "content": self.driveContext} ]
            messages.append({"role": "user", "content": userMessage},)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = chat.choices[0].message.content
            
            print(f"ChatGPT: {reply}")  

            self.roverSocket.sendto(str.encode(reply), self.roverAddress)

            await ctx.send(f'ChatGPT: {reply}')

    # Camera command, used to pan the camera
    @commands.command()
    async def pan(self, ctx: commands.Context):
    
        await ctx.send(f'camera commands to be added')

    # Audio command, used to control background audio
    @commands.command()
    async def audio(self, ctx: commands.Context):
        
        await ctx.send(f'audio command to be added')

    # Filter command, used to change the camera filter
    @commands.command()
    async def filter(self, ctx: commands.Context):
        
        await ctx.send(f'filter command to be added')

    # Filter command, used to change the camera filter
    @commands.command()
    async def help(self, ctx: commands.Context):
        
        await ctx.send(f'help command to be added')

if __name__ == "__main__":

    CFG = None  # global CFG settings
    with open("./configs/config.yml", "r") as ymlfile:
        CFG = yaml.safe_load(ymlfile)

    twitch_initial_channels = CFG["twitch"]["CHANNEL"]
    twitch_prefix = initial_channels = CFG["twitch"]["BOT_PREFIX"]
    twitch_access_token = CFG["twitch"]["ACCESS_TOKEN"]

    openai_key = CFG["openai"]["API_KEY"]
    openai_context = CFG["openai"]["CONTEXT"]

    chatbot = ChatBot(twitch_access_token, twitch_prefix, twitch_initial_channels, openai_key, openai_context)
    chatbot.run()

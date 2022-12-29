import discord, os
from discord import Bot as BotBase
from json import load

with open('utils/configs.json', "r", encoding="utf-8") as f:
    configData = load(f)

class client(BotBase):
    
    def __init__(self):
        
        self.token = configData["token"]
        
        super().__init__(
            command_prefix = configData["prefix"],
            intents = discord.Intents.all(),
            case_insensitive = True,
            help_command = None
        )
        
    def loadcogs(self):
        for commands in os.listdir("./commands"):
            if commands.endswith(".py") and not commands.startswith("__"):
                self.load_extension('commands.{}'.format(commands[:-3]))
        
        for events in os.listdir("./events"):
            if events.endswith(".py") and not events.startswith("__"):

                self.load_extension('events.{}'.format(events[:-3]))
        
    def __run__(self):
        
        self.loadcogs()
        
        self.run(self.token)
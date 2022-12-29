import discord, custom
from discord.ext import commands
from datetime import datetime
from pytz import timezone

class events(commands.Cog):
    
    def __init__(self, bot:commands.Bot):
        
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        
        print(f"Eu entrei como {self.bot.user.name}")
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        
        if interaction.is_component:
            if interaction.to_dict()['data']['custom_id'] == "Modal":return
            if interaction.to_dict()['data']['component_type'] == 3: return
            func =  getattr(custom, f'{interaction.custom_id}')
            await func(self.bot, interaction)
            
def setup(bot:commands.Bot):
    bot.add_cog(events(bot))
import discord, custom
from discord.ext import commands
from datetime import datetime
from pytz import timezone
from utils.verify import *

class events(commands.Cog):
    
    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        
        await self.bot.change_presence(status = discord.Status.idle)
        
        print(f"Eu entrei como {self.bot.user.name}")
        
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        await verfyadv(self.bot,member)

        await verfypoints(self.bot,member)

    @commands.Cog.listener()
    async def on_member_ban(self, guild:discord.Guild, member:discord.User):

        if adv.count_documents({ "_id": member.id}) == 1:
            adv.find_one_and_delete({"_id": member.id})

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user: return

        elif message.author.bot: return

        elif message.mention_everyone: return

        if 'ticket-' in message.channel.name:

            with open(f'./tickets/{message.channel.name}.txt', 'a') as f:

                f.write(f'\n{message.author.name}: {message.content}')
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        
        if interaction.is_component:
            if interaction.to_dict()['data']['custom_id'] == "Modal":return
            if interaction.to_dict()['data']['component_type'] == 3: return
            func =  getattr(custom, f'{interaction.custom_id}')
            await func(self.bot, interaction)
            
def setup(bot:commands.Bot):
    bot.add_cog(events(bot))
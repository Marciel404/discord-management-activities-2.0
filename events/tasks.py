import discord

from pytz import timezone
from datetime import datetime
from discord.ext import commands, tasks
from utils.loader import configData

class tasks(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @tasks.loop(minutes = 1)
    async def times(self):

        guild = self.bot.get_guild(configData['guild'])

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        x = data_e_hora_atuais.astimezone(fuso_horario)

        if x.weekday() == 4:

            channel = self.bot.get_channel(configData['chats']['sugestsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            nvl10 = discord.utils.get(guild.roles, id = configData['roles']['niveis']['nvl10'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                nvl10: discord.PermissionOverwrite(send_messages = True, attach_files = True),

                verifi: discord.PermissionOverwrite(send_messages=False),

                mod: discord.PermissionOverwrite(send_messages=True),

                naoverifi: discord.PermissionOverwrite(read_messages=False),

            }

            if channel.overwrites != overwrites:

                await channel.edit(overwrites = overwrites)

                await channel.send(f'Chat aberto!!!\nVenha indicar algo para os outros membros😃')

        else:

            channel = self.bot.get_channel(configData['chats']['sugestsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            nvl10 = discord.utils.get(guild.roles, id = configData['roles']['niveis']['nvl10'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                nvl10: discord.PermissionOverwrite(send_messages = False, attach_files = True),

                verifi: discord.PermissionOverwrite(send_messages=False),

                naoverifi: discord.PermissionOverwrite(read_messages=False),

                mod: discord.PermissionOverwrite(send_messages=True),

            }

            if channel.overwrites != overwrites:

                await channel.edit(overwrites = overwrites)

                await channel.send(f'E o chat está fechado novamente galera, deixando claro que semana que vem ele volta😁')

        if x.weekday() == 0:

            channel = self.bot.get_channel(configData['chats']['resumsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            nvl10 = discord.utils.get(guild.roles, id = configData['roles']['niveis']['nvl10'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                nvl10: discord.PermissionOverwrite(send_messages = True, attach_files = True),

                verifi: discord.PermissionOverwrite(send_messages = False),

                mod: discord.PermissionOverwrite(send_messages = True),

                naoverifi: discord.PermissionOverwrite(read_messages = False),

            }

            if channel.overwrites != overwrites:

                await channel.edit(overwrites = overwrites)

                await channel.send(f'Chat aberto!!!\nVem contar algo sobre o que rolou na sua semana 😃\n||{verifi.mention}||')

        else:

            channel = self.bot.get_channel(configData['chats']['resumsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            nvl10 = discord.utils.get(guild.roles, id = configData['roles']['niveis']['nvl10'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                nvl10: discord.PermissionOverwrite(send_messages = False, attach_files = True),

                verifi: discord.PermissionOverwrite(send_messages=False),

                naoverifi: discord.PermissionOverwrite(read_messages=False),

                mod: discord.PermissionOverwrite(send_messages=True),

            }

            if channel.overwrites != overwrites:

                await channel.edit(overwrites = overwrites)

                await channel.send(f'E o chat está fechado novamente galera, deixando claro que semana que vem ele volta😁')

def setup(bot:commands.Bot):
    bot.add_cog(tasks(bot))
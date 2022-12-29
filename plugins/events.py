import discord

from discord.ext import commands
from discord import slash_command
from utils.configs import configData
from datetime import datetime
from pytz import timezone
from utils.verify import verfyadv, verfypoints
from db.mod import adv

class events(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot
        
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        
        print(interaction.custom_id)

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
    async def on_message_edit(self, antes:discord.Message, depois: discord.Message):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        if antes.author.bot:

            return
        
        if antes.embeds:

            return
        
        if antes.components:

            return

        if antes.content == depois.content:

            return

        channel = self.bot.get_channel(configData['logs']['chat'])

        e = discord.Embed(

            description = f'Mensagem enviada por {antes.author.mention} foi editada em {antes.channel.mention}',

            color = 0xfff000

        )
        e.add_field(name = 'Antiga:', value = f'{antes.content}', inline=False)

        e.add_field(name = 'Nova:', value =  f'{depois.content}', inline=False)

        e.set_author(name = f'{antes.author.name}#{antes.author.discriminator}', icon_url = antes.author.display_avatar)

        e.set_footer(text = f'生 HAYLENG 死 às {dt}')

        await channel.send(embed = e)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):

        if message.components:

            return

        if message.author == self.bot:

            return

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        channel = self.bot.get_channel(configData['logs']['chat'])

        if message.embeds:

            return

        e = discord.Embed(

            description = f'Mensagem enviada por {message.author.mention} foi deletada em {message.channel.mention}',

            color = 0xff0000

        )
        e.add_field(name = 'Mensagem:', value = f'{message.content}', inline=False)

        e.set_author(name = f'{message.author.name}#{message.author.discriminator}', icon_url = message.author.display_avatar)

        e.set_footer(text = f'生 HAYLENG 死 às {dt}')

        await channel.send(embed = e)

    @commands.Cog.listener()
    async def on_member_update(self, antes:discord.User, depois:discord.User):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        channel = self.bot.get_channel(configData['logs']['membros'])

        if antes.nick != depois.nick:

            e = discord.Embed(

            description = f'{antes.mention} editou o apelido',

            color = 0xfff000
            
        )
            e.add_field(name = 'Apelido antigo:', value = f'{antes.display_name}', inline=False)

            e.add_field(name = 'Apelido novo:', value =  f'{depois.display_name}', inline=False)

            e.set_author(name = f'{antes.name}#{antes.discriminator}', icon_url = antes.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        if antes.roles != depois.roles:

            if discord.utils.get(antes.guild.roles, id = configData['roles']['outras']['verificado']) in depois.roles:

                await depois.remove_roles(discord.utils.get(antes.guild.roles, id = configData['roles']['outras']['naoverificado']))

    @commands.Cog.listener()
    async def on_user_update(self, antes:discord.User, depois:discord.User):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        channel = self.bot.get_channel(configData['logs']['membros'])

        if antes.name != depois.name:

            e = discord.Embed(

            description = f'{antes.mention} editou o nome',

            color = 0xfff000
        )
            e.add_field(name = 'Nome antigo:', value = f'{antes.name}', inline=False)

            e.add_field(name = 'Nome novo:', value =  f'{depois.name}', inline=False)

            e.set_author(name = f'{antes.name}#{antes.discriminator}', icon_url = antes.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member:discord.Member, before:discord.VoiceState, after:discord.VoiceState):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        channel = self.bot.get_channel(configData['logs']['call'])

        channel2 = self.bot.get_channel(configData['logs']['microfone'])

        if before.channel != after.channel:

            if before.channel == None:

                e = discord.Embed(

                description = f'{member.mention} entrou no chat `{after.channel}`',

                color = 0x00ff19

                )

                e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                e.set_footer(text = f'生 HAYLENG 死 às {dt}')

                await channel.send(embed = e)

                return

            if after.channel == None:

                e = discord.Embed(

                description = f'{member.mention} saiu do chat `{before.channel}`',

                color = 0xff0000

                )

                e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                e.set_footer(text = f'生 HAYLENG 死 às {dt}')

                await channel.send(embed = e)

                return

            e = discord.Embed(

            description = f'{member.mention} se moveu do `{before.channel}` para `{after.channel}`',

            color = 0xfff000

            )
            
            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.self_deaf:

            e = discord.Embed(

            description = f'{member.mention} mutou o fone no `{after.channel}`',

            color = 0xfff000

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)
        
        elif before.self_deaf:

            e = discord.Embed(

            description = f'{member.mention} desmutou o fone no `{after.channel}`',

            color = 0x00ff19

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

        elif before.self_mute:

            e = discord.Embed(

            description = f'{member.mention} desmutou o microfone no `{after.channel}`',

            color = 0x00ff19

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

        elif after.self_mute:

            e = discord.Embed(

            description = f'{member.mention} mutou o microfone no `{after.channel}`',

            color = 0xfff000

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

        elif after.self_video:

            e = discord.Embed(

            description = f'{member.mention} ativou o video no `{after.channel}`',

            color = 0x00ff19

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

        elif before.self_video:

            e = discord.Embed(

            description = f'{member.mention} desativou o video no `{after.channel}`',

            color = 0xfff000

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

        elif after.self_stream:

            e = discord.Embed(

            description = f'{member.mention} começou a transmitir no `{after.channel}`',

            color = 0x00ff19

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)
        
        elif before.self_stream:

            e = discord.Embed(

            description = f'{member.mention} parou de transmitir no `{after.channel}`',

            color = 0xfff000

            )

            e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel2.send(embed = e)

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))
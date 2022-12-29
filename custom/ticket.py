import discord, os
from datetime import datetime
from pytz import timezone
from utils.loader import configData
from classes.buttons import AdonTicket, AdonTicket2, jumpto
from db.mod import *

async def abrirTicket(selfbot, interaction):

    data_e_hora_atuais = datetime.now()

    fuso_horario = timezone('America/Sao_Paulo')

    dt = data_e_hora_atuais.astimezone(fuso_horario)

    Chat = discord.utils.get(interaction.guild.channels, name=f'ticket-{interaction.user.id}')

    if Chat is None:

        guild = interaction.guild

        ticket = f'ticket-{interaction.user.id}'

        member = interaction.user

        admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
        
        mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

        suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

        overwrites = {

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            member: discord.PermissionOverwrite(read_messages=True),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            suporte: discord.PermissionOverwrite(read_messages=True),
        }

        for file in os.listdir('./tickets'):

            if file.endswith('.txt'):

                if file.startswith(f'{ticket}'):

                    os.remove(f"./tickets/{ticket}.txt")

        with open(f'./tickets/{ticket}.txt', 'a') as f:

            f.write(f'Ticket de {interaction.user.name} {dt.strftime("%d/%m/%Y")}')

        channel = await interaction.guild.create_text_channel(name=ticket, 
        overwrites = overwrites, 
        category = discord.utils.get(guild.categories, id = int(interaction.message.embeds[0].footer.text)))

        await interaction.response.send_message('Ticket criado com sucesso',view = discord.ui.View(jumpto(f'https://discordapp.com/channels/{interaction.guild.id}/{channel.id}'), timeout = 180), ephemeral = True)
        
        e = discord.Embed(title = f'Ticket de {interaction.user}', 
                          description = dt.strftime("Aberto as %H:%M de %d/%m/%Y"))
        e.set_footer(text = interaction.user.id)

        await channel.send(content = f'{interaction.user.mention} {suporte.mention}',embed = e,view=AdonTicket())
    
    else:

        await interaction.response.send_message('Ticket já existente, encerre o ultimo para criar outro', ephemeral = True)

async def closeTicket(selfbot, interaction):

    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

        return

    member = interaction.guild.get_member(int(interaction.message.embeds[0].footer.text))

    admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        
    mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

    suporte = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['suporte'])

    overwrites = {

        member: discord.PermissionOverwrite(read_messages=False),

        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),

        admin: discord.PermissionOverwrite(read_messages=True),

        mod: discord.PermissionOverwrite(read_messages=True),

        suporte: discord.PermissionOverwrite(read_messages=True),

    }

    e = discord.Embed(description = f'🔒Ticket de {member} fechado por {interaction.user.mention} \nClique no 🔓 para abrir')
    e.set_footer( text = member.id)

    await interaction.channel.edit(overwrites = overwrites)

    await interaction.message.delete()

    msg = await interaction.channel.send(embed = e, view = AdonTicket2())

async def openTicket(selfBot, interaction):

    member = interaction.guild.get_member(int(interaction.message.embeds[0].footer.text))

    admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        
    mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

    suporte = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['suporte'])

    overwrites = {

        member: discord.PermissionOverwrite(read_messages=True),

        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),

        admin: discord.PermissionOverwrite(read_messages=True),

        mod: discord.PermissionOverwrite(read_messages=True),

        suporte: discord.PermissionOverwrite(read_messages=True),

    }

    await interaction.channel.edit(overwrites = overwrites)

    await interaction.message.delete()
    
    e = discord.Embed(title=f'Ticket de {member} aberto 🔓')
    e.set_footer(text = member.id)

    msg = await interaction.channel.send(embed = e, view = AdonTicket())

async def deleteTicket(selfbot,interaction):

    await interaction.channel.delete()
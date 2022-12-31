import discord

from utils.loader import  configData
from db.mod import ausendb, desausendb
from db.mod import advdb, rmvadvdb
from pytz import timezone
from datetime import datetime
from classes.modals import *
from classes.selectmenus import *

async def ausencia(selfbot, interaction):
        
    dt = datetime.now(timezone('America/Sao_Paulo'))

    def check(m):
        return m.content and m.author.id == interaction.user.id

    try:

        role = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['standby'])

        ausente = selfbot.get_channel(configData['chats']['ausencia'])
        
        await interaction.response.defer()

        if role not in interaction.user.roles:

            await interaction.followup.send('Escreva o motivo de estar ausente', ephemeral=True)

            msg = await selfbot.wait_for('message', check = check, timeout = 130)

            await interaction.user.add_roles(role)

            await ausente.send(f'{interaction.user.name} entrou em ausencia às {dt.strftime("%d/%m/%Y")}\nMotivo: {msg.content}')

            await interaction.followup.send(f'Agora você está ausente {interaction.user.mention}', ephemeral = True)

            await msg.delete()

            await ausendb(interaction.user,msg.content,dt.strftime('%d/%m/%Y'))

            return

        if role in interaction.user.roles:

            await interaction.user.remove_roles(role)

            await ausente.send(f'{interaction.user.name} Saiu da ausencia às {dt}')

            await interaction.response.send_message('Você não está mais ausente', ephemeral = True)

            await desausendb(interaction.user)

            return
    
    except Exception:

        await ausente.send(f'{interaction.user.name} clicou no ausente mas não fez nada')
            
async def banMember(selfbot, interaction):

    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) in interaction.user.roles \
    or interaction.user.guild_permissions.ban_members:
        
        await interaction.response.send_modal(banModal())

        return
    
    await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

async def confirmBan(selfbot, interaction):
    
    if interaction.user.guild_permissions.ban_members \
    or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles\
    or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
        l1 = selfbot.get_channel(configData['logs']['mod'])
        membro = interaction.guild.get_member(int(interaction.message.embeds[0].footer.text))
        author = interaction.message.embeds[0].fields[1].value
        motivo = interaction.message.embeds[0].fields[2].value

        guild = interaction.guild

        E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {membro.name} \nQuem baniu: {author}\nAprovado por: {interaction.user.mention} \nmotivo: {motivo}')
        E.set_footer(text = f'id: {membro.id}')

        await l1.send(embed = E)

        await interaction.message.delete()

        await interaction.response.send_message(f'{membro.name} banido com sucesso', ephemeral = True)

        
        await interaction.guil.ban(
            id = membro.id,
            reason = motivo)
        return
    
    await interaction.response.send_message('Você não tem permissão para isso')

async def deny(selfbot, interaction):
    
    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles\
    or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        await interaction.message.delete();return
    
    await interaction.response.send_message('Você não tem permissão para isso', ephemeral = True)

async def confirmAdcAdv(selfbot, interaction):
    
    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles\
    or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
        member = interaction.guild.get_member(id = int(interaction.message.embeds[0].footer.text))
        motivo = interaction.message.embeds[0].fields[2].value
        role1 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1'])
        role2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv2'])
        role3 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv3'])
        rolemute = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['mute'])
        channel = interaction.guild.get_channel(configData['logs']['mod'])

        if role3 in membro.roles:

            E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {membro.name} \n Quem baniu: {interaction.user.mention} \n motivo: Acumulo de adv')

            await channel.send(embed = E)

            await membro.ban(reason = 'Acumulo de advertencia')

            await interaction.message.delete()

            await interaction.response.send_message(f'{membro.name} advertido com sucesso e banido devido o acumulo de adv', ephemeral = True)

        if role2 in membro.roles:

            e = discord.Embed(title = 'Advertencia 3', description = f'{membro.mention} foi advertido por {ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{motivo}')
            
            await advdb(membro.id,3,f'{motivo} {dt}')

            await membro.add_roles(role3, reason = motivo)
            await membro.add_roles(rolemute, reason = 'Adv3')

            await interaction.message.delete()

            await channel.send(embed = e)

            await asyncio.sleep(86400)

            await membro.remove_roles(rolemute)

            return

        if role1 in membro.roles:

            e = discord.Embed(title = 'Advertencia 2', description = f'{membro.mention} foi advertido por {ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{motivo}')
            
            await advdb(membro,2,f'{motivo} {dt}')

            await membro.add_roles(role2, reason = motivo)
            await membro.add_roles(rolemute, reason = 'Adv2')

            await interaction.message.delete()

            await channel.send(embed = e)

            await interaction.response.send_message(f'{membro} advertido com sucesso', ephemeral = True)

            await asyncio.sleep(10800)

            await membro.remove_roles(rolemute)

            return

        if role1 not in membro.roles:

            e = discord.Embed(title = 'Advertencia 1', description = f'{membro.mention} foi advertido por {ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{motivo}')

            await advdb(membro,3,'None')

            await advdb(membro,2,'None')

            await advdb(membro,1,f'{motivo} {dt}')
            
            await membro.add_roles(role1, reason = motivo)

            await membro.add_roles(rolemute, reason = 'Adv1')

            await interaction.message.delete()

            await channel.send(embed = e)

            await interaction.response.send_message(f'{membro} advertido com sucesso', ephemeral = True)

            await asyncio.sleep(3600)

            await membro.remove_roles(rolemute)

            return

        await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)
    
    await interaction.response.send_message('Você não tem permissão para isso')

async def confirmRmvAdv(selfbot, interaction):
    
    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles \
    or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

        await interaction.message.delete()

        member = interaction.guild.get_member(id = int(interaction.message.embeds[0].footer.text))
        motivo = interaction.message.embeds[0].fields[2].value
        role1 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1'])
        role2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv2'])
        role3 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv3'])
        rolemute = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['mute'])
        channel = interaction.guild.get_channel(configData['logs']['mod'])

        e = discord.Embed(title = 'Remoção adv', description = f'{interaction.user.mention} removeu uma advertencia de {membro.mention}')

        if role3 in membro.roles:
            
            await rmvadvdb(membro,3, 'None')
            await membro.remove_roles(role3)
            await channel.send(embed = e)
            await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)
            await membro.remove_roles(mute)
            return

        elif role2 in membro.roles:
            
            await rmvadvdb(membro,2,'None')
            await membro.remove_roles(role2)
            await channel.send(embed = e)
            await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)
            await membro.remove_roles(mute)
            return

        elif role1 in membro.roles:

            await rmvadvdb(membro,1,'None')
            await membro.remove_roles(role1)
            await channel.send(embed = e)
            await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)
            await membro.remove_roles(mute)
            return

        elif discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1']) not in membro.roles:
            await interaction.response.send_message('Esse membro não possue advertencias', delete_after = 3);return
        
    await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

async def advertência(selfbot, interaction):

    if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

        await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

        return

    await interaction.response.send_message('O que ira fazer?', ephemeral = True, view = adcrmvadivertência())

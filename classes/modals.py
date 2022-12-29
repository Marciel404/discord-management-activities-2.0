import discord

from discord.ui import InputText, Modal
from .buttons import *

class banModal(Modal):

    def __init__(self) -> None:

        super().__init__(title = 'Profile', custom_id = "Modal")

        self.add_item(
            InputText(
                label = 'ID',
                placeholder = 'Id do membro a banir',
                required = True
            )
        ),
        self.add_item(
            InputText(
                label = 'Motivo',
                placeholder = 'Motivo de banir o membro',
                required = True
            )
        )
    async def callback(self, interaction: discord.Interaction):
        
        member = interaction.guild.get_member(int(self.children[0].value))
        
        embed = discord.Embed(title = "Ban")
        embed.add_field(name = "Name",value=member.name,inline = False)
        embed.add_field(name = "Author",value=interaction.user,inline = False)
        embed.add_field(name = "Motivo",value=self.children[1].value,inline = False)
        embed.set_footer(text = member.id)
        embed.set_thumbnail(url = member.display_avatar)

        await interaction.response.send_message(embed = embed, view = banbuttons())
        
class adivertenciaAdicionarModal(Modal):

    def __init__(self) -> None:

        super().__init__(title = 'Profile', custom_id = "Modal")

        self.add_item(
            InputText(
                label = 'ID',
                placeholder = 'Id do membro a banir',
                required = True
            )
        ),
        self.add_item(
            InputText(
                label = 'Motivo',
                placeholder = 'Motivo de banir o membro',
                required = True
            )
        )
    async def callback(self, interaction: discord.Interaction):
        
        member = interaction.guild.get_member(int(self.children[0].value))
        
        embed = discord.Embed(title = "Adicionar Advertincia")
        embed.add_field(name = "Name",value=member.name,inline = False)
        embed.add_field(name = "Author",value=interaction.user,inline = False)
        embed.add_field(name = "Motivo",value=self.children[1].value,inline = False)
        embed.set_footer(text = member.id)
        embed.set_thumbnail(url = member.display_avatar)

        await interaction.response.send_message(embed = embed, view = advadcbuttons())

class adivertenciaRemoverModal(Modal):

    def __init__(self) -> None:

        super().__init__(title = 'Profile',custom_id = "Modal")

        self.add_item(
            InputText(
                label = 'ID',
                placeholder = 'Id do membro a banir',
                required = True
            )
        ),
        self.add_item(
            InputText(
                label = 'Motivo',
                placeholder = 'Motivo de banir o membro',
                required = True
            )
        )
    async def callback(self, interaction: discord.Interaction):
        
        member = interaction.guild.get_member(int(self.children[0].value))
        
        embed = discord.Embed(title = "Ban")
        embed.add_field(name = "Name",value=member.name,inline = False)
        embed.add_field(name = "Author",value=interaction.user,inline = False)
        embed.add_field(name = "Motivo",value=self.children[1].value,inline = False)
        embed.set_footer(text = member.id)
        embed.set_thumbnail(url = member.display_avatar)

        await interaction.response.send_message(embed = embed, view = advrmvbuttons())
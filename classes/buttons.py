import discord

class ComandosStaff(discord.ui.View):
    
    @discord.ui.button(label = 'Ausencia', style = discord.ButtonStyle.blurple, custom_id = "ausencia")
    async def ausente():return
    @discord.ui.button(label = 'Ban', style = discord.ButtonStyle.blurple, custom_id = "banMember")
    async def ban():return
    @discord.ui.button(label = 'Advertencia', style = discord.ButtonStyle.blurple, custom_id = "advertência")
    async def advertência():return
    @discord.ui.button(label = 'Cargos', style = discord.ButtonStyle.blurple, custom_id = "adcCargosEquipes")
    async def cargos():return

class BanButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple, custom_id = "confirmBan")
    async def confirmban():return
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple, custom_id = "deny")
    async def deny():return

class AdvAdcButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple, custom_id = "confirmAdcAdv")
    async def confirmadv():return
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple, custom_id = "deny")
    async def denyadm():return

class AdvRmvButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple, custom_id = "confirmRmvAdv")
    async def confirmadv():return
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple, custom_id = "deny")
    async def denyadm():return
    
class Ticket(discord.ui.View):
    
    @discord.ui.button(label = '🛎 Criar ticket', style = discord.ButtonStyle.blurple, custom_id = "abrirTicket")
    async def ticket():return
    
class AdcCapEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple, custom_id = "confirmAdcCap")
    async def confirmadv():return
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple, custom_id = "denyAdcCap")
    async def denyadm():return

class AdcCargoEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple, custom_id = "confirmAdcEquipe")
    async def confirmadv():return
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple, custom_id = "deny")
    async def denyadm():return

class AdonTicket(discord.ui.View):
    
    @discord.ui.button(label = '🔒 Fechar ticket', style = discord.ButtonStyle.blurple, custom_id = "closeTicket")
    async def closeTicket():return

class AdonTicket2(discord.ui.View):
    
    @discord.ui.button(label = '🔓 Abrir ticket', style = discord.ButtonStyle.blurple, custom_id = "openTicket")
    async def openTicket():return
    @discord.ui.button(label = '🛑 Deletar Ticket', style = discord.ButtonStyle.blurple, custom_id = "deleteTicket")
    async def deleteTicket():return

class jumpto(discord.ui.Button):

    def __init__(self, url):

        super().__init__(

            label = 'Atalho para o ticket',

            style=discord.ButtonStyle.url,
        
            url = url
        )
    async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):

        pass
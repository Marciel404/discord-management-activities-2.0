import discord
from discord.ext import commands
from discord import slash_command, option
from classes.buttons import ComandosStaff, Ticket

class commandsMod(commands.Cog):
    
    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @slash_command(name = "buttonsstaff", description = "Envia os botons de staff")
    @option(name = "channel", description = "Escolha o chat para mandar",)
    async def buttonstaff(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        
        if channel == None: channel = interaction.channel
        
        await interaction.response.send_message('Foi', ephemeral = True)
                
        await channel.send("", view = ComandosStaff())
    
    @slash_command(name = "ticketmessage", description = "Envia a mensagem do ticket")
    @option(name = 'channel', description = "Chat para enviar a mensagem")
    @option(name = "category", description = "Categoria para abrir os tickets")
    async def ticketmessage(self, interaction: discord.Interaction, channel: discord.TextChannel = None, category: discord.CategoryChannel = None):
        
        if channel == None: channel = interaction.channel
        if category == None: category = channel.category
        
        e = discord.Embed(title = 'Precisa de ajuda? Reaja a 🛎 para abrir um ticket',
        description = 'Com os tickets você pode reportar algo ou tirar alguma dúvida.',
        color = 0x4B0082)
        e.set_footer(text = 'Staff HYG', icon_url = interaction.guild.icon)
        e.set_image(url = 'https://images-ext-1.discordapp.net/external/t4HSHa7IBshAK98mZcWl1_ud0x51l07Xby2JhQxUJvc/https/media.giphy.com/media/sKezAGnlMZmLnwXwP8/giphy.gif')
        e.set_footer(text = category.id)
        
        await channel.send(embed = e, view = Ticket())
        
        await interaction.response.send_message("Prontinho", ephemeral = True)
        
    discord.slash_command(guild_only = True,name = 'kick', description = 'Expulsa um membro')
    @discord.option(name = 'Membro', description = 'Escolha o membro para expulsar')
    @discord.option(name = 'Motivo', description = 'Escreva o motivo de expulsar')
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx,membro: discord.Member = None,*,motivo=None):

        if motivo == None:

            motivo = 'Motivo não informado'

        e1 = discord.Embed(title = 'kick', description = f'Voce esta prestes a expulsar {membro.mention}')

        if membro == self.bot.user:

            await ctx.response.send_message('Não posso expulsar a mim mesmo')

            return

        elif  membro == ctx.author:

            await ctx.response.send_message('Você não pode expulsar a si mesmo')

            return
        
        elif membro == None:

            await ctx.response.send_message('Você precisa mensionar o membro a banir')

            return

        await ctx.response.send_message(embed = e1, view = kick(self.bot,membro, motivo, ctx.author))

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e expulsou o {membro.name}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'embed', description = 'Envia uma embed em um chat desejado')
    @discord.option(name = 'channel', description = 'Escolha o chat para enviar a embed')
    @discord.option(name = 'title', description = 'Escreva o titulo da embed')
    @discord.option(name = 'link_image', description = 'Escolha a imagem da embed')
    @discord.option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @discord.option(name = 'content', description = 'Escreva o conteudo da embed')
    @discord.option(name = 'color', description = 'Escolha a cor da embed')
    @commands.has_guild_permissions(manage_channels = True)
    async def embed(self, ctx, channel: discord.TextChannel = None, title = None, img = '', mention: discord.Role = None,color = None, *, content = None):

        if channel == None:

            channel = ctx.channel

        if color == None:

            color = hexacolors.string('indigo')

        else:

            try:

                color = hexacolors.string(color)

            except:

                try:

                    color = hexacolors.hexadecimal(color)
                
                except:

                    color = hexacolors.string('indigo')

        if mention != None:

            mention = mention.mention

        e = discord.Embed(title = title, description = content, colour = color)

        e.set_image(url = img)

        e.set_footer(text = f'{ctx.guild.name}', icon_url = ctx.guild.icon)

        channel2 = self.bot.get_channel(channel.id)

        await channel2.send(mention,embed = e)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e enviou uma embed no {channel.mention}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'clear', description = 'Limpa o chat')
    @discord.option(name = 'quantidade',type = int, description = 'Escolha a quantidade de mensagens a limpar')
    @commands.has_permissions(manage_channels = True)
    async def clear(self, ctx, quantidade: int = 0):

        if quantidade > 100:

            await ctx.response.send_message('O limite maximo é de 100 mensagens')

            return

        elif quantidade == 0:

            await ctx.response.send_message('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 100 mensagens')

            return

        purge = await ctx.channel.purge(limit=quantidade)

        await ctx.respond(f"O chat teve {len(purge)} mensagens apagadas por {ctx.author.mention}")

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e apagou {len(purge)} mensagens no {ctx.channel}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'unban', description = 'Desbane um membro')
    @discord.option(name = 'id', description = 'Coloque o id do membro a desbanir')
    @discord.option(name = 'motivo', description = 'Escreva o motivo de Banir')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id, *, motivo = None):

        l1 = self.bot.get_channel(configData['logs']['mod'])

        if motivo == None:

            motivo = 'Não informado'

        e = discord.Embed(title = 'UnBan',

        description = f'Quem desbaniu: {ctx.author}\n quem foi desbanido: <@{id}> \nrazão: {motivo}')

        await l1.send(embed = e)

        user = await self.bot.fetch_user(id)

        await ctx.guild.unban(user)

        await ctx.respond(f'{id} desbanido com sucesso')

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e desbaniu o <@{id}>'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'say', description = 'Envia uma mensagem em um chat')
    @discord.option(name = 'canal', description = 'Escolha o canal que falar')
    @discord.option(name = 'mensagem', description = 'Escreva oq deseja que eu fale')
    async def say(self, ctx, canal: discord.TextChannel = None, *, mensagem = None):

        if mensagem == None:

            await ctx.respond('Você precisa escrever algo para enviar')

            return

        if canal == None:

            canal = ctx.channel

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e falou {mensagem}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

        channel2 = self.bot.get_channel(canal.id)

        await channel2.send(mensagem)

    @discord.slash_command(guild_only = True,name = 'veradv', description = 'Envia as advs de um membro')
    @discord.option(name = 'membro', description = 'Escolha o membro a remover a advertencia')
    async def veradv(self, ctx, membro: discord.Member):

        myquery = { "_id": membro.id}

        if adv.count_documents(myquery) == 1:

            cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e viu as advertencias de {membro.display_name}'''

            cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

            await cmdlc.send(cmdl)

            ad = adv.find_one({"_id": membro.id})

            adv1 = ad['Adv1']

            adv2 = ad['Adv2']

            adv3 = ad['Adv3']

            if adv1 == 'None':

                await ctx.respond('Esse membro não Possui advertencia', ephemeral = True)

                return

            if adv3 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}\nAdv3: {adv3}')

                await ctx.respond(embed = e, ephemeral = True)

                return

            if adv2 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}')

                await ctx.respond(embed = e, ephemeral = True)

                return

            if adv1 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}')

                await ctx.respond(embed = e, ephemeral = True)

                return

        await ctx.respond('Esse membro não Possui advertencia', ephemeral = True)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e viu as advertencias de {membro.display_name}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'editembed', description = 'Edita uma embed já enviada')
    @discord.option(name = 'channel', description = 'Envie o id do canal')
    @discord.option(name = 'embedid', description = 'Envie o id da embed')
    @discord.option(name = 'title', description = 'Escreva o titulo da embed')
    @discord.option(name = 'img', description = 'Escolha a imagem da embed')
    @discord.option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @discord.option(name = 'content', description = 'Escreva o conteudo da embed')
    @discord.option(name = 'color', description = 'Escolha a cor da embed')
    @commands.has_guild_permissions(manage_channels = True)
    async def editembed(self, ctx, channel: discord.TextChannel = None, embedid = None, title = None, img = '', mention: discord.Role = None, color = None, *, content = None):

        if channel == None:

            channel = ctx.channel
        
        if color == None:

            color = hexacolors.string('indigo')

        else:

            try:

                color = hexacolors.string(color)

            except:

                try:

                    color = hexacolors.hexadecimal(color)
                
                except:

                    color = hexacolors.string('indigo')

        if mention != None: 

            mention = mention.mention

        mensagem = await channel.fetch_message(int(embedid))

        e = discord.Embed(title = title, description = content, colour = color)

        e.set_image(url = img)

        e.set_footer(text = f'{ctx.guild.name}', icon_url = ctx.guild.icon)

        await mensagem.edit(mention,embed = e)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e editou a embed {embedid} no canal {channel.mention}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'editmsg', description = 'edita uma mensagem já enviada')
    @discord.option(name = 'channel', description = 'envie o id do canal')
    @discord.option(name = 'messageid', description = 'envie o id da mensagem')
    @discord.option(name = 'msg', description = 'Escreva a mensagem á editar')
    @commands.has_permissions(manage_channels = True)
    async def editmsg(self, ctx, channel: discord.TextChannel = None, messageid = None, *, msg = None):

        if channel == None:

            channel = ctx.channel

        mensagem = await channel.fetch_message(int(messageid))

        await mensagem.edit(msg)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e editou a mensagem {messageid} no chat {channel.mention}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'fmv', description = 'Move um membro para a sua call privada')
    @discord.option(name = 'membro', description = 'Escolha o membro para mover para uma call')
    @discord.option(name = 'canal', description = 'Escolha o canal para mover o membro')
    async def fmv(self, ctx, membro: discord.Member = None, canal: discord.VoiceChannel = None):

        call = self.bot.get_channel(canal.id)

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        await membro.move_to(call)

        await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e moveu o {membro.display_name} para o {canal.name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'fdsc', description = 'Desconecta uma pessoa da call')
    @discord.option(name = 'membro', description = 'Escolha o membro para desconectar da call')
    async def fdsc(self, ctx, membro: discord.Member = None):

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        await membro.move_to(None)

        await ctx.respond(f'{membro.mention} desconectado com sucesso', ephemeral = True)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e desconectou o {membro.display_name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(guild_only = True,name = 'verausentes', description = 'Mostra todos os membros em estado de ausente')
    async def verausente(self, ctx):

        if ausen.find_one({"_id": 'validador'})['valor'] == 1:

            await ctx.respond('Aqui está os ausentes', ephemeral = True)

            for x in ausen.find({'Ausente?': True}):

                await ctx.respond(f"Nome: {x['Nome']}\nData: {x['Data']}\nMotivo: {x['Motivo']}", ephemeral = True)
        
        else:

            await ctx.respond('Ninguem está ausente no momento', ephemeral = True)

    @discord.slash_command(guild_only = True,name = 'verticket', description = 'Mostra as mensagens do ultimo ticket de um membro')
    @discord.option(name = 'membro', description = 'Mostra as mensagens o ultimo ticket da pessoa')
    async def verticket(self, ctx, membro: discord.Member):

        try:

            await ctx.respond(file = discord.File('./tickets/ticket-{}.txt'.format(membro.id),f'Ticket de {membro.name}.txt'), ephemeral = True)

        except:

            await ctx.respond('Esse membro ainda não abriu um ticket', ephemeral = True)
    
    @discord.slash_command(name = 'list_colors', description = 'Lista as cores disponiveis por escrita')
    async def listcolors(self, ctx):

        await ctx.respond(hexacolors.listall, ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(commandsMod(bot))
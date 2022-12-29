import discord
#from .buttons import RmvCapEquipes, RmvCargoEquipes
from utils.loader import configData

class cargoevento2(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe eventos',
                description = 'Remove o cargo de chefe de eventos',
            ),
            discord.SelectOption(
                label = 'Apresentador',
                description = 'Remove o cargo de apresentador'
            ),
            discord.SelectOption(
                label = 'Auxiliar',
                description = 'Remove o cargo de auxiliar'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])

        apresentador = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['apresentador'])

        auxiliar = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['auxiliar'])

        if select.values[0] == 'Chefe eventos':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if capeventos not in membro.roles:

                    await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Remover cargo de Chefe de eventos')
                e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
                e.add_field(name = 'cargo', value = capeventos.mention)
                e.set_footer(text=membro.id)

                await channel.send(embed = e, view = RmvCapEquipes(self.bot, membro, capeventos, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Apresentador':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if apresentador not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de apresentador')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = apresentador.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, apresentador, interaction.user))

            self.stop()

        if select.values[0] == 'Auxiliar':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if auxiliar not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de auxiliar')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = auxiliar.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, auxiliar, interaction.user))

            self.stop()

class cargocall2(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Sub mod',
                description = 'Remove o cargo de sub mod',
            ),
            discord.SelectOption(
                label = 'Staff call',
                description = 'Remove o cargo de staff call'
            ),
            discord.SelectOption(
                label = 'Movimentação',
                description = 'Remove o cargo de movimentação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        submod = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])

        staffcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['staffcall'])

        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['movimenta'])

        if select.values[0] == 'Sub mod':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if submod not in membro.roles:

                    await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Remover cargo de sub mod')

                e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem removel ', value = interaction.user.mention, inline = False)
                e.add_field(name = 'cargo', value = submod.mention)
                e.set_footer(text=membro.id)

                await channel.send(embed = e, view = RmvCapEquipes(self.bot, membro, submod, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff call':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if staffcall not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de staff call')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = staffcall.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, staffcall, interaction.user))

            self.stop()

        if select.values[0] == 'Movimentação':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if movi not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de movimentação')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = movi.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, movi, interaction.user))

            self.stop()

class cargochat2(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Lider chat',
                description = 'Remove o cargo de Lider chat',
            ),
            discord.SelectOption(
                label = 'Staff chat',
                description = 'Remove o cargo de Staff chat'
            ),
            discord.SelectOption(
                label = 'Movimentação',
                description = 'Remove o cargo de movimentação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        liderchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])

        staffchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['staffchat'])

        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['movimenta'])

        if select.values[0] == 'Lider chat':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if liderchat not in membro.roles:

                    await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Remover cargo de Lider Chat')

                e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
                e.add_field(name = 'cargo', value = liderchat.mention)
                e.set_footer(text=membro.id)

                await channel.send(embed = e, view = RmvCapEquipes(self.bot, membro, liderchat, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff chat':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if staffchat not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de Staff Chat')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = staffchat.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, staffchat, interaction.user))

            self.stop()

        if select.values[0] == 'Movimentação':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if movi not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de Movimentação')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = movi.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, movi, interaction.user))

            self.stop()

class cargodiv2(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Promoters',
                description = 'Remove o cargo de promoters',
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Remove o cargo de divulgação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        promoters = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])

        divulgação = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['div'])

        if select.values[0] == 'Promoters':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if promoters not in membro.roles:

                    await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Remover cargo de Promoters')

                e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
                e.add_field(name = 'cargo', value = promoters.mention)
                e.set_footer(text=membro.id)

                await channel.send(embed = e, view = RmvCapEquipes(self.bot, membro, promoters, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Divulgação':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if divulgação not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de Divulgação')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = divulgação.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, divulgação, interaction.user))

            self.stop()

class cargomidia2(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Lider de midia',
                description = 'Remove o cargo de lider de midia',
            ),
            discord.SelectOption(
                label = 'Equipe de midia',
                description = 'Remove o cargo de equipe de midia'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        chefemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])

        equipemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['equipemidia'])

        if select.values[0] == 'Lider de midia':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if chefemidia not in membro.roles:

                    await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Remover cargo de Lider Midia')

                e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
                e.add_field(name = 'cargo', value = chefemidia.mention)
                e.set_footer(text=membro.id)

                await channel.send(embed = e, view = RmvCapEquipes(self.bot, membro, chefemidia, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Equipe de midia':

            await interaction.response.send_message('Mande no chat o id da pessoa a remover o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if equipemidia not in membro.roles:

                await interaction.channel.send('Este membro não possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Remover cargo de Equipe Midia')

            e.add_field(name = 'Quem vai ser removido o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)
            e.add_field(name = 'cargo', value = equipemidia.mention)
            e.set_footer(text=membro.id)

            await channel.send(embed = e, view = RmvCargoEquipes(self.bot, membro, equipemidia, interaction.user))

            self.stop()

class RmvCargos(discord.ui.View):

    def __init__(self, bot, timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Equeipe",
        options = [
            discord.SelectOption(
                label = 'Eventos',
                description = 'Cargos da equipe de eventos',
            ),
            discord.SelectOption(
                label = 'Call',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Chat',
                description = 'Cargos da equipe de chat'
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Midia',
                description = 'Cargos da equipe de Midia'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])

        capcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])

        capchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])

        capdiv = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])

        capmidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        if select.values[0] == 'Eventos':

            if capeventos in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai remover?', ephemeral = True, view = cargoevento2(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Call':

            if capcall in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai remover?', ephemeral = True, view = cargocall2(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Chat':

            if capchat in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai remover?', ephemeral = True, view = cargochat2(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Divulgação':

            if capdiv in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai remover?', ephemeral = True, view = cargodiv2(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Midia':

            if capmidia in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai remover?', ephemeral = True, view = cargomidia2(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return
import discord
from discord import app_commands
from discord.ext import commands

class iniciar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command()
    async def iniciar(self, interact:discord.Interaction):
        
        async def comprar_casa( interact:discord.Interaction):

            async def select_casa(interact:discord.Interaction):

                async def cosntruindo_casa(interact:discord.Interaction):
                    servidor = interact.guild
                    canal = interact.channel
                    categoria = canal.category

                    if categoria.name != 'Fora da Casa':
                        await categoria.edit(name='Fora da Casa')
 
                    if canal.name != 'grama':
                        await canal.edit(name='grama')
                   
                    lista = [lista.name for lista in servidor.categories]
                    if not 'Dentro da Casa' in lista:             
                        await servidor.create_category(name='Dentro da Casa')
                        id=  discord.utils.get(servidor.categories, name='Dentro da Casa')
                        await id.create_text_channel(name='Sala')
                        await id.create_text_channel(name='Quarto')
                        await id.create_text_channel(name='Cozinha')

                    await interact.response.send_message(f'{interact.user.display_name}, A Sua Casa Está Pronta')


                escolha = interact.data['values'][0]
                casas = {'Nv1':'Casa Nivel 1', 'Nv2':'Casa Nivel 2', 'Nv3':'Casa Nivel 3'}
                casa_escolhida = casas[escolha]

                embedConstruir = discord.Embed(title='Passo 2', description=f'Beleza, Agora que compramos a nossa {casa_escolhida}, Vamos Construi-la')
                embedConstruir.color = discord.Color.dark_orange()
                embedConstruir.set_footer(text='Pressione o botão para começar a construção da casa')

                botaoConstuir = discord.ui.Button(label='⚒️ COMEÇAR CONSTRUÇÂO ⚒️')
                botaoConstuir.callback = cosntruindo_casa
                view = discord.ui.View()
                view.add_item(botaoConstuir)
                await interact.response.send_message(embed=embedConstruir, view=view)

            
            embedCasa = discord.Embed(title='Passo 1', 
                                      description='Primeiro passo para nossa jornada se iniciar é comprar a nossa primeira casa')
            embedCasa.color = discord.Color.green()
            embedCasa.set_footer(text='Escolha qual tipo de casa Você vai Comprar')

            select = discord.ui.Select(placeholder='Selecionar Casa')
            option = [
                discord.SelectOption(label='Casa Nivel 1 -- 0 🪙', value='Nv1'),
                discord.SelectOption(label='Casa Nivel 2 -- 100 🪙', value='Nv2'),
                discord.SelectOption(label='Casa Nivel 3 -- 500 🪙', value='Nv3')
            ]

            select.options = option
            select.callback = select_casa
            view = discord.ui.View()
            view.add_item(select)

            await interact.response.edit_message(embed=embedCasa, view=view)


        embed = discord.Embed(title='O Incio', description=f'OK {interact.user.display_name}, Vamos Começar!')
        embed.color = discord.Color.gold()
        embed.set_footer(text='Clique no Botão para Continuar')

        view = discord.ui.View()
        botao = discord.ui.Button(label='Iniciar')
        botao.callback = comprar_casa

        view.add_item(botao)

        await interact.response.send_message(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(iniciar(bot))
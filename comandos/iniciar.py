import discord
from discord import app_commands
from discord.ext import commands

class iniciar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command()
    async def iniciar(self, interaction:discord.Interaction):
        async def comprar_casa(interactio:discord.Interaction):
            embedCasa = discord.Embed(title='Passo 1', 
                                      description='Primeiro passo para nossa jornada se iniciar é construir a sua casa')
            embed.color = discord.Color.green()
            embed.set_footer(text='Escolha qual tipo de casa Você vai comprar')

            await interactio.response.edit_message(embed=embedCasa)

        embed = discord.Embed(title='O Incio', description=f'OK {interaction.user.display_name}, Vamos Começar!')
        embed.color = discord.Color.gold()
        embed.set_footer(text='Clique no Botão para Continuar')

        view = discord.ui.View()
        botao = discord.ui.Button(label='Iniciar')
        botao.callback = comprar_casa

        view.add_item(botao)

        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(iniciar(bot))
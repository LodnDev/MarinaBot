import discord
from discord import app_commands
from discord.ext import commands

class iniciar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        super().__init__()

    @app_commands.command()
    async def iniciar(self, interaction:discord.Interaction):
        embed = discord.Embed(title='O Incio', description=f'OK {interaction.user.display_name}, Vamos Começar a nossa Incrivel Jornada')
        embed.color = discord.Color.gold()

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(iniciar(bot))
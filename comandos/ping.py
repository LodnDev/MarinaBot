import discord
from discord import app_commands
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply('Pong')

async def setup(bot):
    await bot.add_cog(ping(bot))
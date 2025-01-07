import discord
from discord.ext import commands
import json
import os

#Importação do Token:
config = "config.json"

with open(config, 'r') as arquivo:
    dado = json.load(arquivo)

token = dado['Token']

#Configurações de Permições:
intents = discord.Intents.default()
intents.message_content=True
intents.members=True
 
#Variavel que representa o Bot:
bot = commands.Bot(command_prefix=',', intents=intents) #Variavel que representa o Bot

#Função de Carregamento dos Comandos:
async def load_commands():
    for arquivo in os.listdir('comandos'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f'comandos.{arquivo[:-3]}')

#Comando Para Sincronizar os Slash Command:
@bot.command()
async def sinc(ctx:commands.Context):
    if ctx.author.id == 638799315917078538:
        sincronizar = await bot.tree.sync()
        await ctx.reply(f'Comandos sincronizados: {len(sincronizar)}')
    else:
        await ctx.reply(f'{ctx.author.display_name}, esse comando é apenas para o desenvolvedor')

#Iniciando o Bot:
@bot.event
async def on_ready():
    await load_commands()
    print('Estou Online')
bot.run(token=token)
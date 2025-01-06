import discord
from discord.ext import commands
from discord import app_commands
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

#Iniciando o Bot:
@bot.event
async def on_ready():
    await load_commands()
    print('Estou Online')
bot.run(token=token)
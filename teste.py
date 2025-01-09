import discord
from discord.ext import commands

# Define o prefixo dos comandos
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def obter_id_categoria(ctx, nome_categoria: str):
    # Procura pela categoria pelo nome
    categoria = discord.utils.get(ctx.guild.categories, name=nome_categoria)

    if categoria:
        await ctx.send(f'O ID da categoria "{nome_categoria}" é {categoria.id}')
    else:
        await ctx.send(f'Categoria "{nome_categoria}" não encontrada.')

# Insira o token do seu bot aqui
bot.run('SEU_TOKEN_AQUI')

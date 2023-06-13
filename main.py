import os
import discord #use py-cord see  https://pycord.dev/
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
url = 'https://letmegooglethat.com/?q='

bot = commands.Bot(debug_guilds=[1086638377534754897], status=discord.Status.dnd,
                   activity=discord.Activity(type=discord.ActivityType.listening, name="can you google?"))


@bot.listen()
async def on_ready():
    print("Now ready!")


@bot.slash_command(name="ping", description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.slash_command(name='url', description='get the lmgt link for what you want')
async def search(ctx, text: str):
    print(f'new request with {text}')
    url_new = f' {url}{text.replace(" ", "+")}'
    print(url_new)
    embed = discord.Embed(title="result", timestamp=discord.utils.utcnow(), )
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name='URL', value=url_new)
    await ctx.respond(embed=embed)


@bot.slash_command(name='info', description='get info about the bot')
async def info(ctx):
    embed= discord.Embed(title='info', timestamp=discord.utils.utcnow(), )
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name='general info.', value='this bot is made by the team of USF and hosted by blue atomic')
    embed.add_field(name='invite', value='https://discord.com/invite/nXWJtMg3nT')
    await ctx.respond(embed=embed)




bot.run(os.getenv('tolken'))

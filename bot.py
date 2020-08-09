import os
import json
from discord.ext import commands
from dotenv import load_dotenv
import random
#import regex

load_dotenv()
KEY = os.getenv('API_KEY')
TOKEN = os.getenv('DISCORD_TOKEN')
#client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hi')
async def test(ctx):

    await ctx.send("hello")



@bot.command(name='echo')
async def echo(ctx, *args):
    output = " "
    for words in args:
        output += words
        output += " "
    await ctx.message.delete()
    await ctx.send(output)



bot.run(TOKEN)

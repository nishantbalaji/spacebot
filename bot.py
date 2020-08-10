import os
import json
from discord.ext import commands
from dotenv import load_dotenv
import random
import http.client
from nasapy.api import *

load_dotenv()
KEY = os.getenv('API_KEY')
TOKEN = os.getenv('DISCORD_TOKEN')
NASA_KEY = os.getenv('NASA_KEY')
conn = http.client.HTTPSConnection("api.nasa.gov")

nasa = Nasa()

bot = commands.Bot(command_prefix='!', case_insensitive = True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hi')
async def test(ctx):

    await ctx.send("hello")

# Repeat a user's message back to them
@bot.command(name='echo')
async def echo(ctx, *args):
    if not args:
        await ctx.send("What you want me to say? (syntax `!echo [input]`)")
    else:
        output = " "
        for words in args:
            output += words
            output += " "
        await ctx.message.delete()
        await ctx.send(output)

# Get the picture of the day from NASA API
@bot.command(name='apod')
async def apod(ctx, *args):
    if not args:
        apod = nasa.picture_of_the_day(hd=True)
    else:
        date = str(args)
        try:
            apod = nasa.picture_of_the_day(date, hd=True)
        except:
            await ctx.send('Not a valid input, date must be in `YYYY-MM-DD`')
            return 0
    await ctx.send('Title: ' + apod['title'] + '\n' + 'Author: ' + apod['copyright'] + '\n' + 'Date: ' + apod['date'])
    await ctx.send(apod['hdurl'])
    await ctx.send('>>> ' + '*' + apod['explanation'] + '*')

#@bot.command(name='')
#@bot.command(name='help')
#async def help(ctx):


bot.run(TOKEN)

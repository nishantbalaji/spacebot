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
print(nasa.limit_remaining)


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
@bot.command(name='apod', help='Responds with NASA\'s picture of the day. Put the date after the command to specify a specific date. ')
async def apod(ctx, *args):
    if not args:
        apod = nasa.picture_of_the_day(hd=True)
        print('evaluating')
    else:
        date = str(args)
        try:
            apod = nasa.picture_of_the_day('2019-10-05', hd=True)
            print('im here')
        except:
            await ctx.send('Not a valid input, date must be in `YYYY MM DD`')
            return 0
            print()

    if 'copyright' in apod:
        await ctx.send('Title: ' + apod['title'] + '\n' + 'Author: ' + apod['copyright'] + '\n' + 'Date: ' + apod['date'])
    else:
        await ctx.send('Title: ' + apod['title'] + '\n' + 'Date: ' + apod['date'])
    await ctx.send(apod['hdurl'])
    await ctx.send('>>> ' + '*' + apod['explanation'] + '*')


@bot.command()
async def catchAll(ctx):
    await ctx.send('I didn\'t recognize that command.')
#@bot.command(name='')
#@bot.command(name='help')
#async def help(ctx):


bot.run(TOKEN)

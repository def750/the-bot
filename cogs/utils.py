import discord
from discord.ext import commands

import sys

import random

sys.path.insert(1, '../')
from config import *
sys.path.insert(1, '../constants')
from colors import *
from constants import *


#Loading Cog
class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(utils(bot))
    bot.add_command(roll)

@commands.command()
async def roll(ctx, n=100):
    try:
        int(n)
    except:
        return await ctx.send("N must be a digit")
    x = random.randrange(1, n)
    await ctx.send(x)
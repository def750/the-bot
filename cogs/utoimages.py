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
class utoimages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(utoimages(bot))
    bot.add_command(utoimg)

@commands.command(aliases=["utoimge", "utopic"])
async def utoimg(ctx):
    web = "https://the-bot.tk/uto/"
    unallowed = [235, 255]
    x = random.randrange(0, 385)
    if int(x) in unallowed:
        x = 1
    web = web + str(x) + ".jpg"
    embed=discord.Embed(title="Random Uto Image", color=0x9aecdb)
    embed.set_footer(text=f"Bot version: {const.version}")
    embed.set_image(url=web)
    await ctx.send(embed=embed)
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .utoimg at {ctx.author.guild.name}")
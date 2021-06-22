import discord
from discord.ext import commands

import os
import sys

import random

sys.path.insert(1, '../')
from config import *
sys.path.insert(1, '../constants')
from colors import *
from constants import *


#Loading Cog
class randimgs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(randimgs(bot))
    bot.add_command(zander)
    bot.add_command(bored)
    bot.add_command(ryu)

@commands.command()
async def zander(ctx):
    zanders = [
        "https://cdn.discordapp.com/attachments/826850315285561365/856844233990209536/Polish_20210608_231535877.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856844675633512448/image0.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856846736190472192/VID20210622184152.mp4",
        "https://cdn.discordapp.com/attachments/826850315285561365/856847534345158667/Polish_20210531_200109339.jpg",
        "https://cdn.discordapp.com/attachments/826850315285561365/856848031507939388/Polish_20210608_213709956.png",
        "https://cdn.discordapp.com/attachments/814428844991053844/856848116389249024/IMG20210607215430.jpg",
        "https://cdn.discordapp.com/attachments/814428844991053844/856848117060206592/Adobe_20210202_110709.jpg",
        "https://media.discordapp.net/attachments/826850315285561365/856848651262492692/unknown.png",
        "https://media.discordapp.net/attachments/826850315285561365/856848478994563072/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856850267437531166/20210622_185611_mfnr.jpg",
        "https://cdn.discordapp.com/attachments/826850315285561365/856850724800167946/VID20210622185751.mp4",
        "https://cdn.discordapp.com/avatars/524253275214577687/c44a0bb0544c2597740d6b57002c9605.png?size=4096",
        "https://media.discordapp.net/attachments/826850315285561365/856851548172582912/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856865307876524032/VID20210622195516.mp4",
    ]
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .zander at {ctx.author.guild.name}")
    await ctx.send(random.choice(zanders))

@commands.command()
async def bored(ctx):
    boreds = [
        "https://media.discordapp.net/attachments/826850315285561365/856855178216079380/unknown.png",
        "https://media.discordapp.net/attachments/826850315285561365/856855783165132850/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856865998435123240/Screenshot_20210618-092620_Discord.jpg",
        "https://cdn.discordapp.com/attachments/826850315285561365/856866546911805470/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856866613660090388/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856866649448382504/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856866747973894144/unknown.png",
    ]
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .bored at {ctx.author.guild.name}")
    await ctx.send(random.choice(boreds))

@commands.command()
async def ryu(ctx):
    ryus = [
        "https://media.discordapp.net/attachments/826850315285561365/856851773423091762/unknown-11.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856852025093652480/unknown-295.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856851977433251840/unknown.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856852454431129600/Discord_Vgd5QUxyMV-1.png",
        "https://cdn.discordapp.com/attachments/826850315285561365/856852368783179777/unknown-96.png",
        "https://cdn.discordapp.com/attachments/814545127359643708/855318578106728478/Screenshot_20210618_072919.jpg",
        "https://media.discordapp.net/attachments/826850315285561365/856853246981963786/ryuharam.PNG"
    ]
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .bored at {ctx.author.guild.name}")
    await ctx.send(random.choice(ryus))
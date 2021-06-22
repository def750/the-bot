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
class randimgs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(randimgs(bot))
    bot.add_command(russia)
    bot.add_command(thingthatneverhappened)
    bot.add_command(suisei)
    bot.add_command(taiwan)

@commands.command()
async def russia(ctx):
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .russia on {ctx.author.guild.name}")
    await ctx.send("https://cdn.discordapp.com/attachments/856905532925280267/856930631627309096/CB22D164-59CD-4701-8AA7-38AF136CFF40_w1200_r1.png")

@commands.command()
async def thingthatneverhappened(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/826850315285561365/856856851916652544/ezgif-7-19c47ec5c12c.gif")
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .thingthatneverhappened on {ctx.author.guild.name}")

@commands.command()
async def suisei(ctx):
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .suisei on {ctx.author.guild.name}")
    await ctx.send("""Not shitposting. This is serious. I think I genuinely need help. I really really want to fuck Hoshimachi Suisei. Something about her flat chest and her proud cute pure idol image really turn me on. I really want to rip off her idol clothes and expose how she's just a mere woman in front of me, whose only purpose is to be fucked as my personal whore. I want to ravage every inches of her little body as she tries to resist, only to realize how powerless she is against me. I want to fuck her in every possible position while groping her cute little tits, enjoying every seconds of her arousing moans. I want to fuck her for hours while she's thinking about how her fans will think of her, now that their cute comet idol is just a sex slave made purely for sex purpose. I want to whisper "Help will never come. You will never escape from here. Your idol career is over now and you'll spend the rest of your life as my personal sex slave" in her ear as she cries and struggles to escape until she eventually gives up. After I'm done with her, I won't even let her rest. I'll insert a rotor in her pussy and turn it on, leaving her moaning in my basement all the way until the next day, where I'll repeat this process over and over again until her mind is completely broken. A few months ago I didn't really care about her, but somehow these past few days I keep thinking about fucking her. I don't know what triggered it but I'm fucking lusting after Suisei now. "Why can't I have a cute idol vtuber sex slave" these thoughts always appear at the back of my mind. Please help me to get her out of my head because I think I might actually go insane at this point.""")

@commands.command()
async def taiwan(ctx):
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .taiwan on {ctx.author.guild.name}")
    await ctx.send("https://cdn.discordapp.com/attachments/826850315285561365/856979485429334057/asdasdasdasdasdasdasdas.png")
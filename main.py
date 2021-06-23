import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands.help import MinimalHelpCommand
import mysql.connector
from discord.ext.commands import CommandNotFound

import os
import sys
import asyncio

import mysql.connector
from mysql.connector import errorcode

#configs
from config import *
sys.path.insert(1, './constants')
from colors import *
from constants import *
from errors import *

#Try connecting to MySQL
try:
    print(f"{colors.yellow}Connecting to MySQL{colors.end}")
    mydb = mysql.connector.connect(
    host=       sql.host,
    user=       sql.user,
    password=   sql.password,
    database=   sql.database,
    port=       sql.port
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(errors.mysql.wrongcrid)
        exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(errors.mysql.databasenotfound)
        exit()
    else:
        print(f'{colors.red}{err}{colors.end}')
        exit()
else:
    print(f"{colors.green}Connected!{colors.end}")
    c = mydb.cursor()
    print(f"{colors.cyan}リンクスタート！{colors.end}")

#Define Bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=config.prefix, case_insensitive=True, intents=intents)

#Load cogs
for filename in os.listdir('./cogs'):
    filename1 = filename
    if filename.endswith('.py'):
        print(f"{colors.yellow}Loading {filename1}...{colors.end}")
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'{colors.green}Loaded {filename1}{colors.end}')

print(f"{colors.yellow}\n\nConnecting to discord server...{colors.end}")

#Send on bot start
@bot.event
async def on_ready():
    print(f'{colors.bigreen}\nBot loaded successfully!{colors.end}\n{colors.bigreen}Bot Name:{colors.end} {bot.user.name}\n{colors.bigreen}Bot ID:{colors.end} {bot.user.id}')

#Ignore command not found
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


############ Commands that cant be in classes because im too fucking dumb
@bot.command()
async def ping(ctx):
    await ctx.send("PONG!")

@bot.command()
async def china(ctx):
    china = bot.get_emoji(856862263825924136)
    await ctx.send(f"{china}")
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .china on {ctx.author.guild.name}")

@bot.command()
async def uto(ctx):
    utopray = bot.get_emoji(856842821428707358)
    await ctx.send(f"Praise be uto {utopray}")

#@bot.command()
#async def send_dm(ctx, member: discord.Member, y=15, *, content):
#    role = discord.utils.get(ctx.guild.roles, name="Ascended")
#    if role not in ctx.author.roles:
#        await ctx.send(f'No perms, you need to be Ascended')
#    if str(ctx.author.id) == "215024255526633482":
#        return
#    x = 0
#    if y > 15 or y <= 0:
#        return await ctx.send("You fucked up")
#    channel = await member.create_dm()
#    print(f"{ctx.author.name}#{ctx.author.discriminator} to {member.name}#{member.discriminator} {y} {content}")
#    while x != y:
#        await channel.send(content)
#        x += 1

#New send_dm

@bot.command()
async def send_dm(ctx, *args):
    if "-h" in args or "--help" in args:
        color = colors.embeds.blue
        embed=discord.Embed(title=",send_dm Command Help", description="`-msg` `<value>` - Sets text of the dm \n `-n` `<value>` - Amount of DM's \n `-u` `<@user>` - User, you must ping him or put the id", color=color)
        embed.add_field(name="Values", value="**Max for ascended:** 20\n **Max for Bot Owners:** 100", inline=False)
        embed.add_field(name="Example Usage", value=",send_dm -u <@615228438999072819> -n 10 -msg test", inline=False)
        embed.set_footer(text=f"Version: {const.version}")
        return await ctx.send(embed=embed)
    r_args = ["-u", "-n", "-msg"]

    if r_args[0] not in args or r_args[2] not in args:
        return await ctx.send("Forgot something, type `,send_dm -h` if you need help")
    if r_args[1] not in args:
        n = 5
    inp = args
    allowed_args = r_args
    dic = {}
    current_key = None
    for el in inp:
        if el in allowed_args:
            current_key = el
            dic[current_key] = []
        else:
            dic[current_key].append(el)
        
    for key, val in dic.items():
        dic[key] = " ".join(val)

    u = dic["-u"]
    n = dic["-n"]
    msg = dic["-msg"]
    numeric_filter = filter(str.isdigit, u)
    u = "".join(numeric_filter)

    #Check if n is an int
    try:
        n = int(n)
    except:
        return await ctx.send("-n argument must be an integer")

    #Check if user is ascended
    role = discord.utils.get(ctx.guild.roles, name="Ascended")
    if role not in ctx.author.roles:
        return await ctx.send(f'No perms, you need to be Ascended')
    else:
        if str(ctx.author.id) not in config.bot_owners:
            if int(n) > 20:
                return await ctx.send("Limit of dm's for ascended is 20")
        else:
            if int(n) > 100:
                return await ctx.send("Limit of dm's for bot owners is 100")
    if int(n) <= 1:
        return await ctx.send("Specify value that is bigger or equal to 1")

    
    #Main part
    x = 0
    member = ctx.guild.get_member(int(u))
    channel = await member.create_dm()
    print(f"{ctx.author.name}#{ctx.author.discriminator} to {member.name}#{member.discriminator} {n} {msg}")
    while x != int(n):
        await channel.send(msg)
        x += 1
        await asyncio.sleep(0.76)
#make vote
@bot.command()
async def makevote(ctx, *, text):
    upvote = bot.get_emoji(856969885129506866)
    downvote = bot.get_emoji(856969885023207435)
    embed=discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} started a poll!", description=f"{text}", color=colors.embeds.blue)
    embed.set_footer(text=f"Bot Version: {const.version}")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(upvote)
    await msg.add_reaction(downvote)
    print(f"{ctx.author.name}#{ctx.author.discriminator} used .makevote in {ctx.author.guild.name}@{ctx.channel}\nVote text: {text}")


bot.run(config.token)
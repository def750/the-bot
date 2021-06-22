import discord
from discord.ext import commands
import mysql.connector
from discord.ext.commands import CommandNotFound

import os
import sys

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
bot = commands.Bot(command_prefix=config.prefix, case_insensitive=True)

#Ładowanie cogów
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

@bot.command()
async def ping(ctx):
    await ctx.send("PONG!")

bot.run(config.token)
import discord
from discord.ext import commands

import sys
import mysql.connector


sys.path.insert(1, '../')
from config import *
sys.path.insert(1, '../constants')
from colors import *
from constants import *

#MySQL stuff
mydb = mysql.connector.connect(
    host=       sql.host,
    user=       sql.user,
    password=   sql.password,
    database=   sql.database,
    port=       sql.port
    )
c = mydb.cursor()

#Loading Cog
class permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(permissions(bot))
    bot.add_command(checkperms)

@commands.command()
async def checkperms(ctx, user : discord.Member=None):
    author = ctx.author
    server = ctx.guild
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued ,checkperms on {ctx.author.guild.name}")
    if user == None:
        c.execute("SELECT * FROM users WHERE user_id=%s AND server_id=%s", (author.id, server.id))
        res = c.fetchone()
        if not res:
            if str(author.id) in config.bot_owners:
                embed=discord.Embed(title="Perm level", description=f"**Permision level in DB:** 0\n**Group Name:** User\nYou're also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_author(name=f"{author.name}#{author.discriminator}'s Permissions")
                embed.set_thumbnail(url=f"{author.avatar_url}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title="Perm level", description=f"**Permision level:** 0\n**Group Name:** User", color=author.colour)
            embed.set_author(name=f"{author.name}#{author.discriminator}'s Permissions")
            embed.set_thumbnail(url=f"{author.avatar_url}")
            await ctx.send(embed=embed)   
        else:
            group = int(res[3])
            if group == 2:
                n_group = "Admin"
            elif group == 1:
                n_group = "Ascended"
            elif group == 0:
                n_group = "User"
            if str(author.id) in config.bot_owners:
                embed=discord.Embed(title="Perm level", description=f"**Permision level in DB:** {res[3]}\n**Group Name:** {n_group}\nYou're also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_author(name=f"{author.name}#{author.discriminator}'s Permissions")
                embed.set_thumbnail(url=f"{author.avatar_url}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title="Perm level", description=f"**Permision level:** {res[3]}\n**Group Name:** {n_group}", color=author.colour)
            embed.set_author(name=f"{author.name}#{author.discriminator}'s Permissions")
            embed.set_thumbnail(url=f"{author.avatar_url}")
            await ctx.send(embed=embed)
    else:
        c.execute("SELECT * FROM users WHERE user_id=%s AND server_id=%s", (user.id, server.id))
        res = c.fetchone()
        if not res:
            if str(user.id) in config.bot_owners:
                embed=discord.Embed(title="Perm level", description=f"**Permision level in DB:** 0\n**Group Name:** User\nThis user is also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_author(name=f"{user.name}#{author.discriminator}'s Permissions")
                embed.set_thumbnail(url=f"{user.avatar_url}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title="Perm level", description=f"**Permision level:** 0\n**Group Name:** User", color=user.colour)
            embed.set_author(name=f"{user.name}#{author.discriminator}'s Permissions")
            embed.set_thumbnail(url=f"{user.avatar_url}")
            await ctx.send(embed=embed)   
        else:
            group = int(res[3])
            if group == 2:
                n_group = "Admin"
            elif group == 1:
                n_group = "Ascended"
            elif group == 0:
                n_group = "User"
            if str(user.id) in config.bot_owners:
                embed=discord.Embed(title="Perm level", description=f"**Permision level in DB:** {res[3]}\n**Group Name:** {n_group}\nThis user is also Bot owner (Perm Level: 3)", color=user.colour)
                embed.set_author(name=f"{user.name}#{author.discriminator}'s Permissions")
                embed.set_thumbnail(url=f"{user.avatar_url}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title="Perm level", description=f"**Permision level:** {res[3]}\n**Group Name:** {n_group}", color=user.colour)
            embed.set_author(name=f"{user.name}#{author.discriminator}'s Permissions")
            embed.set_thumbnail(url=f"{user.avatar_url}")
            await ctx.send(embed=embed)
    


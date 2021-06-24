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
    bot.add_command(setperms)

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
                embed=discord.Embed(title=f"{author.name}#{author.discriminator}'s Permssions", description=f"**Permision level in DB:** 0\n**Group Name:** User\nYou're also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_thumbnail(url=f"{author.avatar_url}")
                embed.set_footer(text=f"Bot Version: {const.version}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title=f"{author.name}#{author.discriminator}'s Permssions", description=f"**Permision level:** 0\n**Group Name:** User", color=author.colour)
            embed.set_thumbnail(url=f"{author.avatar_url}")
            embed.set_footer(text=f"Bot Version: {const.version}")
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
                embed=discord.Embed(title=f"{author.name}#{author.discriminator}'s Permssions", description=f"**Permision level in DB:** {res[3]}\n**Group Name:** {n_group}\nYou're also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_thumbnail(url=f"{author.avatar_url}")
                embed.set_footer(text=f"Bot Version: {const.version}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title=f"{author.name}#{author.discriminator}'s Permssions", description=f"**Permision level:** {res[3]}\n**Group Name:** {n_group}", color=author.colour)
            embed.set_thumbnail(url=f"{author.avatar_url}")
            embed.set_footer(text=f"Bot Version: {const.version}")
            await ctx.send(embed=embed)
    else:
        c.execute("SELECT * FROM users WHERE user_id=%s AND server_id=%s", (user.id, server.id))
        res = c.fetchone()
        if not res:
            if str(user.id) in config.bot_owners:
                embed=discord.Embed(title=f"{user.name}#{user.discriminator}'s Permssionsl", description=f"**Permision level in DB:** 0\n**Group Name:** User\nThis user is also Bot owner (Perm Level: 3)", color=author.colour)
                embed.set_thumbnail(url=f"{user.avatar_url}")
                embed.set_footer(text=f"Bot Version: {const.version}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title=f"{user.name}#{user.discriminator}'s Permssions", description=f"**Permision level:** 0\n**Group Name:** User", color=user.colour)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.set_footer(text=f"Bot Version: {const.version}")
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
                embed=discord.Embed(title=f"{user.name}#{user.discriminator}'s Permssions", description=f"**Permision level in DB:** {res[3]}\n**Group Name:** {n_group}\nThis user is also Bot owner (Perm Level: 3)", color=user.colour)
                embed.set_thumbnail(url=f"{user.avatar_url}")
                embed.set_footer(text=f"Bot Version: {const.version}")
                return await ctx.send(embed=embed)
            embed=discord.Embed(title=f"{user.name}#{user.discriminator}'s Permssions", description=f"**Permision level:** {res[3]}\n**Group Name:** {n_group}", color=user.colour)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.set_footer(text=f"Bot Version: {const.version}")
            await ctx.send(embed=embed)
    
@commands.command()
async def setperms(ctx, user : discord.Member=None, level=0):
    if str(ctx.author.id) not in config.bot_owners:
        return await ctx.send("You must be bot owner to do that")

    #Help
    if user == None:
        return await ctx.send("Help wip")

    #Syntax checks
    try:
        level = int(level)
    except:
        return await ctx.send("Permission level argument must be a digit")
    if level > 2 or level < 0:
        return await ctx.send("Level must be in range of 0-2")
    
    #Check if user tries to change his own perms
    if str(user.id) == str(ctx.author.id):
        return await ctx.send("You can't change your own perms")

    #Assign group name    
    if level == 2:
        n_group = "Admin"
    elif level == 1:
        n_group = "Ascended"
    elif level == 0:
        n_group = "User"

    y = colors.yellow
    e = colors.end

    #Fetch from database
    c.execute(f"SELECT * FROM users WHERE user_id={user.id} and server_id={ctx.guild.id}")
    res = c.fetchone()

    #Check if in database
    if not res:
        prev_level = 0
        user_tag = f"{ctx.author.name}#{ctx.author.discriminator}"

        ###LOG MESSAGE###
        log_msg = f"Changed permission level of <{user.name}#{user.discriminator} ({user.id})> from {prev_level} to {level}"
        ###LOG MESSAGE###

        #SQL
        sql = "INSERT INTO users (user_id, server_id, group_id) VALUES (%s, %s, %s)"
        val = (user.id, ctx.guild.id, level)
        c.execute(sql, val)
        sql = "INSERT INTO logs (user_id, user_tag, server_id, log) VALUES (%s, %s, %s, %s)"
        val = (ctx.author.id, user_tag, ctx.guild.id, log_msg)
        c.execute(sql, val)
        mydb.commit()

        #embed
        embed=discord.Embed(title=f"Changed {user.name}#{user.discriminator}'s permissions", description=f"**Previous level:** {prev_level}\n**New Level:** {level}\n**Group Name:** {n_group}", color=user.colour)
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.set_footer(text=f"Bot Version: {const.version}")
        ###CONSOLE LOG NOTICE
        print(f"\n{colors.red}-----[ IMPORTANT NOTICE ]-----")
        print(f"Permission change")
        print(f"{y}Executed By: {e}{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
        print(f"{y}User affected: {e}{user.name}#{user.discriminator} ({ctx.user.id})")
        print(f"{y}Previous Group: {e}{prev_level}")
        print(f"{y}New Group: {e}{level}")
        print(f"{y}Server: {e}{ctx.guild.name} ({ctx.guild.id})")
        print(f"{colors.red}This event was also logged to database!{e}\n")
        return await ctx.send(embed=embed)
    else:
        #Previous level
        prev_level = res[3]
        #User Tag
        user_tag = f"{ctx.author.name}#{ctx.author.discriminator}"

        
        ###LOG MESSAGE###
        log_msg = f"Changed permission level of <{user.name}#{user.discriminator} ({user.id})> from {prev_level} to {level}"
        ###LOG MESSAGE###

        #SQL
        c.execute("UPDATE users SET group_id=%s WHERE user_id=%s AND server_id=%s", (level, user.id, ctx.guild.id))
        sql = "INSERT INTO logs (user_id, user_tag, server_id, log) VALUES (%s, %s, %s, %s)"
        val = (ctx.author.id, user_tag, ctx.guild.id, log_msg)
        c.execute(sql, val)
        mydb.commit()

        #Embed
        embed=discord.Embed(title=f"Changed {user.name}#{user.discriminator}'s permissions", description=f"**Previous level:** {prev_level}\n**New Level:** {level}\n**Group Name:** {n_group}", color=user.colour)
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.set_footer(text=f"Bot Version: {const.version}")
        ###CONSOLE LOG NOTICE
        print(f"\n{colors.red}-----[ IMPORTANT NOTICE ]-----")
        print(f"Permission change")
        print(f"{y}Executed By: {e}{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
        print(f"{y}User affected: {e}{user.name}#{user.discriminator} ({ctx.user.id})")
        print(f"{y}Previous Group: {e}{prev_level}")
        print(f"{y}New Group: {e}{level}")
        print(f"{y}Server: {e}{ctx.guild.name} ({ctx.guild.id})")
        print(f"{colors.red}This event was also logged to the database!{e}\n")
        return await ctx.send(embed=embed)
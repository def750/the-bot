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
    #If user not sepecified set it to command author
    if user == None:
        user = ctx.author
        other = False
    else:
        other = True

    #Sql
    c.execute(f"SELECT id, group_id FROM users WHERE user_id={user.id} AND server_id={ctx.guild.id}")
    res = c.fetchone()

    #Check if in database
    if not res:
        weight = 0
        group_id = 0
        group_name = "User"
        db_id = "Not in DB"
    else: 
        c.execute(f"SELECT * FROM permission_table WHERE group_id={res[1]}")
        grp = c.fetchone()
        group_id = grp[0]
        group_name = grp[1]
        weight = grp[2]
        db_id = res[0]

    #Embed Strings#
    db_group_id = f"**Group ID:** {group_id}\n"
    db_group_name = f"**Group Name:** {group_name}\n"
    db_permission_level = f"**Permission level:** {weight}\n"

    #Check if user was specified or not again
    if other == True:
        pron = "This user is also"
    else:
        pron = "You're also"

    #Check if command author is bot owner (additional info)
    if str(ctx.author.id) in config.bot_owners:
        display_id = f"**Entry ID:** {db_id}\n"
    else:
        display_id = ""

    if str(user.id) in config.bot_owners:
        q_bot_owner = f"\n{pron} Bot Owner (**Permission level:** {config.bot_owners_weight})"
    else:
        q_bot_owner = ""

    #Embed Embed
    embed=discord.Embed(title=f"{user.name}#{user.discriminator}'s Permssions", description=f"{db_group_name}{db_group_id}{db_permission_level}{display_id}{q_bot_owner}", color=user.colour)
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

    #Check if level is 3 (Bot owner which is hard coded)
    if level == 3:
        return await ctx.send(f"This group id is reserved and unsettable, if you want someone added here ask def750")
    
    #Check if group exist
    c.execute(f"SELECT group_id FROM permission_table WHERE group_id={level}")
    res1 = c.fetchone()
    if not res1:
        return await ctx.send(f"Group with id {level} does not exist!")

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
        p_weight = 0
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


        c.execute(f"SELECT weight FROM permission_table WHERE group_id={level}")
        w = c.fetchone()
        weight = w[0]

        #embed
        embed=discord.Embed(title=f"Changed {user.name}#{user.discriminator}'s permissions", description=f"**Previous level:** {prev_level} ({p_weight})\n**New Level:** {level} ({weight})\n**Group Name:** {n_group}", color=user.colour)
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.set_footer(text=f"Bot Version: {const.version}")
        ###CONSOLE LOG NOTICE
        print(f"\n{colors.red}-----[ IMPORTANT NOTICE ]-----")
        print(f"Permission change")
        print(f"{y}Executed By: {e}{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
        print(f"{y}User affected: {e}{user.name}#{user.discriminator} ({user.id})")
        print(f"{y}Previous Group: {e}{prev_level} ({p_weight})")
        print(f"{y}New Group: {e}{level} ({weight})")
        print(f"{y}Server: {e}{ctx.guild.name} ({ctx.guild.id})")
        print(f"{colors.red}This event was also logged to database!{e}\n")
        return await ctx.send(embed=embed)
    else:
        #Previous level
        prev_level = res[3]
        c.execute(f"SELECT weight FROM permission_table WHERE group_id={res[3]}")
        w = c.fetchone()
        p_weight = w[0]
        #User Tag
        user_tag = f"{ctx.author.name}#{ctx.author.discriminator}"

        c.execute(f"SELECT weight FROM permission_table WHERE group_id={level}")
        w = c.fetchone()
        weight = w[0]
        
        ###LOG MESSAGE###
        log_msg = f"Changed permission level of <{user.name}#{user.discriminator} ({user.id})> from {prev_level} ({p_weight}) to {level} ({weight})"
        ###LOG MESSAGE###

        #SQL
        c.execute("UPDATE users SET group_id=%s WHERE user_id=%s AND server_id=%s", (level, user.id, ctx.guild.id))
        sql = "INSERT INTO logs (user_id, user_tag, server_id, log) VALUES (%s, %s, %s, %s)"
        val = (ctx.author.id, user_tag, ctx.guild.id, log_msg)
        c.execute(sql, val)
        mydb.commit()


        #Embed
        embed=discord.Embed(title=f"Changed {user.name}#{user.discriminator}'s permissions", description=f"**Previous level:** {prev_level} ({p_weight})\n**New Level:** {level} ({weight})\n**Group Name:** {n_group}", color=user.colour)
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.set_footer(text=f"Bot Version: {const.version}")
        ###CONSOLE LOG NOTICE
        print(f"\n{colors.red}-----[ IMPORTANT NOTICE ]-----")
        print(f"Permission change")
        print(f"{y}Executed By: {e}{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
        print(f"{y}User affected: {e}{user.name}#{user.discriminator} ({user.id})")
        print(f"{y}Previous Group: {e}{prev_level} ({p_weight})")
        print(f"{y}New Group: {e}{level} ({weight})")
        print(f"{y}Server: {e}{ctx.guild.name} ({ctx.guild.id})")
        print(f"{colors.red}This event was also logged to the database!{e}\n")
        return await ctx.send(embed=embed)

@commands.command()
async def creategroup(ctx, name, weight):
    if str(ctx.author.id) not in config.bot_owners:
        return await ctx.send("You must be bot owner to do that")
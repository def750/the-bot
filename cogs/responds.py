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
    bot.add_command(tiananmen)
    bot.add_command(americans)

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

@commands.command(aliases=["square"])
async def tiananmen(ctx):
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .china on {ctx.author.guild.name}")
    await ctx.send("""动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门""")

@commands.command()
async def americans(ctx):
    print(f"{ctx.author.name}#{ctx.author.discriminator} issued .americans on {ctx.author.guild.name}")
    await ctx.send("Americans 🤢 🇺🇸 -> 🔥")
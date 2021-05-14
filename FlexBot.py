# Discord imports:
import discord
from discord.ext import tasks, commands

#import voiceCog
import os
import random
import time
import sys
import datetime
import asyncio
from itertools import cycle
# dotenv:

TOKEN = "ODQyNzI5OTUzNjM5OTIzNzEy.YJ5jbg.S0dFKcdQDdXpM76QSpDfh4TJ_9U"
GUILD = 'Unbroken-Discord'
HARRYPOTTER = ['Ich seh nichts! Erstmal Brille aufsetzen, die ich natürlich sehe.', ('Wieso, ich kann das! Hab ich erst neulich im Zoo gemacht... neulich vor einem Jahr...') ]

# setup:
client = discord.Client()
bot = commands.Bot(command_prefix='+')

# precode:
status = ["test", "test1"]
settings = {"role_check": True, "change_status": True, "auto_text": False, "test_loop_delay": 3,
            "change_status_delay": 5, "dev_colour": True}
channels = []
welcome_channel = None

for guild in bot.guilds:
    if guild.name == GUILD:
        break
    for i in guild.text_channels:
        if i.category_id == 693529477288034344:
            if i.name == "normal-shit":
                welcome_channel = i
            channels.append(i.name)


# functions:
def is_not_pinned(mess):
    return not mess.pinned

def usual_check():
    return None
# loops:
async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed():
        if settings["change_status"]:
            current_status = next(msgs)
            await bot.change_presence(activity=discord.Game(name=current_status, type=1))
            await asyncio.sleep(settings["change_status_delay"])

async def test_loop():
    await bot.wait_until_ready()
    arr = []
    while not bot.is_closed():
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
        for channel in guild.channels:
            if channel.name == "Flex":
                print(f"found {channel.name}")
                print(channel.members)
                print(channel.type)
                break
        
        for member in channel.members:
            print(member)
            channel = await guild.create_voice_channel(f"{member.name}'s channel")
            arr.append(channel)
            await member.move_to(channel)
        
        for t in arr:
            if t.members == []:
                print(f"{t.name} has no members")
                arr.remove(t)
                await t.delete()
            else:
                print(f"{t.name} has members: {t.members}")
        print(f"arr is {arr}")
    
        await asyncio.sleep(1)


# bot events:


# for i in guild.channels:
# if i.name == "willkommen":
# link = await i.create_invite(max_age=15)
# print("invite-link = ", link)
"""
@commands.has_role('Ehre')
@bot.command(name="de-role", help="Removes Ventilator-role from member passed as argument")
async def derole(ctx, *args):
    for guild in bot.guilds:
        for member in guild.members:
            if member.name == "Penis(70cm)":
                await member.remove_roles(discord.utils.get(member.guild.roles, name="Ventilator"))




@bot.command(pass_context=True, name="venti", help="gives user ventilator-role")
async def giverole(ctx, user):
    if user == None:
        user = ctx.message.author
    await user.add_roles(discord.utils.get(user.guild.roles, name="Ventilator"))
    await ctx.send("Ne jetzt bin ich im Fluss")
    print("{} hat die Rolle Ventilator bekommen.".format(user))

@bot.command(help="!W.I.P: Creates Embed ")
@commands.has_role('Ehre')
async def test(ctx, *args):
    embed = discord.Embed(title="Announcements", color=0x00ff00)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await ctx.send(embed=embed)


@bot.command(help="!W.I.P: Creates Embed ")

async def test2(ctx, *args):
    channel = ctx.message.channel
    await channel.purge(limit=1)
    async for message in channel.history(limit=1):
        await ctx.send("was geht so " + message.author.mention +"?")

"""

"""
 timestamp=datetime.datetime,
@bot.command()
@commands.has_role('Ehre')
async def rolle(ctx, member: discord.Member):
    print("hi")
    await member.remove_roles(discord.utils.get(member.guild.roles, name="Ehre"))
"""

bot.loop.create_task(change_status())
bot.loop.create_task(test_loop())
bot.load_extension('Cogs.listenerCog')
bot.load_extension('Cogs.voiceCog')
bot.load_extension('Cogs.cmdCog')
bot.run(TOKEN)


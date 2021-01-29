import discord
from discord.ext import commands
import random
import pandas as pd
import sqlite3


client = commands.Bot(command_prefix='--')

@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Current Version",description="R2D2 is in version 1.0", color=0x2A05A9)
    myEmbed.add_field(name="Version Code:", value="v1.0.0",inline=False)
    myEmbed.add_field(name="Date Released:", value="January 27th 2021", inline=False)
    myEmbed.set_footer(text="Creator: Andrew White")
    await context.message.channel.send(embed=myEmbed)

@client.command(name='details')
async def version(context):
    myEmbed = discord.Embed(title="Born",description="I was born on Andrews computer", color=0x2A05A9)
    myEmbed.add_field(name="Nickname", value="Slayer",inline=False)
    myEmbed.add_field(name="Birthday:", value="January 27th 2021", inline=False)
    myEmbed.set_footer(text="Creator: Andrew White")
    await context.message.channel.send(embed=myEmbed)

#command gets the amount of people in the discord server
@client.command(name='members')
async def version(context):
    await context.message.channel.send(context.guild.member_count)


@client.event
async def on_message(message):
    if message.content == 'send love':
        general_channel = client.get_channel(785339737245876239)
        await message.author.send('I love you')

        # await general_channel.send()
    
    await client.process_commands(message)

@client.event
async def on_ready():
    list_of_games = ['Minecraft', 'Fortnite', 'Call of Duty', 'World of Warcraft', 'Guild Wars', 'Your Mom', 'Your sister', 'Star Wars', 'Saving the Galaxy']
    general_channel = client.get_channel(785339737245876239)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(random.choice(list_of_games)))
    # await general_channel.send('Beep, Beep, Hello channel')


#Allow bot to kick members 
@client.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)

async def kick(context, member: discord.Member):
    await member.kick()
    await context.send('User ' + member.display_name + ' has been kicked.')


#Allow bot to ban members 
@client.command(name="ban", pass_context=True)
@commands.has_permissions(kick_members=True)

async def ban(context, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned.')



#sending images 
@client.command(name="favimage")
async def favimage(context):

    fav_image = "anikan.jpg"
    await context.send(file=discord.File(fav_image))


@client.event
async def on_member_join(member):
    await sleep(10)
#run the bot on the server
client.run('ODA0MTYxMjAwMTc4OTg3MDE4.YBITeg.qMUh1SpfX9b-v-9KWKcfpm2zgWk')
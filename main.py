import discord
from discord.ext                            import commands
client = discord.Client()

#var import
from var                                    import *
#function imports
from functions.general.hellobot             import hellobot
from functions.general.help                 import botHelp
from functions.util.random                  import random

@client.event
async def on_ready(): #when ready
    global botName
    botName = '{0.user}'.format(client)
    botName = botName[:-5]

    global avatar
    avatar = client.user.avatar_url

    print('Logged in as {0.user}'.format(client)) #show in command shell

@client.event
async def on_message(message): #fetch messages
    if message.author == client.user: #don't continue if made by bot
        return

    #GENERAL
    if message.content == "<@!" + str(client.user.id) + ">": #help by bot mention
        await botHelp(botName, avatar, message)
        return

    if message.content == prefix + 'help': #help by command
        await botHelp(botName, avatar, message)
        return

    if message.content == prefix + 'hellobot': #response test
        await hellobot(botName, avatar, message)
        return

    #UTILITY
    if message.content.startswith(prefix + 'random') or message.content.startswith(prefix + 'r'): #random number
        await random(botName, avatar, message, "normal")
        return

    if message.content.startswith(prefix + 'saucerand'): #random sauce
        await random(botName, avatar, message, "sauce")
        return

    #MUSIC
    if message.content == prefix + 'join': #join vc
        channel = message.author.voice.channel
        await channel.connect()

client.run(TOKEN) #RUN
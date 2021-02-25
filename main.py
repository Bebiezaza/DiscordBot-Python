import discord
from discord.ext import commands
client = discord.Client()

#function imports
from functions.general.hellobot import hellobot

@client.event
async def on_ready() : #when ready
    global prefix
    prefix = "$"

    global botName
    botName = '{0.user}'.format(client)
    botName = botName[:-5]

    global avatar
    avatar = client.user.avatar_url

    print('Logged in as {0.user}'.format(client)) #show in command shell

@client.event
async def on_message(message) : #fetch messages
    if message.author == client.user: #don't continue if made by bot
        return

    #   //help by bot mention
    # if (message.content === "<@!" + client.user.id + ">") {
    #     help(client, message, embed);
    #     return;
    # }

    if message.content == "<@!" + str(client.user.id) + ">": #help by bot mention
        await message.channel.send("HELP")

    if message.content.startswith(prefix + 'hellobot'):
        await hellobot(botName, avatar, message)
        return

client.run('NzI2MDcyMDg4NTQ4NjA1OTYy.XvX9Uw._Zf9z_tFG5IsR1QN-v6kgwPyia4') #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)
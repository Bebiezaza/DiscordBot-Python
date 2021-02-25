import discord
from discord.ext import commands
client = discord.Client()

global helpText
helpText = "***ALL COMMANDS***"

@client.event
async def help(botName, avatar, message):
    embed = discord.Embed(description = helpText, color = 0xf1c40f)
    embed.set_author(name = botName + "Alpha 2.0.0", url = embed.Empty, icon_url = avatar)
    await message.channel.send(embed = embed)
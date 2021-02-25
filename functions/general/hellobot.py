import discord
from discord.ext import commands
client = discord.Client()

@client.event
async def hellobot(botName, avatar, message):
    embed = discord.Embed(description = 'hello people', color = 0xf1c40f)
    embed.set_author(name = botName, url = embed.Empty, icon_url = avatar)
    await message.channel.send(embed = embed)
import discord
from discord.ext import commands
client = discord.Client()

@client.event
async def embed(botName, avatar, message, text):
    embed = discord.Embed(description = text, color = 0xf1c40f)
    embed.set_author(name = botName, url = embed.Empty, icon_url = avatar)
    await message.channel.send(embed = embed)
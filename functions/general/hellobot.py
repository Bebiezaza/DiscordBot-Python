import discord
from discord.ext import commands
client = discord.Client()

from ..embed import embed

@client.event
async def hellobot(botName, avatar, message):
    await embed(botName, avatar, message, "hello people")
import discord
from discord.ext import commands
client = discord.Client()

from var import *
from ..embed import embed

global helpText
helpText =              "__**ALL COMMANDS**__\n"
helpText = helpText +   "\n"
helpText = helpText +   "__**General**__\n"
helpText = helpText +   "**" + prefix + "help / bot mentions** = display commands\n"
helpText = helpText +   "**" + prefix + "hellobot** = response test\n"
helpText = helpText +   "\n"
helpText = helpText +   "__**Utility**__\n"
helpText = helpText +   "**" + prefix + "random [min] [max]** / **" + prefix + "r [min] [max]** = random number generator\n"
helpText = helpText +   "**" + prefix + "saucerand** = sauce randomization, result not guaranteed\n"

@client.event
async def botHelp(botName, avatar, message):
    await embed(botName, avatar, message, helpText)
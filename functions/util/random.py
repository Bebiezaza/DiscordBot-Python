import discord
from discord.ext import commands
client = discord.Client()

from var import *
from ..embed import embed

@client.event
async def random(botName, avatar, message, identity):
    if identity == "sauce":
        # generate random integer values
        from random import randint

        # generate some integers
        rand = str(randint(1, 320000))

        #print
        await message.channel.send(rand + "\nThis post was made by a random number generator\nresult not guaranteed")
        
    elif identity == "normal":
        args = message.content.split(" ")

        if len(args) == 1:
            await embed(botName, avatar, message, "**You forgot both input.\n __Usage:__ " + prefix + "random [min] [max]** or **" + prefix + "r [min] [max]** \n\nRequested by <@!" + str(message.author.id) + ">")
        elif len(args) == 2:
            await embed(botName, avatar, message, "**You forgot the second input.\n __Usage:__ " + prefix + "random [min] [max]** or **" + prefix + "r [min] [max]** \n\nRequested by <@!" + str(message.author.id) + ">")
        else:
            minNum = args[1]
            maxNum = args[2]

            if minNum > maxNum:
                await embed(botName, avatar, message, "**The second input is lower than the first input.\n __Usage:__ " + prefix + "random [min] [max]** or **" + prefix + "r [min] [max]** \n\nRequested by <@!" + str(message.author.id) + ">")
            else:
                # generate random integer values
                from random import randint

                # generate some integers
                rand = str(randint(int(minNum), int(maxNum)))

                #print
                await embed(botName, avatar, message, "__**Random:**__ " + minNum + " to " + maxNum + "\n**= " + rand + "**\n\nRequested by <@!" + str(message.author.id) + ">")
    
    await message.delete()
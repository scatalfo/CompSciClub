import discord
import asyncio


command_prefix = '!'
description = 'Bot for NA pros'
client = discord.Client()
timesUsed = 0


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.__version__)


@client.event
async def on_message(message):
    global timesUsed
    if(message.content.startswith('!test')):
        timesUsed=timesUsed+1
        await client.send_message(message.channel, "This is a test command! This command has been used " + str(timesUsed) + " times since the launch of this bot!")
    if(message.content.startswith('!resetTest')):
        timesUsed = 0
        await client.send_message(message.channel, "Times used has been reset to 0")
    if(message.content.startswith('!help')):
        user = message.author
        await client.send_message(message.channel, user.mention + " you have been private messaged all the neccessary info!")
        await client.send_message(user, "This is a test private message!")


client.run('NTIyNjM3ODg2MjE1MTU5ODA5.DvN4Gg.PopEeJqDCjsE0YYdp3oWIYz0XS0')


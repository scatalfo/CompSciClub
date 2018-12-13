import discord
import asyncio
from games import TicTacToe
from sys import exit

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.content.lower().startswith('!challenge'):
        await msg_challenge(message)

    elif message.content.lower().startswith('!move'):
        await msg_move(message)

    elif message.content.lower().startswith('!quit'):
        await msg_quit(message)
    elif message.content.lower().startswith('!redraw'):
        await msg_redraw(message)




async def msg_challenge(message):
    p1 = message.author
    if len(message.mentions) != 1:
        await client.send_message(message.channel, 'Please mention one player.')
        return
    p2 = message.mentions[0]

    for g in games:
        if p1 in g.players or p2 in g.players:
            await client.send_message(message.channel, 'One player is already in a game.')
            return

    if p2 == p1:
        await client.send_message(message.channel, 'Can\'t play against yourself.')
        return

    cnt = message.content.lower()
    game = TicTacToe([p1, p2])
    await game.start(client, message)

    print('Created game ' + str(game))
    games.append(game)


async def msg_move(message):
    for i in range(len(games)):
        g = games[i]
        if g.is_over():
            del games[i]
            break
        if message.author == g.get_whose_turn():
            await g.make_move(client, message)

            break


async def msg_redraw(message):
    for g in games:
        if message.author in g.players:
            print('Redrawing ' + str(g))
            await g.draw(client, message)
            break


async def msg_quit(message):
    for i in range(len(games)):
        if message.author in games[i].players:
            print('Killing game ' + str(games[i]))
            await client.send_message(message.channel, 'Destroyed game: ' + str(games[i]))
            del games[i]
            return
    await client.send_message(message.channel, 'You are not in any game.')




games = []

client.run('NTIyNjU1MDQxMzAwMjAxNDgz.DvOIBg.Z3O61JTU4P5im2pJMgZZfF7PPd4')

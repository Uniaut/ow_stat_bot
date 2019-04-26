import discord

from useful import embed_format

import random

async def decide(client, msg):
    order_contents = msg.content.split(' ')
    del order_contents[0]

    if len(order_contents) < 2:
        return None

    await client.send_message(msg.channel,
        embed = embed_format(
        title = '과연 무엇이 뽑혔을까요?',
        description = '두구두구두구~~~~~\n**%s** 로 결정되었습니다!.'
            %random.choice(order_contents),
        thumbnail = 'http://bitly.kr/erT4D'))

async def anon(client, msg):
    order_contents = msg.content.split(' ', 1)
    del order_contents[0]
    await client.delete_message(msg)
    await client.send_message(msg.channel,
        embed = embed_format(
        title = '익명 발언입니다 :',
        description = order_contents[0],
        thumbnail = 'http://bitly.kr/RqxP2'))

# debugging only   
async def game(client, msg):
    order_contents = msg.content.replace('!겜 ', '')
    await client.delete_message(msg)
    activ = discord.Game(name = order_contents)
    await client.change_presence(game = activ,
        status = discord.Status.online)

orders = {
    '!결정'     : decide,
    '!익명'     : anon,
    '!겜'       : game
}
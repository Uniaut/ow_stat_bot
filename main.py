#-*-coding:utf-8
import asyncio
import discord
import random

from engine import act

from preference import token

client = discord.Client()

logout_pw = 0

@client.event
async def on_ready():
    print("Logged in as ")
    print('Name: ' + client.user.name)
    print('ID  : ' + client.user.id)
    print("===========")
    global logout_pw
    logout_pw = random.randint(1, 10)
    print('logout pw: ' + str(logout_pw))
    print("===========")
    await client.change_presence(
        game = discord.Game(name = 'overwatch.op.gg'),
        status = discord.Status.online
    )

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '!종료 ' + str(logout_pw):
        await client.send_message(message.channel, '봇을 종료합니다.')
        await client.logout()
        print("=========================")
        print("Bot logged out")
        print("=========================")
        return None

    if message.content.startswith('!'):
        await act(client, message)

client.run(token)

def _atexit():
    client.logout()
import atexit
atexit.register(_atexit)


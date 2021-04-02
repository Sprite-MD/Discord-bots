import discord
import asyncio
import os
from dotenv import load_dotenv
import random

'''
Start with !r to roll dice. example format: !r 5d6

Rolls a d6 5 times ^^

'''



token = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


def roll(s):
    total = 0
    
    if 'd' in s:
        times = s.split('d')[0]
        sides = s.split('d')[1]
        total = [random.randint(1,int(sides)) for x in range(int(times))]
        '''for x in range(int(times)):
            total += random.randint(1,int(sides))
            print(total)'''
        return sum(total)

    else:
        total += random.randint(1,int(s))
        return total


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("!r"):
        dice = message.content.split()[1]
        await message.channel.send(roll(dice))



client.run(token)



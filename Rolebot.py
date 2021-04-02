import discord
import asyncio
import os

intents = discord.Intents.default()
intents.members = True


token = ''

client = discord.Client(intents = intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    try:
        role = discord.utils.get(member.guild.roles, id = 731441766896631869)
        await member.add_roles(role)
    except Exception as e:
        print(e)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(token)
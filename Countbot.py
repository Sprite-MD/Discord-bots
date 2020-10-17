
import sys
import discord
import asyncio
# discord.__version__

token = '' 

client = discord.Client() # Initiates Client

count = 0
lastUser = 0

@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    
    global count
    global lastUser

    if message.channel.name != 'pic':
        return

    try:
        number = int(message.content)
    except:
        return

    if number == count + 1 and lastUser != message.author.id:
        count += 1
        await message.add_reaction('✅')
        lastUser = message.author.id

        if count == 100: 
            await message.add_reaction('💯')
    
    else:
        count = 0
        await message.add_reaction("❌")
        await message.channel.send(f'{message.author.name} messed up the count. Starting at 1 now')
        lastUser = 0
    

client.run(token)






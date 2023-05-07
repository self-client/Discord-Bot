import discord
from discord.ext import commands,tasks
from itertools import cycle
import os
import asyncio

c_prefix='.$'

client = commands.Bot(command_prefix=f'{c_prefix}',intents=discord.Intents.all())

client.remove_command("help")

TOKEN='MTA2NDUxNjgxNjI3NTI1NTM1Nw.G09Jxq.ARAL37DFmLTVYKiy4rL3Sq42Zhv4vewZyBtZAs'

@client.event
async def on_ready():
    print(f'{client.user} is online!')
    print('==========================')
    change_status.start()

bot_status = cycle([f'{c_prefix}help','Goenka Tech Fest','created by Goenkan IT Team','idling'])

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

async def load():
    for filename in os.listdir("path_of_the_folder_named_cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())
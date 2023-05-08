import discord 
from discord import app_commands
from discord.ext import commands
import sys

your_user_id=''

class KILL(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('kill.py is ready!')
    
    @commands.command()
    @commands.is_owner()
    async def kill(self,ctx):
        response = 'The bot processes have been killed'
        await ctx.reply(response)
        print('Bye-Bye!!')
        await self.client.close()
    
    @kill.error
    async def kill_error(self,ctx,error):
        if ctx.author.id != your_user_id:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!!** \n __only the owner of this bot can use it__ <@{your_user_id}>')
        
async def setup(client):
    await client.add_cog(KILL(client))

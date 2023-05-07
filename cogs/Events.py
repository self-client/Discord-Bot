import discord 
from discord.ext import commands
from datetime import datetime

class Events(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Events.py is ready!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        log_channel = discord.utils.get(message.guild.channels, name='log-channel')

        
        event_embed = discord.Embed(title='Message Logged',description='Message\'s content and origin',color=discord.Color.dark_blue())
        event_embed.add_field(name='Message Author:',value=message.author.mention,inline=False)
        event_embed.add_field(name='Channel Origin:',value=message.channel.mention,inline=False)
        event_embed.add_field(name='Message Content:',value=message.content,inline=False)

        await log_channel.send(embed=event_embed)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = discord.utils.get(member.guilds.channel,name='log-channel')

        event_embed =  discord.Embed(title='Arrival Logged',description='**This user landed in the server!**',color=discord.Color.dark_purple())
        event_embed.add_field(name='User Joined:',value=member.mention,inline=False)
        event_embed.add_field(name='User ID:',value=member.id,inline=False)

        await log_channel.send(embed=event_embed)
    
async def setup(client):
    await client.add_cog(Events(client))

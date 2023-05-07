import discord 
from discord import app_commands
from discord.ext import commands

class EMBEDED(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('embed.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def embed(self,ctx):
       
        embed_message = discord.Embed(title="*Rules!*",description=f'{text}',color=discord.Color.random())

        embed_message.set_author(name=f'',icon_url=ctx.guild.icon)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url='')
        embed_message.set_footer(text='',icon_url=ctx.guild.icon)

        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(EMBEDED(client))



text=''' '''
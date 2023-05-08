import discord 
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    async def help(self,ctx):
        command_prefix = '.$'

        help_embed =  discord.Embed(title='Help desk for Goenka Tech Fest',description='All commands for the bot.',color=discord.Color.random())

        help_embed.set_author(name='')
        help_embed.add_field(name=f'**{command_prefix}Ping:**',value='returns the latency of the bot.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}clear msg_count:**',value='Deletes a specified amount of messages.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}kick id/@:**',value='Kicks a user from guild/server.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}ban id/@:**',value='Bans a user from guild/server.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}unban id/@:**',value='Unbans a user from guild/sever.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}UserInfo id/@:**',value='returns the information of a user.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}kill:**',value='Ends the loop cycle of the bot (only for the bot owner)',inline=False)
        help_embed.add_field(name=f'**{command_prefix}RPS(Rock Paper Scissors):**',value='returns rock/paper/scissors',inline=False)
        help_embed.add_field(name=f'**{command_prefix}RNG(Random Number Generator):**',value='returns a random number 0 to 100',inline=False)
        help_embed.add_field(name=f'**{command_prefix}flip_a_coin:**',value='returns a random number 0 to 100',inline=False)
        help_embed.add_field(name='**Auto logg**',value='Setup a channel named log-channel for auto logging to work!',inline=False)
        help_embed.add_field(name='**embed:**',value='to be updated',inline=False)
        help_embed.add_field(name='**Do\'nt Dm the bot**',value='**you will be disapointed**')

        await ctx.reply(embed=help_embed)

async def setup(client):
    await client.add_cog(HelpCommand(client))

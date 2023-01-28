import discord
from discord.ext import commands

class others(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def message(self, ctx):
        await ctx.send("Message")
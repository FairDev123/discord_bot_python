import discord
from discord.ext import commands
import os
import json

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hej(self,ctx,name=None):
        await ctx.send(f"Cześć {name}")
async def setup(client):
    await client.add_cog(Example(client))


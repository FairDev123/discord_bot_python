from discord.ext import commands, tasks
import discord
import os
from datetime import datetime
import json
import asyncio
import random
from itertools import cycle

class Incum(commands.Cog):

    def __init__(self, client):
        self.client = client


async def setup(client):
    await client.add_cog(Incum(client))
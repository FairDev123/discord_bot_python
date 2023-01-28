# [MODULES IMPORT]
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, guild_only
from discord.utils import get
import sqlite3
import random
import math
import time
import requests
import json

intents = discord.Intents().all()
client = commands.Bot(command_prefix='?', intents=intents)
intents.members = True

@client.command()
async def iterator(ctx):
    pass


client.run("MTAzMjM1OTUxMzY3MzcwNzU5MQ.GRP4vp.2VMVbJxzJcRhyrVIJDkPYYEUvXhA3i9vztIViw")
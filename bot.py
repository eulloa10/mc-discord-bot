import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from apiclient.discovery import build


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GCS_DEVELOPER_KEY= os.getenv('GCS_DEVELOPER_KEY')
GCS_CX= os.getenv('GCS_CX')

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='search')
async def show_landscapes(ctx, place):
    
    resource = build("customsearch", "v1", developerKey=GCS_DEVELOPER_KEY).cse()
    result = resource.list(q=f'"Minecraft" + {place}', searchType='image', cx=GCS_CX).execute()
    
    landscape = result['items'][random.randint(0, 9)]["link"]
        
    await ctx.send(landscape)
        
# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

bot.run(TOKEN)


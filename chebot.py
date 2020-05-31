import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import requests
import pyowm



    


client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
    print('**Listo gfe')
        
@client.command()
async def tiempo(ctx,*,args):
    sitio = args
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?id={}&appid={}&lang={}'.format(sitio, weather_api,'es'))
    x = r.json()


    print(x['main'])



client.run(TOKEN)

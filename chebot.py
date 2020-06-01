import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import requests
import json


base_url = 'http://api.openweathermap.org/data/2.5/weather?'


f = open('keys.json',)
discord_token = ''

data=json.load(f)
for i in data['maricon']:
	discord_token = i['discord']
	weather_api_key = i['weather_api_key']

f.close()


client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
    print('**Listo gfe')
        
@client.command()
async def tiempo(ctx,*,args):
    sitio = args
    complete_url = base_url+'q='+sitio+'&appid='+weather_api_key+'&lang=es'

    response = requests.get(complete_url)
    print(complete_url)

    x = response.json()
    weather = x['weather']

    await ctx.message.channel.send(weather[0]['main'])

client.run(discord_token)

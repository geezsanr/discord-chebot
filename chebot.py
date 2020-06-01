import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import requests
import json
from google_images_download import google_images_download  
import random



base_url = 'http://api.openweathermap.org/data/2.5/weather?'
response_image = google_images_download.googleimagesdownload() 
bot = commands.Bot(command_prefix='*')

f = open('keys.json',)
discord_token = ''

data=json.load(f)
for i in data['maricon']:
	discord_token = i['discord']
	weather_api_key = i['weather_api_key']

f.close()


#comandos del bot
@bot.event
async def on_ready():
    print('**Listo gfe')
        
@bot.command()
async def tiempo(ctx,*,args):
    sitio = args
    complete_url = base_url+'q='+sitio+'&appid='+weather_api_key+'&lang=es&units=metric'

    response = requests.get(complete_url)
   

    x = response.json()

    if x['cod'] == '404':
        await ctx.message.channel.send('Gilipollas ese sitio no existe aprende a escribir.')
    print(x)
    weather = x['weather']
    


    embed = discord.Embed(
        title = 'El tiempo en '+sitio,
        description = str(weather[0]['description']).capitalize(),
        colour = discord.Colour.purple()
        )
    embed.add_field(name='Temperatura',value=str(x['main']['temp'])+'°',inline=True)
    embed.add_field(name='Sensación térmica',value=str(x['main']['feels_like'])+'°',inline=True)
    embed.add_field(name='Humedad',value=str(x['main']['humidity'])+'%',inline=True)

    await ctx.message.channel.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(
        colour=member.color,
        timestamp=ctx.message.created_at
        )

    print('**userinfo requested')

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Solicitado por {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=member.id, inline=False)
    embed.add_field(name='Nombre:',value=member.display_name, inline=False)
    embed.add_field(name='Creación de la cuenta:',value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC') ,inline=False)

    await ctx.message.channel.send(embed=embed)

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        colour=discord.Colour.red(),
        timestamp=ctx.message.created_at
        )

    embed.set_author(name=f"Ayudita para - {ctx.author}")
    embed.add_field(name='*tiempo /lugar/',value='Te dice el tiempo de la ciudad que le pases.', inline=False)
    embed.add_field(name='*userinfo /alguien/',value='Te da información del usuario que le pases.', inline=False)

    embed.set_footer(text=f"maricon", icon_url=ctx.author.avatar_url)
    await ctx.message.channel.send(embed=embed)

#funciones
async def chng_pr():
    await bot.wait_until_ready()

    statuses = ['matando judios','oprimiendo minorías','dios no existe','los reyes magos son los padres','*ayuda','deberías estar estudiando']

    while not bot.is_closed():
        status = random.choice(statuses)
        print('**Cambiando actividad')

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(60)




bot.loop.create_task(chng_pr())
bot.run(discord_token)

from dis import disco
from hashlib import new
from operator import le
from pydoc import cli, describe
from re import T
from unicodedata import name
import discord
from discord.utils import get


#크롤링
import bs4
from bs4 import BeautifulSoup
import openpyxl
import time
import asyncio
import os

#음악재생
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import youtube_dl

from discord.ext import commands

client = commands.Bot(command_prefix='.')
TOKEN = os.environ.get('BOT_TOKEN')

@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    game = discord.Game("노래")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command()
async def p(ctx, url):
    channel = ctx.author.voice.channel
    if client.voice_clients == []:
    	await channel.connect()

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = client.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@client.command()
async def g(ctx):
    try:
        await client.voice_clients[0].disconnect()
    except:
        await ctx.send("이미 없습니다")

@client.command()
async def s(ctx):
    if not client.voice_clients[0].is_paused():
        client.voice_clients[0].pause()
    else:
        await ctx.send("이미 멈췄습니다")

@client.command()
async def re(ctx):
    if client.voice_clients[0].is_paused():
        client.voice_clients[0].resume()
    else:
        await ctx.send("이미 재생중입니다")

@client.command()
async def e(ctx):
    if client.voice_clients[0].is_playing():
        client.voice_clients[0].stop()
    else:
        await ctx.send("재생중인 음악이 없음")






client.run(TOKEN)

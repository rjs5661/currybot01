from dis import disco
from email import message
from email.message import Message
from hashlib import new
from operator import le
from pydoc import cli, describe
import queue
from re import T
from unicodedata import name
import discord
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get


#크롤링
import bs4
from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import requests
import openpyxl
import random
import time
import asyncio

#음악재생
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import youtube_dl

#버튼
from discord.ext import commands
from discord_buttons_plugin import  *

client = commands.Bot(command_prefix='.')
TOKEN = "MTAwMTk0NjYxNzA5Nzc2OTAyMA.GqfXyU.rH3-bHqn7Tdw8TMbix8jUZu0N9YXhs4KFq7yWs"

user = []
musictitle = []
song_queue = []
musicnow = []

# def title(msg):
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

#     options = webdriver.ChromeOptions()
#     options.add_argument("headless")

#     chromedriver_dir = r"C:\Discord_Bot\chromedriver.exe"
#     driver = webdriver.Chrome(chromedriver_dir, options = options)
#     driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
#     source = driver.page_source
#     bs = bs4.BeautifulSoup(source, 'lxml')
#     entire = bs.find_all('a', {'id': 'video-title'})
#     entireNum = entire[0]
#     music = entireNum.text.strip()
    
#     musictitle.append(music)
#     musicnow.append(music)
#     test1 = entireNum.get('href')
#     url = 'https://www.youtube.com'+test1
#     with YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(url, download=False)
#     URL = info['formats'][0]['url']

#     driver.quit()
    
#     return music, URL
# def play(ctx):
#     global vc
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     URL = song_queue[0]
#     del user[0]
#     del musictitle[0]
#     del song_queue[0]
#     vc = get(client.voice_clients, guild=ctx.guild)
#     if not vc.is_playing():
#         vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

# def play_next(ctx):
#     if len(musicnow) - len(user) >= 2:
#         for i in range(len(musicnow) - len(user) - 1):
#             del musicnow[0]
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     if len(user) >= 1:
#         if not vc.is_playing():
#             del musicnow[0]
#             URL = song_queue[0]
#             del user[0]
#             del musictitle[0]
#             del song_queue[0]
#             vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    game = discord.Game("노래")
    await client.change_presence(status=discord.Status.online, activity=game)

# @client.command()
# async def a(ctx, *, msg):
#     user.append(msg)
#     result, URLTEST = title(msg)
#     song_queue.append(URLTEST)
#     await ctx.send(result + " 를 재생목록에 추가")

# @client.command
# async def l(ctx):
#     if len(musictitle) == 0:
#         await ctx.send("등록된 노래 없음")
#     else:
#         global Text
#         Text = ""
#         for i in range(len(musictitle)):
#             Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
#         await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip()))

# @client.command()
# async def r(ctx):
#     try:
#         ex = len(musicnow) - len(user)
#         del user[:]
#         del musictitle[:]
#         del song_queue[:]
#         while True:
#             try:
#                 del musicnow[ex]
#             except:
#                 break
#         await ctx.send("목록 삭제 완료")
#     except:
#         await ctx.send("등록된 노래 없음.")

@client.command()
async def p(ctx, *, url):
    global vc
    vc = await ctx.message.author.voice.channel.connect()
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after = lambda e: play_next(ctx))
    else:
        await ctx.send("노래가 재생중입니다")
# @client.command()
# async def 노래(ctx, url):
#     channel = ctx.author.voice.channel
#     if client.voice_clients == []:
#     	await channel.connect()

#     ydl_opts = {'format': 'bestaudio'}
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         URL = info['formats'][0]['url']
#     voice = client.voice_clients[0]
#     voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#     await ctx.channel.purge(limit = 1)

@client.command()
async def g(ctx):
    try:
        await client.voice_clients[0].disconnect()
    except:
        await ctx.send("채널에 이미 없습니다")

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
        await ctx.send("재생중인 음악이 없습니다")






client.run(TOKEN)
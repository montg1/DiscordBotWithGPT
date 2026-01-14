import discord
from discord.ext import commands
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import os
import asyncio
import youtube_dl
import time

# Replace TOKEN with your bot's token
TOKEN = ''

# Replace API_KEY with your YouTube API key
API_KEY = ''

# Set the youtube_dl options
yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

# Set the ffmpeg options
ffmpeg_options = {'options': "-vn"}

# Create a Discord client
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')
voice_clients = {}

@client.event
async def on_message(message):
    # Check if the message is a command to join a voice channel
    if message.content.startswith('!join'):
        # Get the voice channel to join
        voice_channel = message.author.voice.channel
        if voice_channel is not None:
            # Join the voice channel
            await voice_channel.connect()
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')
    # Check if the message is a command to leave a voice channel
    elif message.content.startswith('!leave'):
        # Get the voice channel to leave
        voice_client = message.guild.voice_client
        if voice_client is not None:
            # Leave the voice channel
            await voice_client.disconnect()
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')


    # Check if the message is a command to play a YouTube video
    elif message.content.startswith('!play'):

        # Get the query from the command
        query = message.content.split(' ', 1)[1]
        # Create a YouTube API service
        youtube = googleapiclient.discovery.build(
            'youtube', 'v3', developerKey
            =API_KEY)
        # Search for a video
        search_response = youtube.search().list(
            part='id,snippet',
            q=query,
            type='video',
            maxResults=1
        ).execute()
        # Get the video ID
        video_id = search_response['items'][0]['id']['videoId']

        url = f'https://www.youtube.com/watch?v={video_id}'
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        # Send the video ID to the voice channel
        await message.channel.send(f'https://www.youtube.com/watch?v={video_id}')
        # Get the voice channel to play the video in
        #voice_client = message.guild.voice_client

        voice_client = await message.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client

        if voice_client is not None:
            # Play the video
            print('Playing video')
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
            voice_clients[message.guild.id].play(player)
            print('Video played')
            print(f'url: {url}')
            print(f'https://www.youtube.com/watch?v={video_id}')
            if url == f'https://www.youtube.com/watch?v={video_id}':
                print("True")
            #print(f'url: {url} \n data: {data} \n song: {song} \n player: {player}')
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')

    elif message.content.startswith("!stop"):
        try:
            voice_clients[message.guild.id].stop()
            await voice_clients[message.guild.id].disconnect()
        except Exception as err:
            print(err)

@client.command()
async def greet(ctx):
    await ctx.send("Hello, World!")


# Run the client on the server
client.run(TOKEN)



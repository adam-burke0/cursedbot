#!/usr/bin/python3

import praw
import discord
import asyncio
client = discord.Client()
BOT_TOKEN = ''

# Sets up reddit bot and chooses subreddit

def setup():
    global reddit
    global subreddit
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('copypasta')

# Gets latest submission from r/copypasta and saves the content to a variable

def refresh():
    global var
    for submission in subreddit.new(limit=1):
        var = submission.selftext

# Prints to console when bot connects

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))        

# Sends copypasta to #copypasta chat on Vibestation every 20 minutes

@client.event
async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        global var
        refresh()
        
        #If copypasta is longer than Discord's 2000 character limit then it will wait 10 minutes and refresh
        if len(var) > 1500:
            await asyncio.sleep(600)
            refresh()
        #If copypasta is shorter than 1500 characters then the copypasta gets sent and the timer resets to 20 minutes before retrying    
        elif len(var) < 1500:
            channel = client.get_channel(735108850809569311)
            print('sending message in channel: ' + str(channel))
            await channel.send(var)
            print('sent: ' + var)
            await asyncio.sleep(1200)

# Sets the background_loop function go run in the background
client.loop.create_task(background_loop())

# Brings the bot online and begins the loop
client.run(BOT_TOKEN)

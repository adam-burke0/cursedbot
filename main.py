#!/usr/bin/python3

import praw
import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    global channel
    print('Logged in as {0.user}'.format(client))        
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('copypasta')
def refresh():
    global var
    

@client.event
async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        for submission in subreddit.hot(limit=1):
            var = submission.selftext
        channel = client.get_channel(735108850809569311)
        print('sending message')
        print(channel)
        await asyncio.sleep(2)
        await channel.send(var)
        print('sent: ' + var)
        await asyncio.sleep(5)


client.loop.create_task(background_loop())

client.run('NzM1MDk5MTE2MDE0NjY1NzYx.XxbUcg.wt3fW6gjnwId5CAtmho_bKLQg1k')
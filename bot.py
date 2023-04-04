import os
import discord
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import tasks
import logging
import pytz


load_dotenv()
Token = os.getenv('BotToken')
Server = os.getenv('ServerName')
intents = discord.Intents.none()
intents.guilds = True
intents.guild_messages = True
client = discord.Client(intents=intents)
TeaTimeID = os.getenv('teaTimeId')
TeaTimeChannel = os.getenv('teaTimeChannel')


@client.event
async def on_ready():
    logging.info(f"{client.user} has connected")
    await morningTea.start()


@tasks.loop(minutes=30)
async def morningTea():
    channel = client.get_channel(int(TeaTimeChannel))
    est = pytz.timezone('US/Eastern')
    if datetime.now(est).time().hour == 9 and datetime.now(est).time().minute <= 30:
        await channel.send(f"<@&{TeaTimeID}> C'est l'heure du thé")
client.run(Token)

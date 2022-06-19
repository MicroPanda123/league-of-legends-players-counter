import contextlib
import discord
import time
from discord.ext import tasks
import json
import random
import asyncio
from datetime import datetime
import pytz
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
defaults = config['DEFAULTS']
mode = defaults.get('Mode', 'TEST')

update_time = int(defaults.get('updatetime', 60))
save_time = int(defaults.get('savetime', 300))
save_file = defaults.get('savefile', 'save.json')

token = config[mode].get('token')
main_chat = int(config[mode]['main_chat'])
guild = int(config[mode]['guild'])
matixbot_chat = int(config[mode]['matixbot_chat'])
app = config[mode]['app']

intents = discord.Intents.default()
intents.members = defaults.getboolean('intent.members')
intents.presences = defaults.getboolean('intent.presences')

client = discord.Client(intents=intents)

try:
    with open(save_file, 'r') as f:
        players = json.load(f)
except FileNotFoundError:
    players = {}

global counter
counter = 0

@client.event
async def on_ready():
    print('Ready')
    lack_of_sex.start()
    mb_chat = client.get_channel(matixbot_chat)

    global embed_message
    embed_message = defaults.get('messageid', 0)
    if int(embed_message) == 0:
        embed_message = await mb_chat.send(embed=create_embed())
        config.set('DEFAULTS', 'messageid', str(embed_message.id))
        with open('config.ini', 'w') as cf:
            config.write(cf)
    else:
        embed_message = await mb_chat.fetch_message(embed_message)

@tasks.loop(seconds=1)
async def lack_of_sex():
    global counter 
    global embed_message

    counter += 1
    gildia = client.get_guild(guild)
    for member in gildia.members:
        if member.activities:
            for activity in member.activities:
                with contextlib.suppress(AttributeError):
                    if app in activity.name.lower():
                        players[str(member.id)] = players[str(member.id)] + 1 if str(member.id) in players else 1

    if counter%update_time == 0:
        await embed_message.edit(embed=create_embed())
    if counter%save_time == 0:
        with open(save_file, 'w') as f:
            json.dump(players, f)
    if counter >= 1000000001:
        counter = 1

# print(member.name, activity.name, (datetime.now(tz=pytz.UTC) - activity.created_at.replace(tzinfo=pytz.UTC)).total_seconds())

def create_embed(mx = 10):
    embed = discord.Embed(
        title="Najwięksi gracze lola",
        description=f"Gracze lola, aktualizowane co {update_time} sekund"
    )
    index = 1
    lista = sorted(players.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    # print(lista)
    for loser in lista:
        # print(loser[0])
        member = client.get_user(int(loser[0]))
        embed.add_field(name = f'{index}: {member}', value = f'{int(loser[1]/60/60/24)} {time.strftime("%H:%M:%S", time.gmtime(loser[1]))}', inline=False)
        if index >= mx:
            break
        else:
            index += 1
    return embed

client.run(token)
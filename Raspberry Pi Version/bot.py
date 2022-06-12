#!/usr/bin/python3
import discord, asyncio
from os import system
import shutil
import subprocess

token = "" # ADD YOUR TOKEN HERE
id = "" # ADD YOUR ID HERE

client = discord.Client()

def owo(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("[-] User Logged In: {0} [-]".format(client.user).center(width))
        print("[-] ID = {0}".format(id).center(width))
        print()
    ui()

@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '': # Set custom command to clear messages here!
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'cleardms': ## Clears All DMs
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

@client.event
async def on_message_delete(message):
    if message.author.id == id:
        print(f"Script Deleted = '{message.content}' in {message.channel}")
                 
# Bot Start
client.run(token, bot=False, reconnect=True)
# Disclaimer

**_This bot has the ability to get you banned from discord, yet the chances of this happening are very low. I am not responsible for you getting banned!_**

# Discord-Messages-Deletion-Bot

A straightforward bot that deletes your message based on discord.py's API.

# Table Of Contents - Windows Version
* [Requirements - Windows Version](#requirements-windows-version)
* [Installation - Windows Version](#installation-windows-version)
* [Configuration - Windows Version](#configuration-windows-version)
* [Commands - Windows Version](#commands-windows-version)
* [Startup - Windows Version](#startup-windows-version)
* [License](#license)

# Table Of Contents - Raspberrypi Version
* [Requirements - Raspberrypi Version](#requirements-raspberrypi-version)
* [Installation - Raspberrypi Version](#installation-raspberrypi-version)
* [Configuration - Raspberrypi Version](#configuration-raspberrypi-version)
* [Commands - Raspberrypi Version](#commands-raspberrypi-version)
* [Run 24/7 - Raspberrypi Version](#run-247-raspberrypi-version)
* [License](#license)

## Requirements Windows Version

- [Python](https://www.python.org/downloads)
- [discord.py](https://discordpy.readthedocs.io/en/latest/)

  py -m pip install -U discord.py

## Installation Windows Version

  1. Download the zip file, and extract it to your **desktop**!
  2. Go to [configuration](#configuration-windows-version)!
  
## Configuration Windows Version

  1. Open the bot.py ( windows folder... ) (**Use Notepad or any coding editing software**)
  2. Paste your Discord Token into the token: "HERE" field!
  3. Save the file... CTRL+S
  4. Open the bot.bat file ( windows folder... )
  5. and enjoy it working
  6. how to [use](#commands-windows-version)!
  
## Commands Windows Version 

 Typing **0** and sending it in chat/dm clears all your messages in said channel/dm!
 
 Typing **cleardms** and sending it in chat/dm deletes all messages from every dm!

## Startup Windows Version

  well if you are a noob, and don't have a raspberry pi.. joking
  
  Here is how to run the bot on startup, and 24/7 (terminal window will be open 24/7)
  
  1. Open the bot.bat file in file explorer ( windows folder... )
  2. Right click, press 'create shortcut'
  3. Press the Windows logo key + R, type shell:startup, then select OK. This opens the Startup folder.
  4. Copy and paste the bot.bat shortcut you just made to the startup folder.
  5. Congrats man
  
## Requirements Raspberrypi Version

- [Python](https://www.python.org/downloads)
- [discord.py](https://discordpy.readthedocs.io/en/latest/)

  python -m pip install -U discord.py

## Installation Raspberrypi Version

```
# Clone the repository
git clone https://github.com/josephistired/Discord-Message-Deletion-Bot

# Enter into the directory
cd Discord-Message-Deletion-Bot/Raspberry\ Pi\ Version/

# Change the Configuration - See below
nano bot.py

```

## Configuration Raspberrypi Version

  1. Paste your Discord Token into the token: "HERE" field!
  2. Save the file... CTRL+S THEN CTRL+X
  ```
  3. python Discord-Message-Deletion-Bot/Raspberry\ Pi\ Version/bot.py
  ```
  5. and enjoy it working
  6. how to [use](#commands-raspberrypi-version)!
  
## Commands Raspberrypi Version 

 Typing **0** and sending it in chat/dm clears all your messages in said channel/dm!
 
 Typing **cleardms** and sending it in chat/dm deletes all messages from every dm!

## Run 24/7 Raspberrypi Version

The great thing about a Raspberry Pi is that it can be running 24/7. If you would to run this bot 24/7, you can simply run the following command in the terminal:

```

# Here
nohup python Discord-Message-Deletion-Bot/Raspberry\ Pi\ Version/bot.py


```

# License 

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

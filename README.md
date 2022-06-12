# Disclaimer

This bot has the ability to get you banned from discord, yet the chances of this happening are very low. I am not responsible for you getting banned!

# Discord-Messages-Deletion-Bot

A straightforward bot that deletes your message based on discord.py's API.

## Table Of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Running the Bot 24/7](#24/7-Running)
* [License](#license)

## Requirements

- [Python](https://www.python.org/downloads/release/python-392/) - Version 3.9.2   
- Required for the bot to work:
  - [discord.py](https://discordpy.readthedocs.io/en/latest/)
  python -m pip install -U discord.py
  - [asyncio](https://docs.python.org/3/library/asyncio.html)
  python -m pip install -U asyncio 

## Installation

```

# Clone the repository
git clone https://github.com/josephistired/Discord-Message-Deletion-Bot

# Enter into the directory
cd Discord-Message-Deletion-Bot/Raspberry\ Pi\ Version/

# Change the Configuration
nano bot.py

```

## Configuration

* Please add your token to the `token` field in the bot.py file.
[Article](https://www.androidauthority.com/get-discord-token-3149920/)
Go to the Discord website on your desktop browser and log into your account > Next, press Ctrl + Shift + I (or Cmd + Option + I on Mac) on your keyboard to enter Developer Tools. Click Network from the toolbar at the top. > Reload the tab by pressing F5. > There will be many more values within Network. Type /api into the field marked Filter. From the results below, click library. > Within library, click the Headers tab. Scroll down until you see authorization. This is your Discord token.

* Please add your id to the `id` field in the bot.py file.
[Article](https://www.google.com/search?q=how+to+get+your+discord+account+id&sourceid=chrome&ie=UTF-8)
Go to User Settings > Advanced > enable Developer Mode.
Next, simply right-click your profile picture and select ‘Copy ID’ to copy your User ID.

* Feel free to change the default command to clear messages.
**The Default command is 0 to clear all messages in the channel!**
To simply change it... Edit line 41 in the bot.py file.
if commands[0] == 'PUT COMMAND HERE': 

## 24/7 Running

The great thing about a Raspberry Pi is that it can be ran 24/7. If you would to run this self-bot 24/7, you can simply run the following command in the terminal:

```
nohup python3 Discord-Message-Deletion-Bot/Raspberry\ Pi\ Version/bot.py

```

## License 

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
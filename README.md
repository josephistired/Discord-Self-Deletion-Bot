![discord.py](https://miro.medium.com/max/929/1*B1q9uh0MO_2r9hAXBv88NQ.png)

## Disclaimer

**_This bot has the ability to get your account banned on discord, yet the chances of this happening are very low. I am not responsible for you getting banned!_**

## Discord-SelfBot

A very simple discord bot that deletes your messages based on [discord.py](https://discordpy.readthedocs.io/en/stable/)!

## Prerequisites

- Python 3.10.0 **[Python](https://www.python.org/downloads/release/python-3100/)**
- Discord.py 1.7.3 **[discord.py](https://discordpy.readthedocs.io/en/latest/)**
- Discord Account Token **[Guide](https://www.androidauthority.com/get-discord-token-3149920/)**

  Windows -> py -m pip install -U discord.py==1.7.3

  Raspberry Pi -> pip install -U discord.py==1.7.3

## 🖥️ First Things To Do

```
pip install -U discord.py==1.7.3
git clone https://github.com/josephistired/Discord-SelfBot.git
cd Discord-SelfBot
```

## ✅ Configuration

_Edit the bot.py file._

```py
token = "Place Your Token Here!"

if commands[0] == 'Place Custom Command Here To Clear Messages!':
                    if len(commands) == 1:

if commands[0] == 'Place Custom Command Here To Clear All Dms!':
            for channel in client.private_channels:
```

## 🖥️ Starting The Bot

After editing the bot.py file, simply run the bot.bat program.

_If running this program on a raspberrypi follow all the steps above but to run the bot run the command **nohup python bot.py**!_

## Commands

| Command  | Description                                          | Working                                                      |
| -------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| 0        | Clears all messages in channel the command is ran in | <img src="./Assets/checkmark.gif" width="15%" height="15%"/> |
| cleardms | Clears all of user's dms                             | <img src="./Assets/checkmark.gif" width="15%" height="15%"/> |

## Run on Startup

_Windows Only_

1. Open the bot.bat file in file explorer
2. Right click, press 'create shortcut'
3. Press the Windows logo key + R, type shell:startup, then select OK. This opens the Startup folder.
4. Copy and paste the bot.bat shortcut you just made to the startup folder.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

# ⛔ Disclaimer
Please note that using this bot, even though it is created with discord.py, could result in your Discord account being banned by Discord. According to [Discord](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-), automating normal user accounts outside of the OAuth2/bot API is prohibited and may lead to account termination. By using this bot, you acknowledge and accept that I cannot be held responsible for any consequences that may occur as a result of using this bot, including but not limited to your Discord account being banned. Use of this bot is at your own risk!

# 🤖 Discord-SelfBot
This is a simple Discord bot that utilizes the discord.py library to delete messages sent from you in a Discord Server or Direct Message. The bot can clear all messages in a specific channel or in Direct Messages with a single command, making it easy to clean up cluttered chat history. 

# 🔧 Prerequisites
Before using this bot, it is important to make sure you have the latest version of Python installed on your system, your Discord account token, and most importantly discord.py version 1.7.3, which is not the latest version but newer versions don't allow you to use a user's token instead only a bot token.

* [Python](https://www.python.org/downloads/)
* Discord.py 1.7.3 - Run the command in your terminal. 
   -  Windows -> py -m pip install -U discord.py==1.7.3
   -  Raspberry Pi -> pip install -U discord.py==1.7.3
* [Discord Account Token](https://www.androidauthority.com/get-discord-token-3149920/) **NEVER GIVE YOUR TOKEN TO ANYONE**

# 💫 Getting Started
Now that you have all the required Prerequisites. You can move on to the next steps. By running the commands below.

```
git clone https://github.com/josephistired/Discord-SelfBot.git
cd Discord-SelfBot
```

# ⚙️ Configuration
Once you have cloned the bot to your local machine and have all the necessary prerequisites in place, you must now edit the bot.py file for the bot to work correctly.


```py
token = "Place Your Discord Account Token Here!"

```
### ⚙️ Extra Configuration
Please note that this Discord bot also has additional configuration options available for users who wish to customize their experience beyond the preset commands for clearing messages and Direct Messages. You can edit those by simplying editing the bot.py file.

```py
if commands[0] == 'Place Custom Command Here To Clear Messages!':
                    if len(commands) == 1:

if commands[0] == 'Place Custom Command Here To Clear All Dms!':
            for channel in client.private_channels:
```


# 🎊 Starting The Bot
If you have successfully completed all the previous steps, the bot should now be ready to run. If you are on Windows, you can run the bot by opening the bot.bat file. If you are a raspberrpi, simply run the command **nohup python bot.py**. Once the bot is running, you can enjoy its features! If you encounter any issues, you can create a pull request for help.


# 💬 Commands

| Command  | Description                                          | 
| -------- | ---------------------------------------------------- | 
| 0        | Clears all messages in channel the command is ran in |
| cleardms | Clears all of user's dms                             | 

# 🕑 Run on Startup
The bot is best run on a device that is on 24/7, like a Raspberry Pi. Running the bot on a device that is always on will ensure optimal results. If using Windows, you can set the bot to start on startup by following the steps below.

1. Open the bot.bat file in file explorer
2. Right click, press 'create shortcut'
3. Press the Windows logo key + R, type shell:startup, then select OK. This opens the Startup folder.
4. Copy and paste the bot.bat shortcut you just made to the startup folder.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

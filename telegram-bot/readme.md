<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/telegram-bot"><img width=15% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/telegram-bot/images/logo.png"></a>

# Overview
**Telegram Bot** is a bot that interacts with users on Telegram. This bot can also be used in grouped chats.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Telegram Application Setup](#Section2)<br>
3. [Telegram Bot Setup](#Section3)<br>
4. [Execution](#Section4)<br>
5. [Automation](#Section5)</br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Python
- Telegram Account

<a name=Section2></a>
# 2. Telegram Application Setup

Telegram is a free and open source, cross-platform, cloud-based instant messaging software. This service also provides end-to-end encrypted video calling, VoIP, file sharing and several other features. Below we have mentioned steps to setup an account and getting of API key: 

- Go to https://my.telegram.org/auth and authorize your telegram account with the Confirmation code recieved on your phone.
- Once you are done with the verification of the account, you will be redirected to "Your Telegram Core".
- The API Development tools will contain your App Authentication keys and the configuration.
- Create an App title and its associated Short name and save this configuration down below.
- Always remember that your keys and tokens should be kept secret!

<a name=Section3></a>
# 3. Telegram Bot Setup

- Now, open your telegram account in your web application by scanning the QR code.
- To create a bot you need to use the service of BotFather.
- Search for BotFather in the search bar as shown in the image <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/telegram-bot/images/BotFather.PNG">here</a>.
- Initiate chat with BotFather by executing ```/start``` in the chat bar.
- To create a new bot you need to execute ```/newbot``` in the chat.
- Next, you need to create a new name and a username for you bot.
- On successfuly execution of previous steps you will be issued a bot token as shown in the image <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/telegram-bot/images/Create%20Bot.PNG">here</a>.
- Always remember that your tokens should be kept secret!
- Next, search for your newly created bot in the search bar and start the chat by executing ```/start``` in the chat.
- Now you are all setup for the execution of the notebook and sending messages via bot using Python.


<a name=Section4></a>
# 4. Execution

- Download the Telebot.ipynb and save in a directory on your system.
- Run the jupyter notebook on local server and import all the libraries.
- Next, copy your bot token to the respective areas in the notebook.
- To get the chat id of your account navigate to the web and send a message to your newly create bot.
- Next, we will run a http request over the web to get the chat id of the user.
- Open the web and execute ```https://api.telegram.org/bot<Your Bot Token>/getUpdates```.
- You will get a JSON response as shown in the image <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/telegram-bot/images/Get%20Updates.PNG">here</a>.
- Copy the id from the JSON response received and paste it in the respective location in the notebook.
- Execute the cell and voila! the user will receive message from the bot.
- You can also add the bot to a group and send notifications.
- All you have to do is get the group chat id which can be retireved directly from the URL.
- Click on your telegram group on the web portal after adding bot to the group.
- In the search bar your URL will be something like ```https://web.telegram.org/z/#-1322509665```.
- So, your chat id here will be ```-1322509665``` which you can use to send message in the group.
  
<a name=Section5></a>
# 5. Automation

Users can use this bot to send custom notifications and make a bot that programmatically solves the issues of their customers. 
They can create customized services based on the requirement that can help users in advancing their customer support.

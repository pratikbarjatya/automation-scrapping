<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/whatsapp-bot"><img width=15% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/whatsapp-bot/images/logo.png"></a>

# Overview
**WhatsApp Bot** is a bot that interacts with verified Twilio users on WhatsApp.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Getting of Credentials](#Section2)<br>
3. [Setting Up of WhatsApp Service](#Section3)<br>
4. [Execution](#Section4)<br>
5. [Automation](#Section5)</br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Python
- Flask
- Ngrok
- Twilio Account
- WhatsApp

<a name=Section2></a>
# 2. Getting of Credentials

Twilio is an American cloud communications platform as a service company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs. Below we have mentioned steps to setup an account and getting of API key:

- Signup at Twilio by visiting https://www.twilio.com/try-twilio
- Once you are done with the verification of the account, login back.
- Go to your dashboard and copy your ACCOUNT SID and AUTH TOKEN and save them in your system somewhere safe.
- Always remember that your ACCOUNT SID and AUTH TOKEN should be kept secret!

<a name=Section3></a>
# 3. Setting Up of WhatsApp Service

To navigate to the WhatsApp service of Twilio do as following

```
Messaging > Try it out > Send a WhatsApp message
```

To utilize the service of WhatsApp Twilio you need to use trial phone number issued by twilio for WhatsApp messaging. To send messages with WhatsApp in production, WhatsApp has to formally approve your account. But, that doesn't mean you have to wait to start building. Twilio Sandbox for WhatsApp lets you test your app in a developer environment.

To begin testing, connect to your sandbox by sending a WhatsApp message from your device to <twilio issue number> with the given code. For example,
  
```
join <twilio given code>
```

<a name=Section4></a>
# 4. Execution

- Download the WhatsApp.ipynb and save in a directory on your system.
- Run the jupyter notebook on local server and import all the libraries.
- Next, copy your account sid and authorization token to the respective areas in the notebook.
- Replace your message in the body parameter that you want to send on the verified phone number.
- Execute the cell and voila! your verified user will receive message from the bot.
- To receive the message from the WhatsApp you need to use Flask API.
- In this notebook, the endpoint used to get the message from the verified user on WhatsApp is "/whatsapp".
- Run your Receiving of WhatsApp Messages section and it will start a local server on your system at http://127.0.0.1:5000
- Next, we will use Ngrok to tunnel our local IP to the gloabal IP using the local server port which is 5000 in our case.
- If you haven't download the Ngrok click <a href="https://ngrok.com/download">here</a> and extract it somewhere on your system.
- Now to tunnel you local flask app as global you need to run the following command on your powershell that contains ngrok file.
  
```
PS C:\Users\abc\ngrok-stable-windows-amd64> ./ngrok http 5000
```

- Once you will execute the instruction you will get your gloabl IP as shown below:
  
```
ngrok by @inconshreveable                                   (Ctrl+C to quit)
  
Session Status                online
Session Expires               1 hour, 57 minutes
Version                       2.3.40
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://98fe-2409-4055-2e99-b04c-4835-48f9-5fed-7e0a.ngrok.io -> http://localhost:5000
Forwarding                    https://98fe-2409-4055-2e99-b04c-4835-48f9-5fed-7e0a.ngrok.io -> http://localhost:5000
  
Connections                   ttl     opn     rt1     rt5     p50     p90 
                              0       0       0.00    0.00    0.00    0.00  
```

- The global IP in this case is https://98fe-2409-4055-2e99-b04c-4835-48f9-5fed-7e0a.ngrok.io
- The final url in addition to our endpoint will be https://98fe-2409-4055-2e99-b04c-4835-48f9-5fed-7e0a.ngrok.io/whatsapp
- This will be set as a callable in your ```Twilio Sandbox for WhatsApp``` in ```WHEN A MESSAGE COMES IN``` part.
- In the Sandbox Configuration you need to replace your twilio sample callback with your url that you just created.
- Once done with the necessary changes save it and send a message to your WhatsApp bot.
- You will get the message printed that the verified user sent to the bot in your notebook.
  
<a name=Section5></a>
# 5. Automation

Users can use this bot to send custom notifications and make a bot that programmatically solves the issues of their customers. 
They can create customized services based on the requirement that can help users in advancing their customer support.

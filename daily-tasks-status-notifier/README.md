<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/daily-tasks-status-notifier"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/daily-tasks-status-notifier/images/logo.png"></a>

<img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" /> <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" /> <img alt="Trello" src="https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white"/>

# Overview
**Daily Tasks Status Notifier** is a tool for extracting status updates from Trello cards and sending details using email to the specified audience.

# Table of Contents
1. [Trello Setup](#Section1)<br>
  1.1 [Getting of an API Key & Token](#Section11)<br>
  1.2 [Getting of list id from Trello Board](#Section12)<br>
  1.3 [URL Creation](#Section13)<br>  
2. [Gmail Setup](#Section2)<br>
  2.1 [Getting of OAuth2 Client File](#Section21)<br>  
3. [Email Template Setup](#Section3)<br>
4. [Execution](#Section4)<br>
5. [Automation](#Section5)</br>

<a name=Section1></a>
# 1. Trello Setup

<a name=Section11></a>
### 1.1 Getting of an API Key & Token

You can get your API key by logging into Trello and visiting https://trello.com/app-key. 
Be sure to read and agree to Trello Developer Terms of Service. 
Your API key will be clearly labeled at the top of that page.
Your API key should be a 32 character string comprised of random alphanumeric characters. 
Because of the way the authorization flow works, the API key is intended to be publicly accessible. 
An API key by itself doesn't grant access to a user's Trello data. 
However, because API tokens grant access to the user's data, they should be kept secret.
Your users will always see this screen when granting your application access as shown <a href="https://developer.atlassian.com/cloud/trello/guides/rest-api/images/rest-api-auth.png">here</a>. 
The permissions, duration of access, and application name displayed are all configured via the URL parameters. 
More on that at Authorization. But we'll leave everything as is, and click "Allow".
Once you click Allow you'll grant your own app (identified via your API key) access to your account and be redirected to a page that contains the API token.
This token, along with your API key, can be used to read and write for your entire Trello account. Tokens should be kept secret!

<a name=Section12></a>
### 1.2 Getting of list id from Trello Board

You can convert your Trello board into JSON data just by typing .json at the end of the board URL. For visual clarification click <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/daily-tasks-status-notifier/images/trellojsonbefore.PNG">here</a>.
To retrieve the id of the list press CTRL + F and type the list name in the popped-up search bar.
Just before the name of the list, you will see the id of the list. For visual clarification click <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/daily-tasks-status-notifier/images/trellojsonafter.PNG">here</a>. Save this id into your notepad as it will be used later to extract the card details.

<a name=Section13></a>
### 1.3 URL Creation

Now that we have got all the required components, we can move ahead and create a URL that will extract the details from the Trello board list.
The URL consists of 4 components base URL, REST API, API key, and token.

- base URL: https://api.trello.com
- REST API = /1/lists/{id}
- API key = ?key=Paste your API key here
- token = &token=Paste your token here
- URL = base URL + REST API + API key + token

<a name=Section2></a>
# 1. Gmail Setup

<a name=Section21></a>
### 2.1 Getting of OAuth2 Client File

Go to https://console.cloud.google.com/ and then create a new project.
Next, go to the APIs & Services section in the navigation menu and click on Dashboard in the panel.
Then click on ENABLE APIs and SERVICES button and search for Gmail API and enable it for the newly initiated project. 
Once enabled come back to APIs & Services section and go to Credentials section in the panel.
On the top click on CREATE CREDENTIALS and select OAuth client ID. 
A client ID is used to identify a single app to Google's OAuth servers.
Next, you need to choose the application type based on your requirements.
Once you have setup the credentials, download the file from OAuth 2.0 Client IDs area.
You can rename the file to something simple such as client_secret.json as it will be easy to access the file later.
Now go back to the OAuth consent screen on the navigation menu in APIs & Services section and select the user type to external.
Congratulation! you have successfully configured the Gmail API and downloaded the client secret. The file should be kept secret!

<a name=Section3></a>
# 3. Email Template Setup

The template can be customized in any format. Users are allowed to customize the messages in their own way.
Below we have shown a simple email message that can be templatize for sending emails.
For further information about how to templatize the message please check the code present in the jupyter notebook.

```
Hi Receiver,


My Today's Tasks:

• Task 1
• Task 2
• Task 3
• Task 4


Regards,
Sender
```

<a name=Section4></a>
# 4. Execution

- Download the Daily Tasks Status Notifier.ipynb and Google.py file and save in a directory on your system.

- Next, copy your client secret file that you downloaded in section 2.1 in the same directory.
 
- Run the jupyter notebook on local server and import all the libraries including the Google.py file.

- You can either create your own message template or by default it will use the above mentioned message template.
 
- Next, complete your <a name=Section13>URL Creation</a> for extracting data from the cards present in the list on your Trello board.

- The first execution will require manual user authorization over the web browser once the notebook cell is executed.

- Click Allow for all the privileges and a file (token_gmail_v1.pickle) will downloaded in your directory.

- And at the same time you will send the message to the concerned person specified in the code.

- If you want to reply to the same email for updates then you must have the thread id.

- The thread id can be retrieved from the execution of second cell in the notebook which by default outputs it.


<a name=Section5></a>
# 5. Automation

Users can automate the entire process using a small server and Airflow application. 
The notebook can be transformed into a python script which then can be used to create DAGs.
These DAGs can be scheduled at specific interval of time over the server.
This will help in get rid of sending information individually to your senior ups. 

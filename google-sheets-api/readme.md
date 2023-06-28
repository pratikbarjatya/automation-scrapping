<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/google-sheets-api"><img width=15% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/google-sheets-api/images/logo.png"></a>


# Overview
**Google Sheets API** lets you read, write, and format Google Sheets data with your preferred programming language.

# Table of Contents
1. [Requirements](#Section1)<br> 
2. [Getting of OAuth2 Client File](#Section2)<br> 
3. [Execution](#Section3)<br>
4. [Automation](#Section4)</br>

<a name=Section1></a>
# 1. Requirements

- To execute the code, you must meet the following requirements:

- Google Account with Enabled Billing
- Python
- Ezsheets python library

<a name=Section2></a>
# 2. Getting of OAuth2 Client File

- Go to https://console.cloud.google.com/ and then create a new project. 
- Next, go to the APIs & Services section in the navigation menu and click on ```Dashboard``` in the panel. 
- Then click on ```ENABLE APIs and SERVICES``` button and search for Gmail API and enable it for the newly initiated project. 
- Once enabled come back to APIs & Services section and go to Credentials section in the panel. 
- On the top click on ```CREATE CREDENTIALS``` and select OAuth client ID. 
- A client ID is used to identify a single app to Google's OAuth servers. 
- Next, you need to choose the application type based on your requirements (preferred ```Desktop app```). 
- Once you have setup the credentials, download the file from OAuth 2.0 Client IDs area. 
- You can rename the file to something simple such as ```credentials-sheets.json``` as it will be easy to access the file later. 
- Now go back to the OAuth consent screen on the navigation menu in APIs & Services section and select the user type to external. 
- Congratulation! you have successfully configured the Gmail API and downloaded the client secret. The file should be kept secret!

<a name=Section3></a>
# 3. Execution

- Download the GSheetsBook.ipynb and Google.py file and save in a directory on your system.
- Next, copy your client secret file that you downloaded in section 2 in the same directory.
- Run the jupyter notebook on local server and import available the libraries.
- You will be navigated to the authorize your google application in your web browser.
- Once you have authorized your Google Sheets application and Google drive application move back to the notebook.
- You are now ready to use the functions to perform manipulation over the Google spreadsheets using Python.
- You can try several manipulations as shown in the notebook such as read/write, download the spreadsheets, etc.

<a name=Section4></a>
# 4. Automation

- You can use the Google Sheets API to manipulate several spreadsheets altogether at the same time.
- This will perform parallel manipulation over the spreadsheets and save the execution time.
- You can also use some scheduling of these manipulating of tasks using a small server and Airflow application. 
- The notebook can be transformed into a python script which then can be used to create DAGs. 
- These DAGs can be scheduled at specific interval of time over the server. 

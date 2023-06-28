<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/programmable-voice-notifier"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/programmable-voice-notifier/images/logo.png" width="150px" height="150px"></a>

<!-- <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" /> <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" /> <img alt="Trello" src="https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white"/> -->

# Overview
**Programmable Voice Notifier** is a tool to make programmable voice calls to the target audience.

# Table of Contents
1. [Getting of SID and Authorization Token](#Section1)<br>
2. [Verification of Caller IDs](#Section2)<br>
4. [Execution](#Section3)<br>
5. [Automation](#Section4)</br>

<a name=Section1></a>
# 1. Getting of SID and Authorization Token

Twilio is an American cloud communications platform as a service company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs. Below we have mentioned steps to setup an account and getting of API key:

- Signup at Twilio by visiting https://www.twilio.com/try-twilio
- Once you are done with the verification of the account, login back.
- Go to your dashboard and copy your ACCOUNT SID and AUTH TOKEN and save them in your system somewhere safe.
- Always remember that your ACCOUNT SID and AUTH TOKEN should be kept secret!
- Next, in the PHONE NUMBER area get a new trial number that you will use to make an API call.

<a name=Section2></a>
# 2. Verification of Caller IDs

- To make an API call for your voice application, you need to verify the caller IDs of the target users.
- Click on the Phone Numbers in the left side of the panel and expand Manage section inside it.
- Next, click on the Verified Caller IDs and a new section will appear on the right side of the screen.
- Now add your target users by verifying their phone numbers.

<a name=Section3></a>
# 3. Execution

- Download the Voice Notebook.ipynb and save it in a directory on your system.
- Run the jupyter notebook on your local server and import the available library.
- Replace your account_sid, auth_token, your voice message, your Twilio issued number, and the target phone number.
- Once done, execute the cell, and voila, your audience received a call.
- They can press the button on their phone to get the voice message sent by you.

<a name=Section4></a>
# 4. Automation

Users can automate the entire process using a small server and Airflow application. The jupyter notebook can be used as a reference to create a python script. The developer can create a DAG out of this script. This DAG can run at a specific interval of time over the server. This application can help the audience to receive a reminder along with the information of the task.

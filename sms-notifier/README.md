<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/sms-notifier"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/sms-notifier/images/logo.gif" width="150px" height="150px"></a>

<!-- <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" /> <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" /> <img alt="Trello" src="https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white"/> -->

# Overview
**SMS Notifier** is a tool for sending text notifications over the phones to the specified audience.

# Table of Contents
1. [Fast2SMS Setup](#Section1)<br>
2. [SMS Template Setup](#Section2)<br>
4. [Execution](#Section3)<br>
5. [Automation](#Section4)</br>

<a name=Section1></a>
# 1. Fast2SMS Setup

Fast2SMS is an online platform for sending SMS to anyone. They offer DLT SMS, Bulk SMS, Quick SMS, and many other services. One of the good thing about using Fast2SMS is the development API. Moreover, they offer 10 free SMS everyday. Below we have mentioned steps to setup Fast2SMS account and getting of API key:

- Signup at Fast2SMS by visiting https://www.fast2sms.com/
- Once you are done with the verification of the account, login back.
- Go to Dev API in the left panel as shown <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/sms-notifier/images/devpage.PNG">here</a>.
- Go to API Key tab and copy your API.
- Always remember that your API key should be kept secret!

<a name=Section2></a>
# 2. SMS Template Setup

The template can be customized in any format. Users are allowed to customize their SMS except that the sender ID will always remain as TXTIND. Users are allowed to create a message at a max of 200 characters. Below we have shown a simple SMS template for Project Deadline:

```
Project Name : <Your Project Name>
Project deadline : Date & time

Note: Check email for more details.
```

<a name=Section3></a>
# 3. Execution

- Download the SMS Notifications.ipynb and save it in a directory on your system.
- Run the jupyter notebook on your local server and import the available library.
- Replace your message, add phone numbers (comma separated without space) and your API key.
- Once done, execute the cell, and voila, your audience received an SMS.

<a name=Section4></a>
# 4. Automation

Users can automate the entire process using a small server and Airflow application. 
The notebook can be transformed into a python script which then can be used to create DAGs.
These DAGs can be scheduled at specific interval of time over the server.
This will help in get rid of sending SMS to your audience manually. 

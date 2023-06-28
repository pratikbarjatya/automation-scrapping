<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/text-to-speech"><img width=20% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/text-to-speech/images/logo.png"></a>

# Overview
**Speech-to-Text** is a tool for generating audio files from the raw text data.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Google Vision Setup](#Section2)<br>
    2.1 [Project & API Setup](#Section21)<br>
    2.2 [Getting of Service Account File](#Section22)<br>
3. [Execution](#Section3)<br>
4. [Automation](#Section4)<br>

<a name=Section1></a>
# 1. Requirements

- To execute the code you must met with the following requirements:
    - Google Account with enabled billing
    - Service Account File
    - google-cloud-texttospeech: ```pip install google-cloud-texttospeech```

- **Note:** You can use 4 million characters per month for free. Check pricing <a href="https://cloud.google.com/text-to-speech/pricing">here</a>.


<a name=Section2></a>
# 2. Google Text-to-Speech Setup

<a name=Section21></a>
### 2.1 Project & API Setup

- To get a service account file you need to create a new project at https://console.cloud.google.com/. 
- Go to APIs and Services and click on <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/image-text-extractor/images/enabling-apis.PNG">ENABLE APIS AND SERVICES</a> button. 
- Search for Cloud ```Text-to-Speech API``` and click on ```ENABLE```.

<a name=Section22></a>
### 2.2 Getting of Service Account File

- To create a service account file go to Credentials page in ```APIs & Services``` from the navigation menu. 
- Click on ```CREATE CREDENTIALS``` button and select Service account from the dropdown. 
- You will be redirected to the ```IAM & Admin``` section. 
- Add service account details and click on ```CREATE AND CONTINUE```. 
- Select a role of ```Owner``` from Role dropdown and click on continue. 
- For the next part, click on ```Done``` as it is optional part. 
- Now select your service account that you just created from Service Accounts and navigate to ```KEYS``` tab. 
- Click on ```ADD KEY``` and select ```Create new key```. 
- Choose the Key type and click on ```CREATE```. 
- It will download the service account file in your system as JSON.
- Rename this file as service_account.json as it will be used later on.

<a name=Section3></a>
# 3. Execution

- Download the Text-to-Speech.ipynb and save in a directory on your system.
- Copy the service account file that you downloaded from section 2.2.
- Run the jupyter notebook on local server and import all the libraries.
- Next, you have to initialize the workspace environment with the service account file.
- Initialize the raw text for which you wish to generate the audio format file.
- You can always choose voice options from the generated voices list for your audio file.
- After executing the cell, the audio file will be available in your workspace directory.

<a name=Section4></a>
# 4. Automation

- Users can automate the entire process using a small server and Airflow application. 
- The notebook can be transformed into a python script which then can be used to create DAGs.
- These DAGs can be scheduled at specific interval of time over the server.
- This will help in get rid of extracting text from the machine model that is trained on a small sized text files.
- This prototype further can be used to integrate with your social media groups such as Whatsapp, Telegram, Slack, etc.

<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/image-text-extractor"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/image-text-extractor/images/logo.png"></a>

# Overview
**Image Text Extractor** is a tool for extracting text from local and remote images.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Google Vision Setup](#Section2)<br>
  2.1 [Project & API Setup](#Section21)<br>
  2.2 [Getting of Service Account File](#Section22)<br>
  2.3 [Getting of an API Key](#Section22)<br>
3. [Execution](#Section3)<br>
4. [Automation](#Section4)<br>

<a name=Section1></a>
# 1. Requirements

To execute the code you must met with the following requirements:
- Google Account with enabled billing
- Service Account File
- API key
- Images (local or remote)


**Note:** You can predict 1000 images free of cost per month. Check pricing <a href="https://cloud.google.com/vision/product-search/pricing">here</a>.


<a name=Section2></a>
# 2. Google Vision Setup

<a name=Section21></a>
### 2.1 Project & API Setup

To get a service account file you need to create a new project at https://console.cloud.google.com/. Go to APIs and Services and click on <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/image-text-extractor/images/enabling-apis.PNG">ENABLE APIS AND SERVICES</a> button. Search for <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/image-text-extractor/images/cloud-vision-api.PNG">Cloud Vision API</a> and click on ENABLE. Next, you need to create credentials to use the API.

<a name=Section22></a>
### 2.2 Getting of Service Account File

To create a service account file go to Credentials page in APIs & Services from the navigation menu. Click on CREATE CREDENTIALS button and select Service account from the dropdown. You will be redirected to the IAM & Admin setion. Add service account details and click on CREATE AND CONTINUE. Select a role of Owner from Role dropdown and click on continue. For the next part, click on Done as it is optional part. Now select your service account that you just created from Service Accounts and navigate to KEYS tab. Click on  ADD KEY and select Create new key. Choose the Key type and click on CREATE. It will download the service account file in your system as JSON.

<a name=Section23></a>
### 2.2 Getting of an API Key

To get an API key navigate to APIs & Services from the navigation menu. Click on CREATE CREDENTIALS button and select API key. Copy the API key and store it in your notepad for further assitance.

<a name=Section3></a>
# 3. Execution

- Download the Text Detection.ipynb and save in a directory on your system.

- Copy the service account file that you downloaded from section 2.2.

- Run the jupyter notebook on local server and import all the libraries.

- Next, you have to initialize the workspace environment with the service account file and the API key.

- Once the environment is executed, select your image type i.e. local or remote by pressing 1 or 2.

- Next, to send image to the server you need to encode it using b64encode in a JSON format.

- On executing the Getting of Response section you will get a response from the server.

- To extract the text from the response, execute the Text Extraction section and you will get all the text data.

- To validate the success of text extraction you can run the following cell where you will plot the rectangles around the detected text.


<a name=Section4></a>
# 4. Automation

Users can automate the entire process using a small server and Airflow application. 
The notebook can be transformed into a python script which then can be used to create DAGs.
These DAGs can be scheduled at specific interval of time over the server.
This will help in get rid of extracting text from the machine model that is trained on a small set of images.
This prototype further can be used to integrate with your social media groups such as Whatsapp, Telegram, Slack, etc.

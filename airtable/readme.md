<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/airtable"><img width=15% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/airtable/images/logo.png   "></a>

# Overview

**Airtable** is a cloud collaboration service that features of a database but can also be applied to a spreadsheet.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Airtable Setup](#Section2)<br>
    2.1 [API Retrieval](#Section21)<br>
    2.2 [Base ID Retrieval](#Section22)<br>
3. [Execution](#Section3)<br>
4. [Automation](#Section4)<br>

<a name=Section1></a>
# 1. Requirements

- To execute the code you must met with the following requirements:
    - Airtable Account
    - Spreadsheet Files (Excel, CSV, etc.)

- **Note:** 

    - The API is limited to 5 requests per second per base. 
    - If you exceed this rate, you will receive a 429 status code and will need to wait 30 seconds before subsequent requests will succeed.

<a name=Section2></a>
# 2. Airtable Setup

Airtable is a cloud collaboration service headquartered in San Francisco. It was founded in 2012 by Howie Liu, Andrew Ofstad, and Emmett Nicholas. Airtable is a spreadsheet-database hybrid, with the features of a database but applied to a spreadsheet.

<a name=Section21></a>
### 2.1 API Retrieval

- You will get an API key for your account at https://airtable.com/account.
- Please note that the API key is sensitive, and it should be kept secret!

<a name=Section22></a>
### 2.2 Base ID Retrieval

- Each spreadsheet on Airtable is associated with a unique base id.
- To get the base id of a specific spreadsheet, checkout the URL in the address bar of your web browser.
- For example, ```https://airtable.com/appDkIdoz1MG3ucOG/tbllK5uBTpJrT0Wmi/viwoAhj6j1WfsxkZC?blocks=hide```
- In the above URL the string part "```appDkIdoz1MG3ucOG```" is the base id of that spreadsheet.

<a name=Section3></a>
# 3. Execution

- Download the Airtable.ipynb and save in a directory on your system.
- Run the jupyter notebook on local server and import all the libraries.
- Copy the ```API key```, and the ```base id``` of the spreadsheet you wish to interact with, in the respective areas.
- Next, there exist separate section with which you can interact with such as Listing Records, Creating Records, etc.

<a name=Section4></a>
# 4. Automation

- If you are using Airtable API to manipulate several spreadsheets altogether at the same time.
- This will perform parallel manipulation over the spreadsheets and save the execution time.
- You can also use some scheduling of these manipulating of tasks using a small server and Airflow application.
- The notebook can be transformed into a python script which then can be used to create DAGs.
- These DAGs can be scheduled at specific interval of time over the server.

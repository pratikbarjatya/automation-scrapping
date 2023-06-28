<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/stocks-reporter"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/stocks-reporter/images/logo.png"></a>

# Overview
**Stocks Reporter** is a tool for getting stock market data using the help of an API.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Execution](#Section2)<br>
3. [Automation](#Section3)</br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Python
- Libraries such as Flask, Numpy, json, datetime, requests

<a name=Section2></a>
# 2. Execution

- Download the Stocks Reporter.ipynb and stock.py file and save in a directory on your system.
 
- Run the stock.py in either powershell or CMD based on your preference as ```python stock.py```

- A local server will start on your system which will generate a random stock market data that you can fetch using an API call.

- Run the jupyter notebook on local server and import all the libraries in the Stocks Reporter.ipynb file.

- Execute the notebook and your API will run for specific duration of time that you can set inside the notebook.

- Next, based on the threshold set for the change in price value it will send email notifications to the end user.


**Note:** This is a simulation of how one can use stock market APIs which in realtime are very costly.


<a name=Section3></a>
# 3. Automation

Users can automate the entire process using a small server and Airflow application. 
The notebook can be transformed into a python script and along with the stock.py file DAGs can be formed.
These DAGs can be scheduled at specific interval of time over the server.
This will help your end users to stay up to date and time with the profit values that they have gained.

<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/share-market-scrapper"><img width=20% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/share-market-scrapper/images/logo.png"></a>


# Overview
**Share Market Scrapper** is a tool for scrapping stock market data from Google NSE in the form of an API.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Execution](#Section2)<br>
3. [Automation](#Section3)<br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Chrome Webdriver
- Selenium

<a name=Section2></a>
# 2. Execution

- Download the Stock Scrapper.ipynb and save in a directory on your system.
 
- Run the jupyter notebook on local server and import all the libraries in the environment.

- You can change the tiker number for a specific organiation considering it is available to NSE.
 
- Execute the notebook cells and redirect to the http://127.0.0.1:5000/shareprices on your web browser.

- You will get the data in the form of JSON format.


<a name=Section3></a>
# 3. Automation

Users can create and run a separate notebook where they can call this local API using the request method. 
It will give them the data on every update (seconds or minutes) depending upon the refresh rate set by Google. 
Moreover, they can save the data for a specific interval of time such as for the next 4 hours or so.

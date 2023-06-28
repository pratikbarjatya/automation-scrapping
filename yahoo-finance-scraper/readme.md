<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/yahoo-finance-scraper"><img width=10% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/yahoo-finance-scraper/images/logo.png"></a>


# Overview
**Amazon Scraper** is a tool for scrapping yahoo finance data of the last 30 days from current date using Selinium and Beautifulsoup.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Execution](#Section2)<br>
3. [Automation](#Section3)<br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Chrome Webdriver - <a href="https://chromedriver.chromium.org/downloads">Get it here</a>
- Selenium
- Beautifulsoup
- Pandas

<a name=Section2></a>
# 2. Execution

- Download the Yahoo Finance Scraper.ipynb and data and save them in a directory on your system.
- Run the jupyter notebook on the local server and import all the libraries in the environment.
- The data contains ticker names and associated company names which you can load using pandas.
- Let the program execution extract all the data of the last 30 days from the current date.
- Once the process is over, all your data files will be available in the saves directory.
- If you want, you may alter the code and extract a few more details about the process.


<a name=Section3></a>
# 3. Automation

- Users can use this process to extract the data on a daily basis, over a specific interval of time.
- You may use the accumuated data to extract insights out of it by creating dashboards.
- To simplify the data accumualtion, you can perform automation using a small server and Airflow application
- The notebook can be transformed into a python script which then can be used to create DAGs.
- These DAGs can be scheduled at specific interval of time over the server.

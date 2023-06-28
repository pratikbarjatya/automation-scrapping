<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/amazon-scraper"><img width=10% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/amazon-scraper/images/logo.png"></a>


# Overview
**Amazon Scraper** is a tool for scrapping hosted product data over Amazon using Selenium and Beautifulsoup.

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

- Download the Amazon Scraper.ipynb and save it in a directory on your system.
- Run the jupyter notebook on the local server and import all the libraries in the environment.
- You can change the number of pages for which you want to extract the data.
- Specify the product name and let the program execute for a while.
- Once the process is over, you will get the data in the form of CSV format.
- If you want, you may alter the code and extract a few more details about each product.


<a name=Section3></a>
# 3. Automation

- Users can use this process to extract the data on a daily basis, over a specific interval of time.
- You may use the accumuated data to extract insights out of it by creating dashboards.
- To simplify the data accumualtion, you can perform automation using a small server and Airflow application
- The notebook can be transformed into a python script which then can be used to create DAGs.
- These DAGs can be scheduled at specific interval of time over the server.

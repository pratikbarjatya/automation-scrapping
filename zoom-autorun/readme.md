<a href="https://github.com/insaid2018/automation-projects/tree/main/python-codes/zoom-autorun"><img width=15% src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/python-codes/zoom-autorun/images/logo.png"></a>

# Overview
**Zoom Autorun** is an application of zoom GUI automatiion in Windows using python package called PyAutoGUI.

# Table of Contents
1. [Requirements](#Section1)<br>
2. [Task Scheduler Setup](#Section2)<br>
3. [Execution](#Section3)<br>
4. [Automation](#Section4)</br>

<a name=Section1></a>
# 1. Requirements

To execute the code, you must meet the following requirements:

- Python
- Zoom Application
- PyAutoGUI

<a name=Section2></a>
# 2. Task Scheduler Setup

Task Scheduler is a job scheduler in Microsoft Windows that launches computer programs or scripts at pre-defined times or after specified time intervals. Microsoft introduced this component in the Microsoft Plus! for Windows 95 as System Agent. Its core component is an eponymous Windows service.

- Search for Task Scheduler in your Windows 10 platform and click on Create Task on the right side of the navigation pane.
- Set a unique name for your task that you want to schedule and trigger at specific interval of time.
- You may want to configure this task for specific platform such as Windows 10, Windows 7, Windows Server 2008, etc.
- Under Actions tab, click on add a new action and a popup will appear on your screen.
- Under Program/Script: add the path of the python executable installed on your system.
- You can find the complete python path by executing ```where python``` in the Command Prompt.
- Next, copy the complete path of the python script that you want to schedule/trigger and add in the double quotes.
- For example, let's say the complete path is as ```C:\Users\abc\Desktop\My Works\GUI Automation\ZoomAutorun.py```.
- Then the path should be as ```"C:\Users\abc\Desktop\My Works\GUI Automation\ZoomAutorun.py"```.
- Now copy this path and paste in Start in (optional) part in the action to complete the action.
- Save this action and navigate to the Triggers tab to schedule/trigger the task.
- Click on New and specify the needs according to your requirements and save the trigger.
- Next, click on OK to save the task. Congratulation! you have successfully scheduled your python script. 

<a name=Section3></a>
# 3. Execution

- Download the ZoomAutorun.ipynb and ZoomAutorun.py and save in a directory on your system.
- Before finalizing the python script, you can experiment with the notebook to execute the zoom autorun.
- You may want to modify the webinar id in the python script for which you wish to automate the GUI execution.
- Once done experimenting, you can use task scheduler in Windows to schedule your script.


<a name=Section4></a>
# 4. Automation

- There are many possibilities a user can achieve using the power of GUI automation in local system.
- One possible application could be filling of forms automatically using stored data in your system.
- Users can utilize the functionality of GUI automation in local system to automate several repetitive tasks.
- It can save the time and manual intervention of users in some of the tasks that they wish could execute without any efforts.

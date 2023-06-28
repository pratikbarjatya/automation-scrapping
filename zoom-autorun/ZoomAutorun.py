# Importing Libraries
import time
import pyautogui

# Zoom's webinar ID; Example: https://us02web.zoom.us/j/82128916384
webinar_id = '82128916384'

# To check screen coordinates use pyautogui.mouseInfo();
# Windows Search icon coordinates found at 70, 750; may differ system to system.
pyautogui.click(x=70, y=750, duration=0.25)

# Sleep for 2 seconds and then search Zoom application
time.sleep(2)
pyautogui.write(message='Zoom')

# Sleep for 2 seconds and then click Enter key internally
time.sleep(2)
pyautogui.press('Enter')

# Sleep for 2 seconds and then maximize then window
time.sleep(2)
pyautogui.getWindowsWithTitle(title='Zoom')[0].maximize()

# Sleep for 2 seconds and click on Join Meeting option
time.sleep(2)
pyautogui.click(x=535, y=300, duration=0.25)

# Sleep for 2 seconds and click the Meeting ID text box
time.sleep(2)
pyautogui.click(x=570, y=330, duration=0.25)

# Sleep for 4 seconds and then enter the webinar ID
time.sleep(4)
pyautogui.write(message=webinar_id)

# Sleep for 2 seconds and then click Join button
time.sleep(2)
pyautogui.press('Enter')

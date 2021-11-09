import time
from pynput import keyboard as kb
import content as c
import pyautogui as auto
import webbrowser

webbrowser.open(c.url, 1)

time.sleep(c.brLoadTime)  # Delay to open page, login
auto.press('tab')
auto.press('tab')
auto.press('tab')
auto.press('enter')

time.sleep(c.brLoadTime)  # Delay to open page, hc start
auto.press('tab')
auto.press('tab')
auto.write(c.num)

auto.press('tab')

# On campus?
auto.press('enter')
auto.press('tab')
auto.press('tab')

auto.press('tab')

# Status
auto.press('enter')
auto.press('tab')
auto.press('tab')
auto.press('tab')
auto.press('enter')
auto.press('tab')
auto.press('tab')
auto.press('enter')

# Sign and Confirm
auto.press('tab')
auto.press('space')
auto.press('tab')
auto.press('tab')
auto.press('space')
auto.press('tab')
auto.write(c.firstN)
auto.press('tab')
auto.write(c.lastN)

# Finish
auto.press('tab')           
# auto.press('enter')

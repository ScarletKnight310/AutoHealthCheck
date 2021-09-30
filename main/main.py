import time
import os
import content as c
import pyautogui as auto
import webbrowser

os.system("taskkill /im firefox.exe /f")  # clear browser if open
webbrowser.open(c.url, 1)

time.sleep(c.brLoadTime)  # Delay to open page, login
auto.press('tab')
auto.press('tab')
auto.press('tab')
auto.press('enter')

auto.press('f11')
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
auto.press('tab')
auto.press('tab')
auto.press('tab')
auto.write(c.firstN)
auto.press('tab')
auto.write(c.lastN)
auto.moveTo(554, 649)
auto.click()
auto.moveTo(554, 736)
auto.click()

# Finish
auto.press('tab')
auto.press('tab')
auto.press('tab')

auto.press('enter')
auto.press('f11')

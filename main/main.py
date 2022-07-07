import time
import content as c
import pyautogui as auto
import webbrowser

# clicking webpage options, so you don't have to :)
webbrowser.open(c.url, 2)
time.sleep(c.brLoadTime)  # Delay to open page, login

auto.press('right')
auto.write(c.username)
auto.press('tab')
auto.press('right')
auto.write(c.password)
auto.press('tab')
auto.press('enter')

time.sleep(c.brLoadTime)  # Delay to open page, hc start
auto.press('tab')
auto.press('tab')
auto.write(c.num)

auto.press('tab')

# On campus?
if c.onCampusStatus == 0:
    auto.press('enter')
auto.press('tab')
if c.onCampusStatus == 1:
    auto.press('enter')
auto.press('tab')
if c.onCampusStatus == 2:
    auto.press('enter')
auto.press('tab')

# Status
if c.isVacc:
    auto.press('enter')
    auto.press('tab')
else:
    auto.press('tab')
    auto.press('enter')
auto.press('tab')

# ---- Are you sick? (Yes / Yes, but Cleared / No)
if c.isSick == 0:
    auto.press('enter')
auto.press('tab')
if c.isSick == 1:
    auto.press('enter')
auto.press('tab')
if c.isSick == 2:
    auto.press('enter')
auto.press('tab')
auto.press('tab')

# ---- Known exposure to someone with COVID-19 (Yes / Yes, but Cleared / No)
if c.isExposed == 0:
    auto.press('enter')
auto.press('tab')
if c.isExposed == 1:
    auto.press('enter')
auto.press('tab')
if c.isExposed == 2:
    auto.press('enter')
auto.press('tab')
auto.press('tab')

# ---- Tested positive for COVID-19 (Yes / Yes, but Cleared / No)
if c.isPosiTest == 0:
    auto.press('enter')
auto.press('tab')
if c.isPosiTest == 1:
    auto.press('enter')
auto.press('tab')
if c.isPosiTest == 2:
    auto.press('enter')
auto.press('tab')

# Sign and Confirm
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
auto.press('enter')

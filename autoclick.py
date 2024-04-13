#main.py

import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.001
while True:
	while keyboard.is_pressed("f"):
		pyautogui.click()

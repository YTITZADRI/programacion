import pyautogui
import time

cord_x, cord_y = pyautogui.position()
print(cord_x, cord_y)
pyautogui.moveTo(200, 345)
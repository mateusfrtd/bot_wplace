import pyautogui
from time import sleep

pixel = float(input(': '))

for i in range(100):
    pyautogui.moveTo(100+pixel*i)
    sleep(0.5)
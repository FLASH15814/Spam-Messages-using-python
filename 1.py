import pyautogui
import webbrowser 
import time
webbrowser.open("web.whatsapp.com")
time.sleep(30)
for i in range(1000):
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
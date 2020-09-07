import win32api
import pyautogui, time

f = open("file.txt",'r')

win32api.MessageBox(0,'Apos Clicar em "Ok" o Spam vai começar em 5 segundos','')

time.sleep(5.0)

for word in f:
    time.sleep(2.0)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
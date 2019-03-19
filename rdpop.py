import pyautogui
import time

pyautogui.PAUSE = 0.3

#read a list of server FQDNs from a text file
serverFQDNs = open('servers.txt')

#transfer control to Microsoft Remote Desktop

pyautogui.hotkey('command', 'space')
pyautogui.typewrite("Microsoft Remote Desktop")
pyautogui.press('return')
time.sleep(1)

#loop through server FQDNs in the txt file and create RDP records for each

for server in serverFQDNs:
    pyautogui.hotkey('command', 'n')
    pyautogui.typewrite(server)
    pyautogui.press('return')

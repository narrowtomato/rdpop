import pyautogui
import os
import time

#set pyautogui to pause after every function call (otherwise it is too fast for RDP)
pyautogui.PAUSE = 0.4

choice = ''

print('\n\n-----*****WELCOME TO RDPOP*****-----\n')

while True:
    #display menu
    print("1. Run RDPOP")
    print("2. Edit servers.txt")
    print("3. Exit\n")

    choice = input("Enter Selection: ")

    if choice == '1':
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

    elif choice == '2':
        #open servers.txt for editing
        os.system("vim servers.txt")

    elif choice == '3':
        exit()

    else:
        print("Invalid Input")

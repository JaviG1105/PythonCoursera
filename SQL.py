import pyautogui
from time import sleep


def type():
    try:
        print ("prepare cursor in...")
        n = 5
        while n > 0:
            print ("{}..".format(n))
            sleep(1)
            n -= 1
        print ("executing script..")
        x = 0
        for i in range(20): #<<<<< Change this number
        #break the line if the amount of characters exceedes 15 for better view
            if x == 15: 
                pyautogui.press('enter')
                x = 0
            
            #bring number up and add a comma to separate the next number
            pyautogui.press('del')
            pyautogui.press('end')
            pyautogui.press(',')

            #this is for the break line condition above
            x += 1



    except (SystemExit):
            print ("interrupted")

type()

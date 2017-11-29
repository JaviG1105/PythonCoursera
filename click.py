from time import sleep
import pyautogui




def click():

    try:
        print "clicking..."
        x = 0
        while True:
            if x == 0:
                pyautogui.click(500,500)
            else:
                pyautogui.click(700,550)



            if x == 0:
                x += 1
            else:
                x -= 1
            sleep(300)
    except (KeyboardInterrupt, SystemExit):
        print "interrupted"

click()
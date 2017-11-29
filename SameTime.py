from time import sleep
import subprocess
import webbrowser

def openCaff():
    subprocess.Popen(["C:\\Users\\IBM_ADMIN\\Downloads\\caffeine\\caffeine.exe"])

def openATT():
    subprocess.call(["C:\\Program Files (x86)\\AT&T Network Client\\NetClientLauncher.exe"])

def openSTtime():
    subprocess.call(["C:\\Program Files (x86)\\IBM\\Lotus\\Sametime Connect\\rcp\\rcplauncher.exe"])

def openMaximo():
    webbrowser.open('https://mail.notes.na.collabserv.com/verse',new=0)
    sleep(3)
    webbrowser.open('http://158.98.56.180/maximo/ui/login', new=2)



def begin():
    print ("opening programs...")
    
    try:
        openATT()
        print ("AT&T opened.")
    except Exception as e:
        print (e)
    
    n = 50
    while n > 0:
        if str(n)[1:2] == "0":
            print ("{}..".format(n))
        sleep(1)
        n-=1
    
    try:
        openSTtime()
        print ("SameTime opened.")
    except Exception as e:
        print (e)

    try:
        openMaximo()
        print ("Chrome opened.")
    except Exception as e:
        print (e)
    
    try:
        openCaff()
        print ("caffeine opened.")
    except Exception as e:
        print (e)





begin()























































        # pyautogui.click(65,345)
        # pyautogui.click(65,345)

        # sleep(60)

        # pyautogui.click(65,600)
        # pyautogui.click(65,600)

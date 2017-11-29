from time import sleep
import subprocess
import pyautogui
import clipboard

def openWord():
    subprocess.Popen(["C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])



def outputPDF():
    openWord()
    sleep(5)
    pyautogui.hotkey('ctrl','v')
    sleep(2)
    pyautogui.hotkey('ctrl','s')

    texto = clipboard.paste()
    print (texto[14:22] + ' - Confirmación usuario')
    
    



outputPDF()

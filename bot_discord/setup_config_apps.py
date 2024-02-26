import os
import time
import pygetwindow
import win32com
import win32com.client as wincl

from colorama import Fore, init
RED = Fore.RED
LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
#  BLU = Fore.BLUE  # слишком тёмные цвета
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
#  MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
BLA = Fore.BLACK
init(convert=True) 

def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
        
# создание ярлыка + запуск с него
def create_shortcut(shortcut_name, target_script_path):
    path_to_shortcut = ""  # папка ярлыков
    try:
        shortcut_if_create = pygetwindow.getWindowsWithTitle(shortcut_name)[0]
        shortcut_if_create.moveTo(88, 220)
        shortcut_if_create.resizeTo(849, 327)
    except Exception as e:
        print(f"\r                                               (!o_O) ярлык --> {shortcut_name}\r")
        script_path = target_script_path
        script_directory = os.path.dirname(script_path)
        shortcut_name_link_path = os.path.join(script_directory, path_to_shortcut + shortcut_name + ".lnk")
        if not os.path.isfile(shortcut_name_link_path):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_name_link_path)
            shortcut.TargetPath = "python.exe"
            shortcut.Arguments = script_path
            shortcut.Description = shortcut_name
            shortcut.WorkingDirectory = script_directory
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + shortcut_name)
        exit()

# gun_fire
def gun_fire(x):
    gun1 = "(√•_•)ԅ⌐╦╦═─"
    gun2 = "(√¬_¬)ԅ⌐╦╦═─"
    fire = "‒=═≡Ξ"
    for i in range(1, len(gun1)):
        print("\b"*len(gun1) + gun1[-i:], end='', flush=True)
        time.sleep(0.03)
    for i in range(x):      
        for i in range(1, len(fire)+1):
            print("\r" + gun2 + fire[:i], end='')
            time.sleep(0.005)
        for i in range(1, 15):
            print("\r" + gun2 + " "*i + "_", end='')
            time.sleep(0.01)
        for i in range(1, len(fire)+1):
            print("\r" + gun2 + fire[:i], end='')
            time.sleep(0.005)
        for i in range(1, 15):
            print("\r" + gun2 + " "*i + "─", end='')
            time.sleep(0.01)
        for i in range(1, len(fire)+1):
            print("\r" + gun2 + fire[:i], end='')
            time.sleep(0.005)   
        for i in range(1, 15):
            print("\r" + gun2 + " "*i + "‾" + "\r", end='')
            time.sleep(0.01)    
            print(" "*31 + "\r", end='')      
    for i in range(len(gun1)+1):
        print("\r" + gun1[i:] + " " + "\r", end='')
        time.sleep(0.03)

# пример использования
# create_shortcut("ассистент", os.path.abspath(__file__))

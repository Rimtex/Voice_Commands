print("______________________обработчик ошибок______________________")
import os
import re
import time

import keyboard

"""
import pyautogui
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
app_title.resizeTo(836, 844)
"""

def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)

with open('Discord_bot_g4f.py', 'r', encoding='utf-8') as file:
    data = file.read()
with open('Discord_bot_g4f.py', 'r', encoding='utf-8') as file:
    data_format = file.read()
# захват библиотек
pattern = r"(?<=\bpip install\b)\s+[^'`\"<>\n]*"  # Шаблон для извлечения команды pip install

pip_install_matches = re.findall(pattern, data_format)

print(data)

if pip_install_matches:
    print("______________________требуемые модули______________________")
    for match in pip_install_matches:
        print(match.strip("'`\"<>"))  # Убираем дополнительные символы
        # print("pip install" + match.strip("'`\"<>")) 
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")    

# тест
try:    
    import Discord_bot_g4f
    with open("gpt_code_error.txt", "w", encoding='utf-8') as file_g:
        file_g.truncate()
    input()
except Exception as e:
    error = str(e)
    print(data)
    printt(error)
    if "No module named" in error:
        import_error = error.split("'")[1]    
        printt("\nПопытка установить необходимый модуль\n")
        try:
            os.system(f'pip install --upgrade {import_error}')
            os.startfile("gpt_code_tester.py")  
        except:
            os.startfile("cmd")
            time.sleep(2)
            keyboard.write(f'pip install --upgrade {import_error}')
            keyboard.press("enter")        
    else:        
        with open('gpt_code_error.txt', 'w', encoding='utf-8') as file:
            file.write(error)
        try:  
            os.startfile(f"G4f_action.lnk")
        except FileNotFoundError:   
            os.startfile("G4f_action.py")       
    

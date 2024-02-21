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

with open('gpt_code.py', 'r', encoding='utf-8') as file:
    data = file.read()
with open('gpt_code_format.py', 'r', encoding='utf-8') as file:
    data_format = file.read()
# захват библиотек
pattern = r'```bash\n(.*?)```'
bash_match = re.search(pattern, data_format, re.DOTALL)
if bash_match:
    bash_code = bash_match.group(1)
    pip_install_modules = re.search(r'^.*pip install.*$', bash_code, re.DOTALL)
    if pip_install_modules:
        print(pip_install_modules.group(0))  # Print the matched part of pip install command
    else:
        print("No 'pip install' command found in the Bash code.")
else:
    print("No Bash code enclosed within triple backticks found in the data.")

# тест
try:
    print(data)
    import gpt_code
    with open("gpt_code_error.txt", "w", encoding='utf-8') as file_g:
        file_g.truncate()
    # input()
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
            keyboard.press("")        
    else:        
        with open('gpt_code_error.txt', 'w', encoding='utf-8') as file:
            file.write(error)
        try:  
            os.startfile(f"G4f_action.lnk")
        except FileNotFoundError:   
            os.startfile("G4f_action.py")       



"""   


"""

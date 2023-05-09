# Димас зацени


import os

try:
    import re
    import time
    import psutil
    import pyautogui
    import win32gui
except ImportError:
    print("Trying to Install required modules:")
    os.system('pip install psutil pyautogui win32gui')
    import re
    import time
    import psutil
    import pyautogui
    import win32gui


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    time.sleep(1)


printt("----------------начало теста----------------\n")

printt("\n #: получаем отсортированый список запущенных процессов и их названий: -->\n")

process_list = []
for proc in psutil.process_iter(['name']):
    try:
        # Получаем название процесса
        process_name = proc.info['name']
        process_list.append(process_name)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

unique_process_list = sorted(set(process_list))

print(unique_process_list)

printt("\n # получаем названия открытых приложений: -->\n")


def get_window_titles():
    titles = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))
        return True

    win32gui.EnumWindows(callback, None)
    return titles


print(get_window_titles())
printt(f"\n # число {len(get_window_titles())}\n")

printt("""
 # Discord - развернуть приложение, сделать активным, свернуть 
 
import re

words = "Discord"  # пишем объект окна по его заголовку
re.match(r'^.{0,20}.{0,20}$', words)  # юзаем рематч

import pyautogui
window = pyautogui.getWindowsWithTitle(words)[0]  # получаем значение окна
window.restore()  # Разворачиваем окно
window.activate()  # Делаем окно активным
window.minimize()  # сворачиваем
""")
printt("\n ----->\n")
try:

    words = "Discord"  # пишем объект окна по его заголовку
    re.match(r'^.{0,20}.{0,20}$', words)  # юзаем рематч

    window = pyautogui.getWindowsWithTitle(words)[0]  # получаем значение окна
    window.restore()  # Разворачиваем окно
    time.sleep(1)
    window.activate()  # Делаем окно активным
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("(!o_O) ymom")
    time.sleep(1)
    window.minimize()  # сворачиваем
except Exception as e:
    print(e, f"\n Discord не запущен!")
printt("\n #: дёргаем ассистента\n")
printt("""
assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
assistant.minimize()  # сворачиваем
assistant.restore()  # разворачиваем 
assistant.activate()  # активируем
assistant.moveTo(100, 100)  # двигаем ассистента
assistant.resizeTo(1849, 227)  # настраиваем размер окна
assistant.moveTo(-8, 2)  # двигаем ассистента в угол
assistant.resizeTo(849, 327)  # настраиваем размер окна 
""")
try:
    printt("\n ----->\n")
    assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
    assistant.minimize()  # сворачиваем
    assistant.restore()  # разворачиваем
    assistant.activate()  # активируем
    time.sleep(1)
    assistant.moveTo(100, 100)  # двигаем ассистента
    time.sleep(1)
    assistant.resizeTo(1849, 227)  # настраиваем размер окна
    time.sleep(1)
    assistant.moveTo(-8, 0)  # двигаем ассистента в угол
    time.sleep(1)
    assistant.resizeTo(849, 327)  # настраиваем размер окна
except Exception as ee:
    print(ee, f"\n ассистент не запущен!")
printt("\n #: разворачиваем на хрен все!\n")
printt("""
window_titles = get_window_titles()
for title in sorted(window_titles):
    window = pyautogui.getWindowsWithTitle(title)[0]
    window.minimize()
    window.restore()
    time.sleep(.1)
""")
printt("\n -----> погнали! (⌐■˽■)\n")
window_titles = get_window_titles()
for title in sorted(window_titles):
    window = pyautogui.getWindowsWithTitle(title)[0]
    window.minimize()
    window.restore()
    time.sleep(.1)

printt("\n -----> сворачиваем! (√¬_¬)ԅ⌐╦╦═─ - ═ ≡ Ξ \n")
window_titless = get_window_titles()
for title in sorted(window_titless):
    window = pyautogui.getWindowsWithTitle(title)[0]
    window.minimize()
    time.sleep(.1)

printt("\n -----> хоба (ˇò_ó) \n")
assistant = pyautogui.getWindowsWithTitle('тест')[0]
assistant.restore()  # разворачиваем

printt("\n----------------конец теста----------------")
input("")

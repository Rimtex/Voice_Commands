import re
import time

def printt(pt):
    for char in pt:
        print(char, end='', flush=True)
        time.sleep(0.025)

printt("----------------начало теста----------------")
time.sleep(1)
printt("""
# получаем список запущенных процессов и их названий:
""")
time.sleep(1)
import psutil

process_list = []
for proc in psutil.process_iter(['name']):
    try:
        # Получаем название процесса
        process_name = proc.info['name']
        process_list.append(process_name)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
print(process_list)
time.sleep(1)
printt("""
# получаем названия открытых приложений:
""")
time.sleep(1)
import win32gui


def get_window_titles():
    titles = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))
        return True

    win32gui.EnumWindows(callback, None)
    return titles


print(get_window_titles())


printt("\n# открыть приложение и сделать его активным -> import pyautogui\n")

import pyautogui


printt('\n# Получаем объект окна по его заголовку -> words = "Discord"\n')

words = "Discord"

printt("\n# юзаем рематч -> re.match(r'^.{0,19}.{0,19}$', words)\n")

re.match(r'^.{0,20}.{0,20}$', words)
window = pyautogui.getWindowsWithTitle(words)[0]

printt("\n# Разворачиваем окно -> window.restore()\n")
time.sleep(1)
window.restore()


printt("\n# Делаем окно активным -> window.activate()\n")
time.sleep(1)
window.activate()


printt("\n# сворачиваем -> window.minimize()\n")
time.sleep(1)
window.minimize()

printt("\n# ещё есть куча приколов с -> Win32Window\n")
time.sleep(1)
printt("\n----------------конец теста----------------")
input("")

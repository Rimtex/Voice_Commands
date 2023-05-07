import time


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    time.sleep(1)


printt("----------------начало теста----------------\n")

printt("\n #: получаем список запущенных процессов и их названий:\n")

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

printt("\n # получаем названия открытых приложений:\n")

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
printt("\n # развернуть приложение, сделать активным, свернуть \n")
printt('\n     # Получаем объект окна по его заголовку -> words = "Discord"\n')
words = "Discord"
printt("\n     # юзаем рематч -> re.match(r'^.{0,19}.{0,19}$', words)\n")
import re

re.match(r'^.{0,20}.{0,20}$', words)
printt("\n     # получаем значение окна -> window = pyautogui.getWindowsWithTitle(words)[0]\n")
import pyautogui

window = pyautogui.getWindowsWithTitle(words)[0]
printt("\n     # Разворачиваем окно -> window.restore()\n")
window.restore()
printt("\n     # Делаем окно активным -> window.activate()\n")
window.activate()
printt("\n     # сворачиваем -> window.minimize()\n")
window.minimize()
printt("\n     # ещё есть куча приколов с -> Win32Window\n")
printt("\n----------------конец теста----------------")
input("")

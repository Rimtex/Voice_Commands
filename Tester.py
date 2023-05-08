import time

import pyautogui


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
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

printt("""
 # развернуть приложение, сделать активным, свернуть 
 
import re

words = "Discord"  # пишем объект окна по его заголовку
re.match(r'^.{0,20}.{0,20}$', words)  # юзаем рематч
import pyautogui

window = pyautogui.getWindowsWithTitle(words)[0]  # получаем значение окна
window.restore()  # Разворачиваем окно
time.sleep(1)
window.activate()  # Делаем окно активным
time.sleep(1)
window.minimize()  # сворачиваем
""")

import re

words = "Discord"  # пишем объект окна по его заголовку
re.match(r'^.{0,20}.{0,20}$', words)  # юзаем рематч
import pyautogui

window = pyautogui.getWindowsWithTitle(words)[0]  # получаем значение окна
window.restore()  # Разворачиваем окно
time.sleep(1)
window.activate()  # Делаем окно активным
time.sleep(1)
window.minimize()  # сворачиваем

printt("\n #: дёргаем ассистента\n")
printt("""
assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
assistant.restore()  # Разворачиваем 
assistant.activate()  # активируем
time.sleep(1)
assistant.moveTo(100, 100)  # двигаем ассистента
time.sleep(1)
assistant.resizeTo(1849, 227)  # настраиваем размер окна
time.sleep(1)
assistant.moveTo(-8, 2)  # двигаем ассистента в угол
time.sleep(1)
assistant.resizeTo(849, 327)  # настраиваем размер окна
""")

assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
assistant.restore()  # Разворачиваем
assistant.activate()  # активируем
time.sleep(1)
assistant.moveTo(100, 100)  # двигаем ассистента
time.sleep(1)
assistant.resizeTo(1849, 227)  # настраиваем размер окна
time.sleep(1)
assistant.moveTo(-8, 2)  # двигаем ассистента в угол
time.sleep(1)
assistant.resizeTo(849, 327)  # настраиваем размер окна

printt("\n----------------конец теста----------------")
input("")

"""
assistant.moveTo(-8, 2)  # двигаем ассистента в угол
assistant_bottomright = pyautogui.getWindowsWithTitle('ассистент')[0].bottomright
#  pyautogui.click(assistant_bottomright)
pyautogui.moveTo(assistant_bottomright)
pyautogui.moveRel(-10, -10)
time.sleep(2.5)
pyautogui.mouseDown()
pyautogui.moveTo(837, 324, duration=0.25)  # настраиваем размер окна
pyautogui.mouseUp()
"""

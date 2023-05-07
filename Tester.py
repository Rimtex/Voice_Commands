import re
import time
print("начало теста")
time.sleep(1)
print("""
# получить список запущенных процессов и их названий:
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
print("""
# в операционной системе Windows на языке Python
# Для получения названий открытых приложений:
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

time.sleep(1)
print("\n# открыть приложение и сделать его активным -> import pyautogui ")
import pyautogui
time.sleep(1)
print('\n# Получаем объект окна по его заголовку -> words = "ассистент"')
time.sleep(1)
words = "ассистент"
print("\n# юзаем рематч -> re.match(r'^.{0,19}.{0,19}$', words)")
time.sleep(1)
re.match(r'^.{0,20}.{0,20}$', words)
window = pyautogui.getWindowsWithTitle(words)[0]
print("\n# Разворачиваем окно -> window.restore()")
time.sleep(1)
window.restore()
time.sleep(1)
print("\n# Делаем окно активным -> window.activate()")
time.sleep(1)
window.activate()
time.sleep(1)
print("\n# сворачиваем -> window.minimize()")
time.sleep(1)
window.minimize()
time.sleep(1)
print("\n# ещё есть куча приколов с -> Win32Window ")
time.sleep(1)
input("\nконец теста")

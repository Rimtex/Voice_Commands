# раздупление приложений


import os

try:
    import time
    import pyautogui
except ImportError:
    print("Trying to Install required modules:")
    os.system('pip install pyautogui')
    import time
    import pyautogui


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    time.sleep(1)


print("---------------- приложения ----------------\n")

# Получаем список всех окон на рабочем столе
windows = pyautogui.getAllWindows()
# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    if window.title:  # если у окна есть заголовок
        print(f"{i + 1}. {window.title}")  # выводим номер и заголовок окна
        time.sleep(.02)  # ждем 0.02 секунды
windows = pyautogui.getAllWindows()  # получаем список всех окон на рабочем столе
printt(" введите номер для: \n")
printt(" --> minimize + restore --> \n")
while True:
    app_number = int(input(""))  # задаем номер приложения
    app_title = windows[app_number - 1].title  # получаем заголовок приложения с заданным номером
    printt(app_title + "\n")  # выводим заголовок на экран
    app = pyautogui.getWindowsWithTitle(app_title)[0]  # получаем объект окна с заданным заголовком
    app.minimize()  # сворачиваем окно
    app.restore()  # разворачиваем окно

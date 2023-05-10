# ну типа вот но зачем


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
        time.sleep(0.012)
    time.sleep(0.5)


print("---------------- приложения ----------------\n")

# Получаем список всех окон на рабочем столе
windows = pyautogui.getAllWindows()
# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    if window.title:  # если у окна есть заголовок
        print(f"{i + 1}. {window.title}")  # выводим номер и заголовок окна

printt("\n #: разворачиваем приложение"
       "\n #: Получаем позицию и размеры выбранного приложения"
       "\n #: активируем приложение"
       "\n --> Введите номер приложения:\n")

while True:
    try:
        app_number = int(input(""))  # задаем номер приложения
        if app_number != "":
            app_title = windows[app_number - 1].title  # получаем заголовок приложения с заданным номером
            # printt(app_title + "\n")  # выводим заголовок на экран
            app = pyautogui.getWindowsWithTitle(app_title)[0]  # получаем объект окна с заданным заголовком
            app.minimize()  # сворачиваем окно
            app.restore()  # разворачиваем окно
            size = app._getWindowRect()
            printt(f" {app.title}: {size}\n")
            app.activate()
    except Exception as e:
        print(e)

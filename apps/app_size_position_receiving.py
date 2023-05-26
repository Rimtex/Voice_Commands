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
        time.sleep(0.005)


print("---------------- pyautogui - № ----------------\n")

# Получаем список всех окон на рабочем столе
windows = pyautogui.getAllWindows()
# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    if window.title:  # если у окна есть заголовокчто за фигня
        print(f"{i + 1}. {window.title}")  # выводим номер и заголовок окна

print("\n №._getWindowRect()"
      "\n Извлекает размеры ограничивающего прямоугольника указанного окна"
      "\n Размеры даны в экранных координатах относительно левого верхнего угла экрана"
      "\n :выводит функцию для размещения")
printt("\n введите номер приложения:\n")

while True:
    try:
        app_number = int(input(" "))  # задаем номер приложения
        if app_number != "":
            app_title = windows[app_number - 1].title  # получаем заголовок приложения с заданным номером
            # printt(app_title + "\n")  # выводим заголовок на экран
            app = pyautogui.getWindowsWithTitle(app_title)[0]  # получаем объект окна с заданным заголовком
            # app.minimize()  # сворачиваем окно
            # app.restore()  # разворачиваем окно
            # app.activate()
            size = app._getWindowRect()
            printt(f"{app_title}\n")
            printt(f"{size}\n")
            printt(f" app_title = pyautogui.getWindowsWithTitle('{app_title}')[0]\n")
            printt(f" app_title.moveTo" f"{size.left, size.top}\n")
            printt(f" app_title.resizeTo" f"({size.right - size.left}," f"{size.bottom - size.top})\n")
    except Exception as e:
        print(e)

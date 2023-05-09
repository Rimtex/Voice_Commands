# уличный дэнсер


import os

try:
    import time
    import random
    import pygetwindow
    import pyautogui
except ImportError:
    print("Trying to Install required modules:")
    os.system('pip install psutil pyautogui win32gui')
    import time
    import random
    import pygetwindow
    import pyautogui


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    time.sleep(1)


printt("----------------осторожно уличный дэнсер----------------\n")
# Получаем список всех окон на рабочем столе
windows = pygetwindow.getAllWindows()

# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    if window.title:
        print(f"{i + 1}. {window.title}")
        time.sleep(.02)

rdk = ("Right", "Up", "Left", "Down")
random.choice(rdk)
while True:
    printt("\n нажмите энтер для дискотеки\n")
    input("")
    # Обращаемся к каждому непустому окну по порядку
    for i in range(len(windows)):
        window = windows[i]
        # Проверяем, есть ли у окна заголовок
        if window.title:
            # Тут можно делать что-то с непустым окном, например, выводить его заголовок
            print(f"{i + 1}. {window.title}")
            window.minimize()
            time.sleep(.1)
            window.restore()
            time.sleep(.1)
            pyautogui.hotkey('winleft', f'{random.choice(rdk)}')
            time.sleep(.1)
            # time.sleep(.2)
            # pyautogui.hotkey('winleft', f'{random.choice(rdk)}')
            # window.minimize()

    # assistant = pyautogui.getWindowsWithTitle('тест' or 'Tester.py' or 'Python')[0]
    window = pyautogui.getWindowsWithTitle('python')[0]
    window.minimize()
    window.restore()  # разворачиваем
    time.sleep(1)

# printt("\n -----> хоба (ˇò_ó) \n")
# printt("\n----------------конец теста----------------")
# input("")

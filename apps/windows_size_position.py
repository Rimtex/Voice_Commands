import pyautogui


def app_titles_recovery():
    app_restore = {
        # ! размещаем нужные позиции копи пастой

        'ассистент': (-8, 0, 836, 327),
        'Voice_Commands.py': (813, 0, 1450, 1408),
        'DeepL  ': (2048, 0, 520, 1408),
        'Microsoft​ Edge': (-8, 319, 836, 1089)

    }
    return app_restore


# Получаем список всех окон на рабочем столе
windows = pyautogui.getAllWindows()
# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    size = window._getWindowRect()
    if window.title:  # если у окна есть заголовок
        app_title = window.title  # получаем заголовок приложения с заданным номером
        app = pyautogui.getWindowsWithTitle(app_title)[0]  # получаем объект окна с заданным заголовком
        size = app._getWindowRect()
        print(f"        '{app_title}': {size.left, size.top, size.right - size.left, size.bottom - size.top}")

print("\n Enter восстанавливает позиции окон из функции")

# while True:
try:
    app_number = input("")
    app_titles = app_titles_recovery()
    for title, pos in app_titles.items():
        try:
            app_title = pyautogui.getWindowsWithTitle(title)[0]
            app_title.moveTo(*pos[:2])
            app_title.resizeTo(*pos[2:])
        except IndexError:
            print("~", end="")

except Exception as e:
    print(e)

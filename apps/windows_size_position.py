import pyautogui
import os


def load_coordinates_from_file(file_path):
    coordinates = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.endswith(")"):
                parts = line.split('(')
                title = parts[0].strip()
                values = [int(x.strip()) for x in parts[1].strip()[:-1].split(',')]
                if len(values) == 4:
                    coordinates[title] = tuple(values)
    return coordinates


def app_titles_recovery():
    app_restore = load_coordinates_from_file('windows_coordinates.txt')
    return app_restore


# Проверяем существование файла с координатами окон и создаем его при необходимости
coordinates_file_path = 'windows_coordinates.txt'
if not os.path.exists(coordinates_file_path):
    with open(coordinates_file_path, 'w') as file:
        pass  # Создаем пустой файл, если он не существует

print("\n текущие координаты и размеры окон:\n")

# Получаем список всех окон на рабочем столе
windows = pyautogui.getAllWindows()
# Выводим список приложений с их номерами
for i, window in enumerate(windows):
    size = window._getWindowRect()
    if window.title:  # если у окна есть заголовок
        app_title = window.title  # получаем заголовок приложения с заданным номером
        app = pyautogui.getWindowsWithTitle(app_title)[0]  # получаем объект окна с заданным заголовком
        size = app._getWindowRect()
        print(f"{app_title}({size.left}, {size.top}, {size.right - size.left}, {size.bottom - size.top})")

print("\n Enter восстанавливает позиции окон из window_coordinates.txt <- Space Enter ")

while True:
    try:
        app_number = input("")
        if app_number == "":
            app_titles = app_titles_recovery()
            for title, pos in app_titles.items():
                try:
                    app_title = pyautogui.getWindowsWithTitle(title)[0]
                    app_title.moveTo(*pos[:2])
                    app_title.resizeTo(*pos[2:])
                except IndexError:
                    print("~", end="")
        if app_number == " ":
            os.startfile(coordinates_file_path)

    except Exception as e:
        print(e)

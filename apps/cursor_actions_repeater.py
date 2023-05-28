import os
import time
import pyautogui
from pynput import mouse

coordinates_file_path = 'actions_remember.txt'

# Проверьте, существует ли файл с координатами окна, и создайте его при необходимости.
if not os.path.exists(coordinates_file_path):
    with open(coordinates_file_path, 'w') as file:
        pass  # Создать пустой файл, если он не существует


def on_click(x, y, button, pressed):
    if pressed:
        action = 'press'
    else:
        action = 'release'
    timestamp = time.time()
    with open(coordinates_file_path, 'a') as file:
        file.write(f'{timestamp},{x},{y},{action}\n')


def record_actions(duration):
    with mouse.Listener(on_click=on_click) as listener:
        time.sleep(duration)
        listener.stop()


def replay_actions():
    with open(coordinates_file_path, 'r') as file:
        lines = file.readlines()
    prev_timestamp = None
    for line in lines:
        timestamp, x, y, action = line.strip().split(',')
        x, y = int(x), int(y)
        if prev_timestamp:
            time.sleep(float(timestamp) - float(prev_timestamp))
        if action == 'press':
            pyautogui.mouseDown(x, y)
        elif action == 'release':
            pyautogui.mouseUp(x, y)
        prev_timestamp = timestamp


user_input = input("Введите количество секунд для записи действий курсора или Enter, чтобы воспроизвести действия:")

if user_input:
    duration = int(user_input)
    with open(coordinates_file_path, 'w') as file:
        file.write('')  # Clear the file
    print(f"Запись действий для {duration} секунды...")
    record_actions(duration)
else:
    print("Воспроизведение действий из файла " + coordinates_file_path)
    replay_actions()

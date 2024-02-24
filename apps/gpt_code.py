import os
import random

# Получить список всех файлов в папке E:\Muzic
files = os.listdir("E:\\Muzic")

# Выбрать случайный файл из списка
random_file = random.choice(files)

# Открыть случайный файл с помощью программы по умолчанию
os.startfile("E:\\Muzic\\" + random_file)

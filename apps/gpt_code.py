# Импортируем модули
import os
import random

# Получаем список файлов в папке E:\Muzic
files = os.listdir("E:\\Muzic")

# Перемешиваем список
random.shuffle(files)

# Выбираем первый файл
file = files[0]

# Открываем файл
os.startfile("E:\\Muzic\\" + file)

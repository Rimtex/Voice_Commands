"""
```python
"""

import random
import os

# Получить список файлов из директории E:\Muzic
music_directory = "E:\\Muzic"
music_files = os.listdir(music_directory)

# Выбрать случайный файл из списка
random_file = random.choice(music_files)

# Сформировать полный путь к файлу
file_path = os.path.join(music_directory, random_file)

# Запустить выбранный файл
os.startfile(file_path)


"""
```

Этот код сначала получает список файлов из директории `E:\Muzic` с помощью функции `os.listdir()`. Затем он выбирает случайный файл из списка с помощью функции `random.choice()`. Далее он формирует полный путь к файлу с помощью функции `os.path.join()`. Наконец, он запускает выбранный файл с помощью функции `os.startfile()`.
"""
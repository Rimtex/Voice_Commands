import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Настройка размеров изображения
figsize = (6, 6)
dpi = 100
background_color = 'black'  # Установим черный фон для звездного неба

# Размеры солнца и звезды
sun_radius = 0.1
star_radius = 0.02

# Создание фигуры изображения
fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
ax.set_facecolor(background_color)

# Рисование солнца
ax.add_patch(Circle((0.5, 0.5), sun_radius, color='yellow'))

# Генерация случайных координат для звезд
num_stars = 20
star_x = np.random.uniform(0, 1, num_stars)
star_y = np.random.uniform(0, 1, num_stars)

# Рисование звезд
for x, y in zip(star_x, star_y):
    ax.add_patch(Circle((x, y), star_radius, color='white'))

# Границы и текст
ax.axis('off')  # Отключаем оси
ax.set_title("Солнце и звезды", fontsize=16, color='white')

# Показываем изображение
plt.show()

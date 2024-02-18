import pyautogui

# Координаты пятиконечной звезды
star_coords = [(100, 0), (140, 90), (200, 90), (160, 140), (180, 200), (100, 160), (20, 200), (40, 140), (0, 90), (60, 90)]

# Перемещаем курсор по координатам для рисования звезды
pyautogui.moveTo(star_coords[0], duration=1)
for coord in star_coords[1:]:
    pyautogui.dragTo(coord, duration=0.2)

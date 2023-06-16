import pyautogui
from PIL import ImageGrab
import time
import keyboard
title = "работа с выделенными скриншотами: преобразование в текст > копирование в буфер"
# C:\Program Files\Tesseract-OCR   |   eng+rus+ukr


def capture_area():
    start_x, start_y = None, None
    # end_x, end_y = None, None

    while True:
        if keyboard.is_pressed('alt'):
            if start_x is None and start_y is None:
                start_x, start_y = pyautogui.position()
                print(f"Начальная позиция: {start_x}, {start_y}")
            time.sleep(0.1)
        else:
            if start_x is not None and start_y is not None:
                end_x, end_y = pyautogui.position()
                print(f"Конечная позиция: {end_x}, {end_y}")
                break
            time.sleep(0.1)

    left = min(start_x, end_x)
    top = min(start_y, end_y)
    width = abs(end_x - start_x)
    height = abs(end_y - start_y)

    screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))
    screenshot.save("screenshot.png")

    # ! нужно чтобы файл копировался в буфер
    screenshot.show()

    try:
        import pytesseract
        from PIL import Image
        import os
        import pyperclip

        os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
        # Укажите путь к установленному Tesseract OCR, если он отличается от стандартного пути
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Открываем изображение
        image = Image.open("screenshot.png")

        # Преобразуем изображение в текст
        text = pytesseract.image_to_string(image, lang="eng+rus+ukr")

        # Выводим полученный текст
        print(text)

        # Копируем текст в буфер обмена
        pyperclip.copy(text)

        # exit()
        # print("Скриншот сохранен в файл 'screenshot.png' и запущен.")
    except Exception as e:
        print(e, "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe")


def main():
    print(title)
    print(" - Нажмите и удерживайте alt для выбора области скриншота курсором.")
    while True:
        keyboard.wait('alt')  # Блокирует выполнение программы до нажатия клавиши "alt"
        capture_area()  # Вызываем функцию для захвата области скриншота


if __name__ == "__main__":
    main()

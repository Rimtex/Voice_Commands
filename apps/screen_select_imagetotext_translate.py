import imageio
from PIL import ImageGrab
import time
from python_translator import Translator
import os
import keyboard
import pyautogui
import win32com
import win32com.client as wincl

title = "работа с выделенными скриншотами: " \
        "сохранение в png > преобразование в текст > перевод > копирование в буфер > конверт в ICO"
tesseract = "https://github.com/UB-Mannheim/tesseract/wiki"
tesseract_path = r"C:\Program Files\Tesseract-OCR"  # ! путь к установленному Tesseract OCR
lang = "eng+rus+ukr"  # "eng"  ! нужные языки "eng+rus+ukr"
translang = "russian"  # ! перевод eng ua


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
    screen_path = "screenshot.png"
    screenshot.save(screen_path)
    #  screenshot.show()  #  открывает файл

    img = imageio.v3.imread(screen_path)
    imageio.imwrite("screenshot.ico", img)  # создаёт иконку

    try:
        import pytesseract
        from PIL import Image
        import os
        import pyperclip

        # путь к установленному Tesseract OCR, если он отличается от стандартного пути
        os.environ['TESSDATA_PREFIX'] = tesseract_path + r'\tessdata'
        pytesseract.pytesseract.tesseract_cmd = tesseract_path + r'\tesseract.exe'

        # Открываем изображение
        image = Image.open("screenshot.png")

        # Преобразуем изображение в текст
        # text = pytesseract.image_to_string(image)
        text = pytesseract.image_to_string(image, lang)
        print(text)
        pyperclip.copy(f"{text}")
        # переводим полученный текст
        try:
            translator = Translator()
            trans = translator.translate(f"{text}", translang)
            print(trans)
            # pyperclip.copy(f"{trans}")
            screenshot = pyautogui.getWindowsWithTitle("скриншот")[0]
            screenshot.minimize()
            screenshot.restore()
        except Exception as er:
            print(er)

        # Копируем текст в буфер обмена
        # pyperclip.copy(text)

        # exit()
        # print("Скриншот сохранен в файл 'screenshot.png' и запущен.")
    except Exception as er:
        print(er, tesseract)


def main():
    print(title)
    print(" - Нажмите и удерживайте alt для выбора области скриншота курсором.")
    while True:
        keyboard.wait('alt')  # Блокирует выполнение программы до нажатия клавиши "alt"
        capture_area()  # Вызываем функцию для захвата области скриншота


if __name__ == "__main__":
    screen = None
    screenshot_window = "скриншот"
    try:
        screen = pyautogui.getWindowsWithTitle(screenshot_window)[0]
        screen.moveTo(88, 220)
        screen.resizeTo(849, 327)
    except Exception as e:
        print(f"\r                                                   (!o_O) ярлык --> {screenshot_window}\r")
        # Получить путь к текущему скрипту
        script_path = os.path.abspath(__file__)

        # Получить путь к папке, в которой находится скрипт
        script_directory = os.path.dirname(script_path)

        # Проверить наличие ярлыка писатель
        screenshot_window_link_path = os.path.join(script_directory, screenshot_window + ".lnk")
        if not os.path.isfile(screenshot_window_link_path):
            # Создать объект ярлыка
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(screenshot_window_link_path)
            # Установить путь к исходному скрипту в ярлыке
            shortcut.TargetPath = script_path
            # Установить имя ярлыка
            shortcut.Description = screenshot_window
            # Установить рабочую папку
            shortcut.WorkingDirectory = script_directory
            # Сохранить ярлык
            shortcut.Save()
        print(e)
        os.startfile(screenshot_window)
        exit()
    main()

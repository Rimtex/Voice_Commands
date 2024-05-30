import imageio
from PIL import ImageGrab
import time
from python_translator import Translator
import os
import keyboard
import pyautogui
import win32com
import win32com.client as wincl
import webbrowser

""""""
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
app_title.resizeTo(836, 444)
app_title.moveTo(-8, 319)


title = "работа с выделенными скриншотами: " \
        "сохранение в png > преобразование в текст > перевод > копирование в буфер > конверт в ICO"
tesseract = "https://github.com/UB-Mannheim/tesseract/wiki"
tesseract_path = r"C:\Program Files\Tesseract-OCR"  # ! путь к установленному Tesseract OCR
lang = "eng+rus+ukr"  # ! нужные языки "eng+rus+ukr"
translang = "russian"  # ! перевод eng ua


def capture_area():
    start_x, start_y = None, None
    # end_x, end_y = None, None

    while True:
        if keyboard.is_pressed('alt') or keyboard.is_pressed('shift'):
            if keyboard.is_pressed('alt'):
                lang = "rus"
            elif keyboard.is_pressed('shift'):
                lang = "eng"    
            else:   
                lang = "eng+rus+ukr"
            if start_x is None and start_y is None:
                start_x, start_y = pyautogui.position()
                print(f"____________________({start_x}, {start_y})____________________")
            time.sleep(0.1)
        else:
            if start_x is not None and start_y is not None:
                end_x, end_y = pyautogui.position()                
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
        print(f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾({end_x}, {end_y})‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        pyperclip.copy(f"{text}")
        if text != "":
            try:                        
                webbrowser.open('https://www.google.com/search?q=' + text)
                print("G", end='')
            except OSError:
                print( "OSError", end='')
        # переводим полученный текст
        try:
            translator = Translator()
            trans = translator.translate(f"{text}", translang)
            print(f"__________(translator)__________")
            print(trans)
            print(f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            # pyperclip.copy(f"{trans}")
            screenshot = pyautogui.getWindowsWithTitle(app_title_window)[0]
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
    print(" - Нажмите и удерживайте alt или shift для выбора области скриншота курсором.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed('alt'):
                # keyboard.wait('alt')  # Блокирует выполнение программы до нажатия клавиши "alt"
                capture_area()  # Вызываем функцию для захвата области скриншота
            elif keyboard.is_pressed('shift'):                
                # keyboard.wait('shift')  # Блокирует выполнение программы до нажатия клавиши "alt"
                capture_area()  # Вызываем функцию для захвата области скриншота


if __name__ == "__main__":
    main()

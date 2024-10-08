import tkinter as tk
import pyautogui
import keyboard
from PIL import ImageGrab, Image
import time
from python_translator import Translator
import pytesseract
import os
import pyperclip

from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
app_title.resizeTo(836, 444)
app_title.moveTo(-8, 319)

tesseract = "https://github.com/UB-Mannheim/tesseract/wiki"
tesseract_path = r"C:\Program Files\Tesseract-OCR"  # Путь к установленному Tesseract OCR
lang = "eng+rus+ukr"  # Нужные языки для распознавания текста
translang = "russian"  # Язык перевода текста

print("SHIFT: преобразование в текст > копирование в буфер > перевод") 
class RectangleDrawer:
    def __init__(self, root):
        self.root = root

        # Получаем размеры экрана
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")  # Устанавливаем размер окна по всему экрану
        self.root.attributes('-topmost', True)  # Окно на переднем плане
        self.root.attributes('-transparentcolor', 'black')  # Прозрачный фон

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_point = None
        self.rectangle = None

        self.root.bind('<Escape>', self.exit_program)
        self.update_rectangle()

    def update_rectangle(self):
        if keyboard.is_pressed('shift'):
            if self.start_point is None:
                self.start_point = pyautogui.position()  # Запоминаем точку начала

            current_point = pyautogui.position()  # Текущая точка
            self.draw_rectangle(self.start_point, current_point)
        else:
            if self.start_point is not None:
                self.capture_area(self.start_point, pyautogui.position())  # Снимок выделенной области
            self.start_point = None  # Сброс при отпускании Shift
            self.clear_rectangle()

        self.root.after(10, self.update_rectangle)  # Обновляем каждые 10 миллисекунд

    def draw_rectangle(self, start, end):
        self.clear_rectangle()
        self.rectangle = self.canvas.create_rectangle(
            start[0], start[1], end[0], end[1], outline="red", width=2
        )

    def clear_rectangle(self):
        if self.rectangle:
            self.canvas.delete(self.rectangle)
            self.rectangle = None

    def exit_program(self, event=None):
        self.root.quit()

    def capture_area(self, start, end):
        left = min(start[0], end[0])
        top = min(start[1], end[1])
        right = max(start[0], end[0])
        bottom = max(start[1], end[1])

        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        screenshot.save("screenshot.png")
        self.process_image()

    def process_image(self):
        try:
            # Настройка Tesseract OCR
            os.environ['TESSDATA_PREFIX'] = tesseract_path + r'\tessdata'
            pytesseract.pytesseract.tesseract_cmd = tesseract_path + r'\tesseract.exe'

            # Открываем изображение
            image = Image.open("screenshot.png")

            # Преобразуем изображение в текст
            text = pytesseract.image_to_string(image, lang=lang)
            print(f"Распознанный текст:\n{text}")

            # Копируем текст в буфер обмена
            pyperclip.copy(text)

            # Переводим текст
            translator = Translator()
            translated_text = translator.translate(text, translang)
            print(f"Переведённый текст:\n{translated_text}")

        except Exception as e:
            print(f"Ошибка обработки изображения: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.overrideredirect(True)  # Убираем границы окна
    app = RectangleDrawer(root)
    root.mainloop()


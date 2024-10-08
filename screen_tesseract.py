import tkinter as tk
from colorama import Fore
import pyautogui
import keyboard
from PIL import ImageGrab, Image
from python_translator import Translator
import pytesseract
import os
import pyperclip

tesseract_path = r"C:\Program Files\Tesseract-OCR"  # Путь к установленному Tesseract OCR
lang = "eng+rus+ukr"  # Нужные языки для распознавания текста
translang = "russian"  # Язык перевода текста

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
        self.is_capturing = False  # Флаг захвата
        self.captured_once = False  # Флаг, чтобы избежать повторного захвата

        self.root.bind('<Escape>', self.exit_program)
        self.update_rectangle()

    def update_rectangle(self):
        if self.captured_once:  # Если уже захвачено, игнорируем обновления
            return
        
        if keyboard.is_pressed('shift'):
            if self.start_point is None and not self.is_capturing:
                self.start_point = pyautogui.position()  # Запоминаем точку начала
                self.is_capturing = True  # Начинаем захват

            current_point = pyautogui.position()  # Текущая точка
            self.draw_rectangle(self.start_point, current_point)
        else:
            if self.start_point is not None:
                self.capture_area(self.start_point, pyautogui.position())  # Снимок выделенной области
                self.start_point = None  # Сброс при отпускании Shift
                self.clear_rectangle()  # Очищаем прямоугольник
            self.is_capturing = False  # Завершаем захват

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
            print(f"{Fore.LIGHTGREEN_EX}Распознанный текст:{Fore.WHITE}\n{text}", end='')

            # Копируем текст в буфер обмена
            pyperclip.copy(text)

            # Переводим текст
            translator = Translator()
            translated_text = translator.translate(text, translang)
            print(f"{Fore.LIGHTYELLOW_EX}Переведённый текст:{Fore.WHITE}\n{translated_text}")

        except Exception as e:
            print(f"Ошибка обработки изображения: {e}")
        finally:
            self.clear_rectangle()  # Очищаем прямоугольник
            self.captured_once = True  # Устанавливаем флаг захвата
            self.root.after(100, self.exit_program)  # Завершаем программу через 100 мс после обработки

# Функция для создания и запуска окна захвата экрана
def start_capture():
    root = tk.Tk()
    root.overrideredirect(True)  # Убираем границы окна
    app = RectangleDrawer(root)
    root.mainloop()

# Если файл запущен как основной, то запускается процесс выделения области
if __name__ == "__main__":
    start_capture()


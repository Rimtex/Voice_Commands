import win32con
import win32gui
import re


class WindowMgr:
    """Инкапсулирует некоторые вызовы winapi для управления окнами"""

    def __init__(self):
        """Конструктор"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """Нахождение окна по названию его имени класса"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Переход к win32gui.EnumWindows() для проверки всех открытых окон"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """нахождение окна по его тайтлу согласно заданному параметру в wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """Показ и активация окна один раз если оно было свёрнуто"""
        win32gui.SetForegroundWindow(self._handle)

    def set_background(self):
        """Минимизация окна - сворачивание"""
        win32gui.ShowWindow(self._handle, win32con.SW_MINIMIZE)

    def set_active(self):
        """Показ и полная активация окна"""
        win32gui.ShowWindow(self._handle, win32con.SW_NORMAL)

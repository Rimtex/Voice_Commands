import random
import pyautogui
from colorama import init, Fore, Style
from keyboard_scripts import click_print_cor

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
init(convert=True)


def show_mouse_scripts():  # ! это не функция это просто для копипасты скриптов
    x = 1280  # координаты центра
    y = 720  # координаты центра
    pyautogui.moveTo(1256, 777)
    pyautogui.click()
    pyautogui.click(button='right')
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    screen_width, screen_height = pyautogui.size()  # получение размеров монитора
    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=0.25)  # координаты центр экрана
    pyautogui.moveTo(2439, 1420, duration=0.25)  # перемещает курсор мыши в абсолютные координаты на экране
    pyautogui.moveRel(2439, 1420, duration=0.25)  # двигаться относительно его текущего положения
    pyautogui.moveRel(100, 0)  # вправо сто пикселей
    pyautogui.moveRel(0, 100)  # вниз сто пикселей
    pyautogui.moveRel(-100, 0)  # влево сто пикселей
    pyautogui.moveRel(0, -100)  # вверх сто пикселей
    pyautogui.click(0, 9)  # координаты ассистента  на рабочем столе
    pyautogui.click(411, 1439)  # координаты ассистента  на панели задач
    # words_num_dict = vocabulary.numbers()  # импортируем словарь цифр
    # num = words_num_dict[words[2]]  # получаем третье слово в виде числа
    # pyautogui.moveRel(num*100, 0)  # вправо num* сто пикселей
    pyautogui.mouseDown(408, 11)
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 3, duration=0.25)
    pyautogui.moveRel(-200, 0, duration=0.20)
    pyautogui.moveRel(+400, 0, duration=0.20)
    pyautogui.moveRel(-200, -200, duration=0.20)
    pyautogui.moveRel(0, 400, duration=0.20)
    pyautogui.moveRel(0, -200, duration=0.20)


print("(*ᴥ*)\n", end='')
click_print_cor(411, 1439)
screen_width, screen_height = pyautogui.size()
pyautogui.mouseDown(408, 11)  # (408, 11)
pyautogui.moveTo(screen_width / 2, screen_height / 3, duration=0.25)
for i in range(6):
    pyautogui.moveRel(-200, 0, duration=0.15)
    pyautogui.moveRel(+400, 0, duration=0.15)
    pyautogui.moveRel(-200, -200, duration=0.15)
    pyautogui.moveRel(0, 400, duration=0.15)
    pyautogui.moveRel(0, -200, duration=0.15)
    print(f"\n{random.choice(colors)}"
          f"          {random.choice(colors)}иисус      ¯\\_('-')_/¯{random.choice(colors)}"
          f"      господь!   {random.choice(colors)}господь!{random.choice(colors)}"
          f"      ¯\\_('-')_/¯      {random.choice(colors)}христос{Style.RESET_ALL}")
pyautogui.mouseUp(408, 11)

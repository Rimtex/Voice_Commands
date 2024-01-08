import pyautogui
import time

print("-----Автокликер-----")

def main():
    print("Введите интервал в секундах:")
    interval = float(input())

    print("Наведите курсор в нужное место")
    time.sleep(5)  # Даем 2 секунды на перемещение фокуса на нужное место

    # Получаем текущие координаты мыши
    x, y = pyautogui.position()
    print(f"Запомненные координаты: x={x}, y={y}")

    try:
        while True:
            # Повторяем клик в сохраненных координатах с введенным интервалом            
            pyautogui.click(x, y)
            time.sleep(interval)
            print(".", end="", flush=True)
    except KeyboardInterrupt:
        print("Прервано пользователем.")

if __name__ == "__main__":
    main()

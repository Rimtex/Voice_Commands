import time
import winsound

# Устанавливаем время будильника
alarm_time = time.time() + 1800  # 1800 секунд = 30 минут

print("Будильник установлен на 30 минут.")

while True:
    current_time = time.time()
    if current_time >= alarm_time:
        print("Время будильника!")
        winsound.Beep(1000, 1000)  # Звук будильника
        break
    time.sleep(1)  # Проверяем каждую секунду

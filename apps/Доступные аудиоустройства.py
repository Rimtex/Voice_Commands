import sounddevice as sd


def print_audio_devices():
    devices = sd.query_devices()
    print("Доступные аудиоустройства:")
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device['name']} - {device['max_input_channels']} входных канала(-ов)")


# Вывести информацию о доступных устройствах
print_audio_devices()
input()

"""
1. Microsoft Sound Mapper - Input - 2 входных канала(-ов)
2. Микрофон (Realtek(R) Audio) - 2 входных канала(-ов)
3. Microsoft Sound Mapper - Output - 0 входных канала(-ов)
4. Динамики (Realtek(R) Audio) - 0 входных канала(-ов)
5. Realtek Digital Output (Realtek - 0 входных канала(-ов)
6. AG271QG4 (NVIDIA High Definitio - 0 входных канала(-ов)
7. Первичный драйвер записи звука - 2 входных канала(-ов)
8. Микрофон (Realtek(R) Audio) - 2 входных канала(-ов)
9. Первичный звуковой драйвер - 0 входных канала(-ов)
10. Динамики (Realtek(R) Audio) - 0 входных канала(-ов)
11. Realtek Digital Output (Realtek(R) Audio) - 0 входных канала(-ов)
12. AG271QG4 (NVIDIA High Definition Audio) - 0 входных канала(-ов)
13. Realtek ASIO - 2 входных канала(-ов)
14. Realtek Digital Output (Realtek(R) Audio) - 0 входных канала(-ов)
15. AG271QG4 (NVIDIA High Definition Audio) - 0 входных канала(-ов)
16. Динамики (Realtek(R) Audio) - 0 входных канала(-ов)
17. Микрофон (Realtek(R) Audio) - 2 входных канала(-ов)
18. Output (NVIDIA High Definition Audio) - 0 входных канала(-ов)
19. Стерео микшер (Realtek HD Audio Stereo input) - 2 входных канала(-ов)
20. Микрофон (Realtek HD Audio Mic input) - 2 входных канала(-ов)
21. Speakers (Realtek HD Audio output) - 0 входных канала(-ов)
22. SPDIF Out (Realtek HDA SPDIF Out) - 0 входных канала(-ов)
23. Лин. вход (Realtek HD Audio Line input) - 2 входных канала(-ов)
24. Headphones (Realtek HD Audio 2nd outpuтакt) - 0 входных канала(-ов)
"""

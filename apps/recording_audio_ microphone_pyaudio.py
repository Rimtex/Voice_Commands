import pyaudio
import wave
import keyboard
from pydub import AudioSegment

filename = "recorded_audio.wav"  # Имя файла для записи


def record_audio():
    frames = []
    chunk = 1024
    channels = 2
    format_type = pyaudio.paInt16
    rate = 48000

    p = pyaudio.PyAudio()

    stream = p.open(format=format_type,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    # print("Нажмите 'Q' для начала записи и 'W' для завершения записи.")
    print("Нажмите 'W' для завершения записи.")
    # keyboard.wait("Q")
    print("Начало записи...")

    while not keyboard.is_pressed("W"):
        data = stream.read(chunk)
        frames.append(data)

    print("Завершение записи.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames


def save_to_file(frames):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
    wf.setframerate(48000)
    wf.writeframes(b''.join(frames))
    wf.close()


def increase_volume(input_file, output_file, gain):
    sound = AudioSegment.from_wav(input_file)
    louder_sound = sound + gain
    louder_sound.export(output_file, format="wav")


# Запуск записи по нажатию кнопки
audio_frames = record_audio()

# Сохранение записи в файл
if audio_frames:
    print("Сохранение записи в файл...")
    save_to_file(audio_frames)

    # Увеличение громкости
    increase_volume(filename, filename, 10)  # 10 - это уровень увеличения громкости (можете изменить)

    print(f"Запись сохранена в файл {filename}")

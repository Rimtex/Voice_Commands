import os
import torch
import sounddevice as sd

"""
ipython
omegaconf
pydub
PyYAML
torch
torchaudio
"""

models_urls = ['https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
               'https://models.silero.ai/models/tts/en/v3_en.pt']

if not os.path.exists("silero_models"):
    os.mkdir("silero_models")
    os.makedirs("silero_models/ru", exist_ok=True)
    os.makedirs("silero_models/en", exist_ok=True)

model_ru = 'silero_models/ru/model.pt'
model_en = 'silero_models/en/model.pt'

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = model_ru

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file(models_urls[0],
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

sample_rate = 48000
speaker = 'kseniya'  # aidar, baya, kseniya, xenia, eugene
en_speaker = 'en_6'


def speaker_silero(text):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate)
    sd.play(audio, blocking=True)


"""
- Кто там? - Я! - Я? Да ты гонишь!
"""
if __name__ == '__main__':
    while True:
        sss = '32131- Кто там? - Я! - Я? Да ты гонишь!'
        speaker_silero(sss)

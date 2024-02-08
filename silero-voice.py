import os
from gtts import gTTS
from io import BytesIO
import torch
import sounddevice as sd
import soundfile as sf

"""
ipython
omegaconf
pydub
PyYAML
torch
torchaudio
"""


def speaker_gtts(text):
    lang = os.getenv("LANG")
    with BytesIO() as f:
        gTTS(text=text, lang=lang, slow=False).write_to_fp(f)
        f.seek(0)
        data, fs = sf.read(f)
        sd.play(data, fs, blocking=True)


models_urls = ['https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
               'https://models.silero.ai/models/tts/en/v3_en.pt']

if not os.path.exists("silero_models"):
    os.mkdir("silero_models")
    os.makedirs("silero-models/ru", exist_ok=True)
    os.makedirs("silero-models/en", exist_ok=True)

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


def speaker_silero(text):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate)
    sd.play(audio, blocking=True)

"""
- Кто там? - Я! - Я? Да ты гонишь!
"""

while True:
    sss = input('1')
    if sss != '':
        speaker_silero(sss)

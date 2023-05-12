#  ggml-gpt4all-l13b-snoozy.bin
from colorama import init, Fore  # , Style
from pygpt4all.models.gpt4all import GPT4All

init(convert=True)
model = GPT4All('./ggml-gpt4all-l13b-snoozy.bin')

# Код ошибки 0xc0000005 проблемы с памятью.
"""
#: состав словаря из названий моделей
file_list = os.listdir("models\\")
bin_files = [f for f in file_list if f.endswith(".bin")]
labels = []  # словарь названий ярлыков
for bin_file in bin_files:
    full_path = os.path.join("models\\", bin_file)
    label = bin_file
    labels.append(label)
for i, label in enumerate(labels):
    print(f"{i + 1}. {label}")
"""


def generate_response(user_input):
    # n_predict = len(userinput)  #: предикт можно добавлять пробелами
    response = model.generate(user_input)  # , n_predict=n_predict
    return response


#  Интерактивный диалог
#  Вы можете настроить интерактивный диалог, просто оставив model переменную активной:
while True:
    try:
        userinput = input(Fore.LIGHTYELLOW_EX + "You: " + Fore.RESET)
        if userinput == '':
            continue
        print(f"AI:", end='')
        for token in generate_response(userinput):
            print(f"{token}", end='', flush=True)
        print(Fore.RESET)
    except KeyboardInterrupt:
        break

    """   
       
tell funny jokes                                            расскажи смешные шутки
make a guide.                                               составь гайд
build for the game.                                         билд для игры
for a quick start                                           для быстрого старта
from this description                                       из этого описания
read this description.                                      зачитай это описание         
in the style of                                             в стиле 
gangsta rap!.                                               гангста рэпа      
        
python:                                                     питон:
in my code:                                                 в моем коде:
change and improve:                                         изменить и улучшить:
to make it work, you need to do something like this         чтобы работала нужно как-то так сделать
need to make the following script work!:                    необходимо заставить работать следующий скрипт!
to make it work you need to do something like this          чтобы работала нужно как-то так сделать
i want to call the print which is written in the function   хочу вызывать принт, который написан в функции
like this -                                                 примерно таким образом - 
I need to improve a function:                               мне нужно улучшить функцию:
remove unnecessary lines of code:                           убрать лишние строки кода:
can you do something to improve this code:                  можешь как-то улучшить этот код:   

a script for a cartoon                                      сценарий для мультфильма  
Rick and Morty :                                            Рик и Морти 
About Rick and Morty making a courgette but talking others out of it. 
О том, как Рик и Морти делают кабачок, но отговаривают других.    
    """
# n_predict - количество символов влияет на длину генерируемого текста
# ! нужно выяснить на что влияют другие настройки
"""
    :param model_path: путь к модели gpt4all
    :param prompt_context: глобальный контекст взаимодействия
    :param prompt_prefix: префикс подсказки
    :param prompt_suffix: суффикс подсказки
    :param log_level: уровень логирования, по умолчанию установлен на INFO
    :param n_ctx: LLaMA контекст
    :param seed: случайное семя
    :param n_parts: LLaMA n_parts
    :param f16_kv: использовать fp16 для кэша KV
    :param logits_all: вызов llama_eval() вычисляет все логиты, а не только последний.
    :param vocab_only: загружать только словарь, без весов
    :param use_mlock: заставить систему хранить модель в оперативной памяти
    :param embedding: только режим встраивания
    """

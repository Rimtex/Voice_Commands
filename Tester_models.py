from pygpt4all.models.gpt4all import GPT4All
from colorama import Fore, Style, init

RED = Fore.RED
LYE = Fore.LIGHTYELLOW_EX
CYA = Fore.CYAN
LGR = Fore.LIGHTGREEN_EX
SRA = Style.RESET_ALL
init(convert=True)

#  ggml-gpt4all-j-v1.3-groovy.bin
#  ggml-gpt4all-l13b-snoozy.bin

# n_predict - количество символов влияет на длину генерируемого текста
# ! нужно выяснить на что влияют другие настройки

model = GPT4All('./gpt4all/pygpt4all/models/ggml-gpt4all-l13b-snoozy.bin')


def new_text_callback(text: str):  # функция печати текста по символам
    print(LGR + text, end="")


def generate_response(userinput):
    n_predict = len(userinput)  #: чем длиннее запрос - тем больше предикт
    response = model.generate(userinput, n_predict=n_predict, new_text_callback=new_text_callback)
    # response = model.generate(user_input, n_predict=55, n_threads=8)
    return response


while True:
    user_input = input(LYE + "\nyou: " + SRA)
    generate_response(user_input)

    """
a script for a cartoon                    сценарий для мультфильма  
Rick and Morty :                          Рик и Морти 
About Rick and Morty making a courgette but talking others out of it. 
О том, как Рик и Морти делают кабачок, но отговаривают других.
       
tell funny jokes                          расскажи смешные шутки
make a guide.                             составь гайд
build for the game.                       билд для игры
for a quick start                         для быстрого старта
from this description                     из этого описания
read this description.                    зачитай это описание         
in the style of                           в стиле 
gangsta rap!.                             гангста рэпа      

python:                                              питон:
in my code:                                          в моем коде:
change and improve:                                  изменить и улучшить:
to make it work, you need to do something like this  чтобы работала нужно как-то так сделать
need to make the following script work!:             необходимо заставить работать следующий скрипт!
to make it work you need to do something like this   чтобы работала нужно как-то так сделать
i want to call the print which is written in the function   хочу вызывать принт, который написан в функции
like this -                                          примерно таким образом - 
I need to improve a function:                        мне нужно улучшить функцию:
remove unnecessary lines of code:                    убрать лишние строки кода:
can you do something to improve this code:           можешь как-то улучшить этот код:       
    """

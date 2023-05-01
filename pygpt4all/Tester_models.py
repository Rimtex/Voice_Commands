#  ggml-gpt4all-j-v1.3-groovy.bin
#  ggml-gpt4all-l13b-snoozy.bin


from pygpt4all.models.gpt4all import GPT4All

model = GPT4All('./pygpt4all/models/ggml-gpt4all-l13b-snoozy.bin')

translat = ""  # Объявляем переменную translat в глобальной области видимости


def new_text_callback(text: str):  # (text: str)
    print(text, end="")


#    model.generate("write: script for a cartoon - Rick and Morty:
#    funny joke:  About  Rick and Morty making a mystery  'courgette' but talking others out of it
#    .", n_predict=55, new_text_callback=new_text_callback)

while True:
    def generate_response(user_input):
        response = model.generate(user_input, n_predict=55)
        #  response = model.generate(user_input, n_predict=55, n_threads=8)
        return response

#  user_input = input("you: ")
#  generate_response(user_input)

#  generate_response(user_input)


# model = GPT4All('./pygpt4all/models/ggml-gpt4all-l13b-snoozy.bin')


# print("!!! # вопрос !!! как мне разделить ответы от модели - \n строками")
# model.generate(input('you: '), n_predict=55, new_text_callback=new_text_callback)

#  pip install --upgrade GPT4All_J
from pygpt4all import GPT4All_J

model = GPT4All_J('ggml-gpt4all-j-v1.3-groovy.bin')

#  Интерактивный диалог
#  Вы можете настроить интерактивный диалог, просто оставив model переменную активной:
while True:
    try:
        prompt = input("You: ")
        if prompt == '':
            continue
        print(f"AI:", end='')
        for token in model.generate(prompt):
            print(f"{token}", end='', flush=True)
        print()
    except KeyboardInterrupt:
        break

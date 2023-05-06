#  ggml-gpt4all-l13b-snoozy.bin

from pygpt4all.models.gpt4all import GPT4All

model = GPT4All('ggml-gpt4all-l13b-snoozy.bin')

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

import g4f

"""
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Есть такая штука как «Двигаться дальше». Попробуйте, поможет."}],
    stream=True,
)


bot_responses = []
for message in response:
    bot_responses.append(message)
    if bot_responses:
        print(bot_responses[0])
"""
## Normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Есть такая штука как «Двигаться дальше». Попробуйте, поможет."}],
)  # Alternative model setting

print(response)
# Открываем файл gpt_answer.txt в режиме записи ('w' - write)
with open('gpt_answer.txt', 'w', encoding='utf-8') as file:
    # Записываем содержимое переменной response в файл
    file.write(response)

input()

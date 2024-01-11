
import g4f




# Using automatic a provider for the given model
"""
# Streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True,
)
for message in response:
    print(message, flush=True, end='')
"""

## Normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "1!анекдот про рик и морти"}],
)  # Alternative model setting

print(response)


"""
# Открываем файл gpt_answer.txt в режиме записи ('w' - write)
with open('gpt_answer.txt', 'w', encoding='utf-8') as file:
    # Записываем содержимое переменной response в файл
    file.write(response)
"""

input()

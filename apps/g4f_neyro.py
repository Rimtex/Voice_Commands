import g4f

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": """
     Есть такая штука как «Двигаться дальше». Попробуйте, поможет.
     """}],
    stream=True,
)


bot_responses = []
for message in response:
    bot_responses.append(message)
    if bot_responses:
        print(bot_responses[0])

input()

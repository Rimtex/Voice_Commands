from g4f.client import Client

client = Client()


def ask_gpt(messages: list) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    print(response.choices[0].message.content)
    return response.choices[0].message.content


messages = []
while True:
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    assistant_response = ask_gpt(messages=messages)
    messages.append({"role": "assistant", "content": assistant_response})

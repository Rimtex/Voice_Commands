import g4f


# вызов нейро чата
neyro_model = "gpt_4_turbo"

def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=getattr(g4f.models, neyro_model),
        messages=messages)
    print(response)
    return response


messages = []
while True:
    messages.append({"role": "user", "content": input()})
    messages.append({"role": "assistant", "content": ask_gpt(messages=messages)})

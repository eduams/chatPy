from openai import OpenAI

client = OpenAI(api_key="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")


def conversar(texto):
    resposta = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Suponha que você é um instrutor de Python."},
        {"role": "user", "content": texto},
    ],
    temperature=0.7)
    return resposta.choices[0].message.content


while True:
    prompt = input("Usuário: ")
    resposta_chatgpt = conversar(prompt)
    print("Bot: " + resposta_chatgpt)

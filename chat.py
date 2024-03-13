from openai import OpenAI
import json

client = OpenAI(api_key="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")
 
 
def conversar(texto):
    resposta = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": texto},
    ],
    temperature=0.7)
    return resposta.choices[0].message.content

all_rows = []

with open('code.json') as json_file:
    all_rows = json.load(json_file)

# Agora você pode trabalhar com a lista 'all_rows'
# por exemplo, pode iterar sobre ela e imprimir ou realizar outras operações
prompt = input("Digite o prompt que irá antes do código: ")

# Abra o arquivo JSON em modo de escrita
with open('results.json', 'w') as json_file:
    results = []

    # Loop principal
    for row in all_rows:
        if row == None:
            row = [" "]

        # Crie a prompt concatenando as linhas
        promptfull = prompt.join(row)

        # Obtenha a resposta do ChatGPT
        resposta_chatgpt = conversar(promptfull)

        # Imprima a resposta
        print(resposta_chatgpt)

        # Adicione a resposta à lista de resultados
        results.append({'prompt': promptfull, 'resposta_chatgpt': resposta_chatgpt})

    # Escreva a lista de resultados no arquivo JSON
    json.dump(results, json_file, indent=4)

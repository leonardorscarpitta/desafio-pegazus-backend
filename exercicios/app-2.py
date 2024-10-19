#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

import json

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# Navega por todos os itens do dicionario em formato de JSON nomeado "responsejson"
for key in responsejson["produtos"]:
    if key["nome"] == "Produto B": # Verifica se o nome da chave é "Produto B" para entao armazenar o valor do produto em uma variavel
        preco_produto = key["preço"]
        print(f"O produto B custa R$ {preco_produto}")

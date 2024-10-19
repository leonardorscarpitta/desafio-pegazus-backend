#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

import requests

URL = " https://jsonplaceholder.typicode.com/users"  # Definindo uma variável para endpoint

request_get = requests.get(URL)  # Definindo uma variavel para realizar o metodo de requisição get
request_json = request_get.json()  # Formatando o request para JSON

# Parsing de dados do endereço do usuario - com a chave requerida
for info in request_json:
    name = info["name"]
    user_name = info["username"]
    user_email = info["email"]
    user_street = info["address"]["street"]
    street_number = info["address"]["zipcode"]

    print(f"{name} | {user_name} | {user_email} | {user_street} | {street_number} \n")

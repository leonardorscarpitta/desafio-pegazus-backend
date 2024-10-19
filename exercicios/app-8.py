#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

import requests


def handle_request():
    """
    Função para tratar o endpoint e realizar a contagem de tarefas concluidas e pendentes
    :return: None
    """
    URL = "https://jsonplaceholder.typicode.com/todos"  # Definindo uma variável para endpoint

    request_get = requests.get(URL)  # Definindo uma variavel para realizar o metodo de requisição get
    request_json = request_get.json()  # Formatando o request para JSON

    # Inicializando as variáveis contadoras para os status das tasks
    pending = 0
    concluded = 0

    # Iterar pelo JSON do request
    for key in request_json:
        if key["completed"]: # Verificar se o valor da chave "completed" é igual a true nesse caso não precisamos de um == True
            concluded += 1
        else: # Caso não seja True, será false, então há um incremento no numero de tasks pendentes
            pending += 1

    print(f"Numero de tasks concluídas: {concluded}\nNúmero de tasks pendentes: {pending}")

handle_request() # Chamando a função solicitada

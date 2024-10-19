#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

name_list = ["Lucas", "Léo", "Januario"]  # Criando uma lista com nomes


def fifo_method(fifolist):
    print(f"O nome {fifolist[-1]} foi removido da lista seguindo a metodologia FIFO!")
    fifolist.pop(-1)  # Removendo o item -1 (ultimo) da lista, já que o LIFO diz que o ultimo a entrar é o primeiro a sair


# Criando um painel simples para aplicar a metodologia
while True:
    if len(name_list) == 0:
        print("Lista vazia, encerrando programa")
        break  # Encerrar o programa caso a lista esteja vazia

    print("Nomes na lista: ")

    # Percorrer a lista de nomes para printar os valores
    for name in name_list:
        print(f"- {name}")
    user_type = int(input(f"\nDigite 1 para aplicar a metodologia FIFO na lista - "))
    match user_type:
        case 1:
            fifo_method(name_list)  # Iniciar o
        case _:
            print("Encerrando programa")  # Encerrar o programa caso o usuário digite outro numero

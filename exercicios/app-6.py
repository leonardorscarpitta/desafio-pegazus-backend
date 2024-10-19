#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

indice = 0 # Criando uma variável para facilitar a manipulação dos itens da lista

# Percorrer os nomes da lista para verificar os nomeados como "joao"
for nome in lista:
    if nome == "joao":
        lista.pop(indice) # Remover o nome joao do indice que foi verificado em "nome"
        lista.insert(indice, "maria") # Adicionar o nome "maria" no lugar de joao
    indice += 1 # Para evitar manipular o mesmo indice, incrementar 1 sempre que finalizar a estrutura "for" de repetição

print(lista)

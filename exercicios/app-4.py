#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]
lista_formatada = []

# Percorrendo os itens da lista para retirar os espaços em branco
for nome in lista:
    nome_formatado = nome.strip() # Essa função retira todos os espaços em branco
    lista_formatada.append(nome_formatado)

# Adicionando novos itens conforme solicitado
lista_formatada.append("carlos") # Adiciona um item ao final da lista
lista_formatada.append("josias")
lista_formatada.insert(0, "jose") # Adiciona um item em um indice especifico, no caso o indice 0 (o inicial)
 
print(f"A lista com as modificações solicitadas ficaria da seguinte forma: \n {lista_formatada}")

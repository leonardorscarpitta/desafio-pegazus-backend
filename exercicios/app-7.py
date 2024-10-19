#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

list = [1,2,3,4,5,6,7,8,9,0] # Criando uma lista de numeros inteiros

count = 0 # Criando a variável inicializada em 0 para iterar inicialmente sobre o primeiro item

while count <= 5:
    item_formatado = list[count] # Criando uma variável para definir como o print deve se comportar
    print(item_formatado)
    count += 1 # Assim que o while ocorre uma vez, a variável recebe o incremento de um

codigo_cliente = int(input("Qual o codigo do cliente? "))
soma_alturas = 0
soma_pesos = 0
lista_de_codigos = []
lista_de_pesos = []
lista_de_alturas = []
i = 0
while codigo_cliente != 0:
    i = i + 1
    altura_cliente = float(input("Altura do cliente: "))
    lista_de_alturas.append(altura_cliente)
    peso_cliente = float(input("Peso do cliente: "))
    lista_de_pesos.append(peso_cliente)
    soma_alturas = soma_alturas + altura_cliente
    soma_pesos = soma_pesos + peso_cliente
    codigo_cliente = int(input("Qual o codigo do proximo cliente? "))
    lista_de_codigos.append(codigo_cliente)

media_alturas = soma_alturas / i
media_pesos = soma_pesos / i
print("Media de alturas: {}, Media de pesos: {}".format(media_alturas, media_pesos))
print("Maior altura: {}".format(max(lista_de_alturas)))
print("Maior peso: {}".format(max(lista_de_pesos)))
print("Menor altura: {}".format(max(lista_de_alturas)))
print("Menor peso: {}".format(max(lista_de_pesos)))

print(“Maior altura {} é a do usuário com código {}“.format(maior_altura, lista_de_codigos[maior_altura_posicao])
maior_altura_posicao = lista_de_alturas.index(maior_altura)
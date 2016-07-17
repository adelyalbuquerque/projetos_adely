lista_de_carros = []
lista_km_por_litro = []

print("Comparativo de Consumo de Combustível")

for i in range (1,6):
    print("Veiculo {}:".format(i))
    lista_de_carros.append(input("Nome: ".format(i)))
    lista_km_por_litro.append(float(input("Km por litro: ")))


print("Reltatorio Final:")

for i in range(1,6):
    print("{} - {} - {} - {} litros - R$ {} ".format(i, lista_de_carros[i-1], lista_km_por_litro[i-1],
                                                    round((1000 / lista_km_por_litro[i-1]),2),
                                                    round((1000/ lista_km_por_litro[i-1]) * 2.25),2 ))


x = lista_km_por_litro.index(max(lista_km_por_litro))
menor_consumo = lista_de_carros[x]
print(menor_consumo)

nome_do_atleta = str(input("Qual o nome do atleta? "))
lista_pulos = []
i = 1
for i in range(1,6):
    pulo = float(input("Qual a distancia do salto {}: ".format(i)))
    lista_pulos.append(pulo)
    i = i + 1

print("Atleta: {}".format(nome_do_atleta))
print("Primeiro salto: {}".format(lista_pulos[0]))
print("Segundo salto: {}".format(lista_pulos[1]))
print("Terceiro salto: {}".format(lista_pulos[2]))
print("Quarto salto: {}".format(lista_pulos[3]))
print("Quinto salto: {}".format(lista_pulos[4]))
print("Atleta: {}".format(nome_do_atleta))
print("Saltos: {}".format(lista_pulos))
print("Media de Saltos: {}".format(sum(lista_pulos)/5))


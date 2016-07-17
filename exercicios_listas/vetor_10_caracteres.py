lista_caracteres_consoantes = []
lista_caracteres_vogais = []
i = 1
while i <= 10:
    caracteres = str(input("Insira o caracter {}: ".format(i)))
    if caracteres == "a" or caracteres == "e" or caracteres == "i" or caracteres == "o" or caracteres == "u":
        lista_caracteres_vogais.append(caracteres)
    else:
        lista_caracteres_consoantes.append(caracteres)
    i = i + 1

print(len(lista_caracteres_consoantes))
print(lista_caracteres_consoantes)
pergunta_1 = str(input("Telefonou para a vitima? Sim - S / Nao - N "))
pergunta_2 = str(input("Esteve no local do crime? Sim - S / Nao - N "))
pergunta_3 = str(input("Mora perto da vitima? Sim - S / Nao - N "))
pergunta_4 = str(input("Devia para a vitima? Sim - S / Nao - N " ))
pergunta_5 = str(input("Ja trabalhou com a vitima? Sim - S / Nao - N "))
lista_de_respostas = []
lista_de_respostas.append(pergunta_1)
lista_de_respostas.append(pergunta_2)
lista_de_respostas.append(pergunta_3)
lista_de_respostas.append(pergunta_4)
lista_de_respostas.append(pergunta_5)
if lista_de_respostas.count("S") == 2:
    print("SUSPEITA(O)")
elif lista_de_respostas.count("S") >= 3:
    if lista_de_respostas.count("S") == 3:
        print("CUMPLICE")
    elif lista_de_respostas.count("S") == 4:
        print("CUMPLICE")
    else:
        print("ASSASSINO")
else:
    print("INOCENTE")


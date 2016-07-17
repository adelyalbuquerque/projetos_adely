voto = int(input("OPCOES: 1 - Joao/ 2 - Maria/ 3 - Jose/ 4 - Ana/ 5 - Voto Nulo/ 6 - Voto em Branco/  "
                 "0 - Para sair - QUAL SEU VOTO? "))
lista_de_votos = []
while voto != 0:
    if voto == 1 or voto == 2 or voto == 3 or voto == 4 or voto == 5 or voto == 6:
        lista_de_votos.append(voto)
        voto = int(input("OPCOES: 1 - Joao/ 2 - Maria/ 3 - Jose/ 4 - Ana/ 5 - Voto Nulo/ 6 - Voto em Branco/  "
                         "0 - Para sair - QUAL SEU VOTO? "))
    else:
        print("ERRO. O numero inserido nao esta entre as opcoes, tente novamente: ")
        voto = int(input("OPCOES: 1 - Joao/ 2 - Maria/ 3 - Jose/ 4 - Ana/ 5 - Voto Nulo/ 6 - Voto em Branco/  "
                         "0 - Para sair - QUAL SEU VOTO? "))


my_dict = {i: lista_de_votos.count(i) for i in lista_de_votos}
print(my_dict)

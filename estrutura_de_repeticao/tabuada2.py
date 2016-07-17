numero = input("Insira um numero inteiro: ")
print("Montar tabuada de: {}".format(numero))
multiplicador_inicial = input("Comecar por: ")
multiplicador_final = input("Terminar em: ")
if multiplicador_inicial > multiplicador_final:
    print("ERRO. Numero do comeco eh maior que o numero terminal!")
else:
    print("Vou montar tabuada de {}, comecando em {} e terminando em {}: ".format(numero, multiplicador_inicial,
                                                                         multiplicador_final))
i = numero
for i in range (multiplicador_inicial, multiplicador_final + 1):
    print("{} x {} = {}".format(numero, multiplicador_inicial, numero * multiplicador_inicial))
    multiplicador_inicial = multiplicador_inicial + 1

lista_numeros_inteiros = []
multiplicacao = 1
i = 1
while len(lista_numeros_inteiros) < 10:
    numero = int(input("Insira o numero inteiro: "))
    lista_numeros_inteiros.append(numero)
    multiplicacao = multiplicacao * numero

print(sum(lista_numeros_inteiros))
print(multiplicacao)
print(lista_numeros_inteiros)

numero_inteiro = int(input("Insira um numero inteiro: "))
print("Fatorial de: {}".format(numero_inteiro))
i = 1
fatorial = numero_inteiro * i
while i < numero_inteiro:
    fatorial = fatorial * i
    i = i + 1

print("5! : {}".format(fatorial))




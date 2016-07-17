numero = input("Digite um numero inteiro: ")
while numero != 0:
    if (numero % 1) != 0 and (numero % numero) != 0:
        print("Primo")
    else:
        print("Nao eh primo")


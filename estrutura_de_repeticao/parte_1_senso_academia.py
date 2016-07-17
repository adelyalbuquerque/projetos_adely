lista_de_codigos = []
lista_de_pesos = []
lista_de_alturas = []
lista_de_codigos.append(int(input("Insira o codigo do cliente: ")))
while lista_de_codigos != 0:
    lista_de_pesos.append(float(input("Insira o peso do cliente: ")))
    lista_de_alturas.append(float(input("Insira a altura do clliente: ")))
    proximo_codigo = int(input("Insira o proximo codigo de cliente: "))
    if proximo_codigo != 0:
        lista_de_codigos.append(proximo_codigo)

print(max(lista_de_pesos, lista_de_alturas))
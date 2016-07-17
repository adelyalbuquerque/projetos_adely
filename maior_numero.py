i = 0
lista =[]

while i < 5:
    lista.append(int(raw_input("Digite o seguinte numero:")))
    i= i+1

i = 0
maior = lista[i]
while i < len(lista):
    if maior < lista[i+1]:
        maior = lista[i+1]
    i=i+1

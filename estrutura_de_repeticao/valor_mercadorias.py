print("Lojas Tabajara")
i = 1
preco_da_mercadoria = float(input("Produto {} : R$".format(i)))
total = 0
while preco_da_mercadoria != 0:
    i = i + 1
    total = total + preco_da_mercadoria
    preco_da_mercadoria = float(input("Produto {} : R$".format(i)))
print("Total: R${}".format(total))

dinheiro = float(input("Dinheiro: R$"))
troco = dinheiro - total
print("Troco: R${}".format(troco))

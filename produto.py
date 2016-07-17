def produto_mais_barato(produto1, produto2, produto3):
    if produto1 < produto2:
        if produto1 < produto3:
            print "Menor preco: {}".format(produto1)
        else:
            print "Menor preco: {}".format(produto3)
    else:
        if produto2 < produto3:
            print "Menor preco: {}".format(produto2)
        else:
            print "Menor preco: {}".format(produto3)


produto1 = float(raw_input("Qual o preco do produto 1?"))
produto2 = float(raw_input("Qual o preco do produto 2?"))
produto3 = float(raw_input("Qual o preco do produto 3?"))

produto_mais_barato(produto1, produto2, produto3)
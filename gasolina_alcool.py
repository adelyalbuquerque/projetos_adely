def preco_desconto_gasolina_alcool(litros, combustivel):
    if combustivel == "A":
        if litros <= 20:
            gasto = (litros * 1.90) - (litros * 0.03) * 1.90
            print "Valor a ser pago: {}".format(gasto)
        else:
            gasto = (litros * 1.90) - (litros * 0.05) * 1.90
            print "Valor a ser pago: {}".format(gasto)
    elif combustivel == "G":
        if litros <= 20:
            gasto = (litros * 2.50) - (litros * 0.04) * 2.50
            print "Valor a ser pago: {}".format(gasto)
        else:
            gasto = (litros * 2.50) - (litros * 0.06) * 2.50
            print "Valor a ser pago: {}".format(gasto)
    else:
        print "ERRO"


litros = float(raw_input("Quantos litros voce comprou?"))
combustivel = raw_input("Qual tipo de combustivel escolhido? (Alcool ou gasolina) A/G ")


preco_desconto_gasolina_alcool(litros, combustivel)
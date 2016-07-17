def valor_positivo_ou_negativo():
    valor = float(raw_input("Digite o numero: "))
    if valor > 0:
        print "Valor Positivo"
    elif valor == 0:
        print "Valor Neutro"
    else:
        print "Valor Negativo"

valor_positivo_ou_negativo()

def peso_pescaria():
    peso = float(raw_input("Quantos quilos foram pescados?"))
    excesso_peso = peso - 50
    if excesso_peso > 0:
        multa_por_excesso = excesso_peso * 4
    else:
        multa_por_excesso = 0

    print "Quilos excedidos: {}".format(excesso_peso)
    print "Multa por excesso: {}".format(multa_por_excesso)

peso_pescaria()

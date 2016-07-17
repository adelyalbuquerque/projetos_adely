def maior_numero():
    primeiro_numero = float(raw_input("Digite o primeiro numero: "))
    segundo_numero = float(raw_input("Digite o segundo numero: "))

    if primeiro_numero > segundo_numero:
        print "Maior numero: {}".format(primeiro_numero)
    else:
        print "Maior numero: {}".format(segundo_numero)


maior_numero()
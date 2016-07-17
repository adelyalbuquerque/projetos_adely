def definicao_sexo():
    sexo = raw_input("Qual seu sexo? (M/F)")
    if sexo == "F":
        print "FEMININO"
    elif sexo == "M":
        print "MASCULINO"
    else:
        print "SEXO INVALIDO"

definicao_sexo()

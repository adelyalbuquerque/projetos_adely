nota = int(raw_input("Digite uma nota entre 0 e 10: "))
while (nota < 0 or nota > 10):
    print "INVALIDO"
    nota = int(raw_input("Nota invalida! Digite uma nota entre 0 e 10: "))



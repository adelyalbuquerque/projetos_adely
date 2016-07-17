def classificador_vogal_ou_consoante():
    letra = raw_input("Digite uma letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print "VOGAL"
    elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print "VOGAL"
    else:
        print "CONSOANTE"

re_executar = "S"
while re_executar == "S":
    classificador_vogal_ou_consoante()
    re_executar = raw_input("Deseja executar novamente? S/N ")


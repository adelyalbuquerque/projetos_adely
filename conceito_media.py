def conceito_baseado_na_nota(nota1, nota2):
    if media >= 7.5 and media <= 10 :
        if media >= 9:
            print "CONCEITO A"
        else:
            print "CONCEITO B"
    elif media >= 4 and media < 7.5:
        if media >= 6:
            print "CONCEITO C"
        else:
            print "CONCEITO D"
    else:
        print "CONCEITO E"


nota1 = float(raw_input("Qual a sua primeira nota? "))
nota2 = float(raw_input("Qual a sua segunda nota?"))
media = (nota1 + nota2) / 2

conceito_baseado_na_nota(nota1, nota2)

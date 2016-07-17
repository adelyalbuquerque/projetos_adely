def media_alcancada(a, b):
    if media < 7:
        print "Reprovado"
    elif media >= 10:
        print "Aprovado com Distincao"
    else:
        print "Aprovado"


a = float(raw_input("Primeira nota: "))
b = float(raw_input("Segunda nota: "))
media = (a + b) / 2

media_alcancada(a, b)
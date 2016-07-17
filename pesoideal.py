def calculo_peso_ideal(altura, sexo):
  if sexo == "M":
      return (72.7 * altura) - 58
  elif sexo == "F":
    return (62.1 * altura) - 44.7
  else:
    return 0

altura = raw_input("Qual sua altura?")
altura = float(altura)
sexo = raw_input("Qual seu sexo? (M/F)")
peso = float(raw_input("Qual seu peso atual?"))

peso_ideal_da_pessoa = calculo_peso_ideal(altura, sexo)

if peso > peso_ideal_da_pessoa:
  print "Voce esta acima do peso"
elif peso < peso_ideal_da_pessoa:
  print "Voce esta abaixo do peso"
else:
  print "Voce esta no peso ideal"

print "Peso Ideal: {}".format(peso_ideal_da_pessoa)

def quantidade_valor_tintas(metros_quadrados_area):

    quantidade_litros_tinta = metros_quadrados_area / 3
    quantidade_de_latas = quantidade_litros_tinta / 18
    valor_gasto_em_latas = quantidade_de_latas * 80

    print "Numero de latas necessarias: {}".format(quantidade_de_latas)
    print "Valor a ser gasto: {}".format(valor_gasto_em_latas)

metros_quadrados_area = float(raw_input("Qual o tamanho em metros quadrados da area a ser pintada?"))

quantidade_valor_tintas(metros_quadrados_area)



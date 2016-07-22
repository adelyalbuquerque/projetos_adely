def reducao_tempo_de_vida_de_um_fumante(cigarros_dia, anos_fumando):
    cigarros_dia = int(cigarros_dia)
    anos_fumando = int(anos_fumando)
    minutos_perdidos_por_dia = cigarros_dia * 10
    dias_fumando = anos_fumando * 365
    minutos_perdidos_anos = dias_fumando * minutos_perdidos_por_dia
    horas_perdias_anos = minutos_perdidos_anos / 1440
    return horas_perdias_anos

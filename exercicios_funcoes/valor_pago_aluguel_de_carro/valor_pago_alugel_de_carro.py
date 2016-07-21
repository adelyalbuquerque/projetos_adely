def valor_pago_alugel_de_carro(km_percorrido, dias_alugados):
    km_percorrido = float(km_percorrido)
    dias_alugados = int(dias_alugados)
    valor_pago_km = km_percorrido * 0.15
    valor_pago_dias = dias_alugados * 60
    valor_total = valor_pago_km + valor_pago_dias
    return valor_total
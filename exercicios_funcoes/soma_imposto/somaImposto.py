def somaImposto(custo, taxa_impostos):
    custo = custo + (taxa_impostos * custo / 100 )
    return custo


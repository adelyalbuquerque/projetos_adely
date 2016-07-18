from definidor_numero_positivo_ou_negativo import definidor_numero_negativo_ou_postivo

def test_definidor_numero_positivo_ou_negativo():
    assert definidor_numero_negativo_ou_postivo(1) == "P"
    assert definidor_numero_negativo_ou_postivo(0) == "N"
    assert definidor_numero_negativo_ou_postivo(-2) == "N"

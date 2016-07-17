numero_de_turmas = int(input("Qual o numero de turmas? ")) # numero de turmas eh 10

turma_i = 1
media_subtotal = 0

while turma_i <= numero_de_turmas:
    numero_alunos_da_turma = int(input("Insira a quantidade de alunos da turma {}: ".format(turma_i)))
    while numero_alunos_da_turma > 40:
        numero_alunos_da_turma = int(input("ERRO! A quantidade de alunos tem que ser menor que 40, "
                                           "insira a quantidade de alunos da turman {} novamente: ".format(turma_i)))

    media_subtotal = media_subtotal + numero_alunos_da_turma
    turma_i = turma_i + 1

media = media_subtotal / numero_de_turmas

print("A media de alunos eh {}".format(media))
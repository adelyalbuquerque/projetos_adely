nome_usuario = raw_input("Digite seu nome: ")
senha_usuario = raw_input("Digite sua senha: ")
while (nome_usuario == senha_usuario):
    print "INVALIDO"
    nome_usuario = raw_input("Nome do usuario igual a senha! Favor digite seu nome: ")
    senha_usuario = raw_input("Nome do usuario igual a senha! Favir digite uma nova senha: ")




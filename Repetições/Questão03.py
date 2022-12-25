while True:
    nome = input('Digite o usuario: ')
    senha = input('Digite a senha: ')
    if nome == senha:
        print('A senha nao pode ser igual ao nome do usuario')
    else:
        print('Senha valida')
        break

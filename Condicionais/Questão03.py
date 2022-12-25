idade = int(input('Qual a sua idade? '))
if 16 <= idade < 18:
    print('Pode votar!')
    print('Não pode dirigir')
elif idade < 16:
    print('Não pode votar')
    print('Não pode dirigir')
else:
    print('Pode votar')
    print('Pode dirigir')

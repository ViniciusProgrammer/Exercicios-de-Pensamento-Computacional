nomes = ['Julio', 'Anna', 'Isabel', 'Izaac', 'Eduardo']
print('A lista contem os seguintes nomes:')
for c in nomes:
    print(c)
nome = str(input('Qual nome voce quer verificar? '))
if nome in nomes:
    print(f'O nome {nome} está na lista!')
else:
    print(f'O nome {nome} nao esta na lista!')


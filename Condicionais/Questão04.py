compra = float(input('Qual o valor da compra? R$'))
opc = str(input('''Informe a opção de compra
V - A vista
P - Parcelado
'''))
if opc in 'Vv':
    print('O valor da sua compra ficou R${:.2f}'.format(compra * 95/100))
elif opc in 'Pp':
    print('O valor da sua compra ficou R${} em 3x de R${:.2f}'.format(compra * 108/100, (compra * 108/100)/3))

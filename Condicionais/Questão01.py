opc = int(input('''1-SAQUE   2-DEPOSITO   3-SALDO'''))
saldo = 1000.00
if opc == 1:
    saque = float(input('Qual o valor deseja sacar?'))
    if saque <= 1000:
        print('Saque de R${} realizado.\nsaldo atual: R${}'.format(saque, saldo - saque))
    elif saque > 1000:
        print('Saldo insuficiente.')
elif opc == 2:
    dep = float(input('Qual valor a ser depositado?'))
    if dep >= 0:
        print('Deposito de R$ {} realizado.'.format(dep))
        saldo += dep
        print('Saldo atual: R${}'.format(saldo))
    else:
        print('Valor inválido')
elif opc == 3:
    print('Saldo atual: R${:.0f}\nObrigado por usar os nossos servicos.'.format(saldo))
    
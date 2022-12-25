def valores(n1, n2):
    primos = []
    for c in range(n1, n2 + 1):
        cont = 0
        for i in range(1, c + 1):
            if c % i == 0:
                cont += 1
        if cont == 2:
            primos.append(c)
    return primos


print('Vamos encontrar os numeros primos em um intervalo entre dois numeros positivos?')
num1 = int(input('Digite o numero menor do intervalo:'))
num2 = int(input('Digite o numero maior do intervalo:'))

valores(num1, num2)

primos = valores(num1, num2)

if len(primos) == 0:
    print('Nao ha numeros primos nesse intervalo!')

else:
    print('Os numeros primos sao:')
    for k in primos:
        print(f'{k}')

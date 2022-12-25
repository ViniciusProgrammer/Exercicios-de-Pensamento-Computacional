num1 = int(input('n1? '))
num2 = int(input('n2? '))
num3 = int(input('n3? '))

maior = 0
menor = 0
meio = 0
maiores = 0
menores = 0

if num1 > num2 and num1 > num3 and num2 > num3:
    maior = num1
    menor = num3
    meio = num2
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num2 > num1 and num2 > num3 and num1 > num3:
    maior = num2
    menor = num3
    meio = num1
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num3 > num1 and num3 > num2 and num1 > num2:
    maior = num3
    menor = num2
    meio = num1
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num1 > num2 and num1 > num3 and num2 < num3:
    maior = num1
    menor = num2
    meio = num3
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num3 > num1 and num3 > num2 and num2 > num1:
    maior = num3
    menor = num1
    meio = num2
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num2 > num1 and num2 > num3 and num3 > num1:
    maior = num2
    menor = num1
    meio = num3
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
    print('Meio: {}'.format(meio))

elif num1 == num2 == num3:
    print('todos sao iguais a {}'.format(num1))

else:
    if num1 == num2 and num1 > num3:
        print('Maiores: {}'.format(num1))
        print('Menor: {}'.format(num3))
        print('nao ha elementos do meio')

    elif num2 == num3 and num2 > num1:
        print('Maiores: {}'.format(num2))
        print('Menor: {}'.format(num1))
        print('nao ha elementos do meio')

    elif num1 == num3 and num1 > num2:
        print('Maiores: {}'.format(num3))
        print('O menor: {}'.format(num2))

    elif num1 == num2 and num1 < num3:
        print('Maior: {}'.format(num3))
        print('Menores: {}'.format(num1))
        print('nao ha elementos do meio')

    elif num2 == num3 and num2 < num1:
        print('Maior: {}'.format(num1))
        print('Menores: {}'.format(num2))
        print('nao ha elementos do meio')

    elif num1 == num3 and num3 < num2:
        print('Maior: {}'.format(num2))
        print('Menores: {}'.format(num3))

#Fatorial de um número
num = int(input('Digite um numero: '))
fatorial = 1
if num == 0:
    print(f'O numero tem que ser maior que {num}')
    num = int(input('Digite um numero: '))
if num > 0:
    for c in range(num, 0, -1):
        fatorial *= c
    print('Resultado fatorial: {} '.format(fatorial))

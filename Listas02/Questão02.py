termos = int(input('Quantos termos tu deseja ver? '))
t1 = 0
t2 = 1
t3 = t1 + t2
cont = 0
while cont < termos:
    if cont == termos - 1:
        print(f'{t3}', end='')
    else:
        print(f'{t3}', end=',')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1

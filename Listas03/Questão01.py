valores = []
for c in range(1, 6):
    num = int(input(f'Digite o numero {c}: '))
    valores.append(num)
for v in valores:
    if v % 2 == 0:
        print(f'O numero {v} e par')
    else:
        print(f'O numero {v} e ímpar')

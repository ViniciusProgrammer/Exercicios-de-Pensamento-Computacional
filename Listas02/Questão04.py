# Tabuada de quanto a quanto vc digitar
num1 = int(input('Informe um valor: '))
num2 = int(input('Informe o outro valor: '))
for c in range(num1, num2 + 1):
    print('A tabuada do {}'.format(c))
    for i in range(1, 10 + 1):
        print(f'{c} x {i} = {c*i}')
        
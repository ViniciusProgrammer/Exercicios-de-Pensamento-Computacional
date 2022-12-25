numbers = []
for i in range(0, 5):
    numbers.append(int(input()))
print('Digite 5 numeros:')
for k in range(1, 5):
    if numbers[k] > numbers[k - 1]:
        print('Intervalo [{}, {}] = '.format(numbers[k - 1], numbers[k]), end='')
        for j in range(numbers[k - 1], numbers[k] + 1):
            if j < numbers[k]:
                print('{},'.format(j), end='')
            else:
                print(j)
    else:
        print('Intervalo [{}, {}] = '.format(numbers[k], numbers[k - 1]), end='')
        for j in range(numbers[k], numbers[k - 1] + 1):
            if j < numbers[k - 1]:
                print('{},'.format(j), end='')
            else:
                print(j)

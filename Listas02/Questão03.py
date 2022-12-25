n1 = int(input('n1? '))
n2 = int(input('n2? '))
impares_nao_primos = []

if n1 > n2:
    temp = n2
    n2 = n1
    n1 = temp

for c in range(n1, n2+1):
    cont = 0
    if c % 2 == 1:
        for i in range(c, 0, -1):
            if c % i == 0:
                cont += 1
        if cont != 2:
            impares_nao_primos.append(c)
print('numeros impares nao primos [{}-{}]: {}'.format(n1, n2, ', '.join(map(str, impares_nao_primos))))

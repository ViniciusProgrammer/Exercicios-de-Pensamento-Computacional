# Procurando quantos números primos tem em um intervalo
n1 = int(input("n1?"))
n2 = int(input("n2?"))
primos = 0
for c in range(n1, n2 + 1):
    cout = 0
    for i in range(1, c + 1):
        if c % i == 0:
            cout += 1
    if cout == 2:
        primos += 1
if primos == 1:
    print("Existe {} numero primo entre {} e {}".format(primos, n1, n2))
else:
    print("Existem {} numeros primos entre {} e {}".format(primos, n1, n2))

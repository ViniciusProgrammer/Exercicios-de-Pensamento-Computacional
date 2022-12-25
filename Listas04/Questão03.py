def listas(l1, l2):
    ldivisores = []
    for k in range(0, len(l1)):
        cont = 0
        for t in range(0, len(l2)):
            if l2[t] % l1[k] == 0:
                cont += 1
        if cont == len(l2):
            ldivisores.append(l1[k])

    return ldivisores


n1 = int(input('Digite a quantidade de numeros que deseja incluir na Lista 1:'))

lista1 = []
lista2 = []

for c in range(0, n1):
    lista1.append(int(input('Digite um numero:')))

n2 = int(input('Digite a quantidade de numeros que deseja incluir na Lista 2:'))

for i in range(0, n2):
    lista2.append(int(input('Digite um numero:')))

listas(lista1, lista2)

ldivisores = listas(lista1, lista2)

if len(ldivisores) == 0:
    print('Nao foram encontrados valores da Lista 1 que dividem todos os valores da Lista 2!')
else:
    print('Os valores da Lista 1 que divide todos os valores de L2 sao:')
    for p in ldivisores:
        print(p)

N = int(input('Qual o N?'))
valores = []
print('Digite os valores:')
for i in range(0, N):
    valores.append(int(input('')))
op = int(input('Qual a OP?'))
A = int(input('Qual o A?'))
B = int(input('Qual o B?'))
if op == 0:
    total = valores[A - 1] + valores[B-1]
    print('{} + {} = {}'.format(valores[A-1], valores[B-1], total))
elif op == 1:
    total = valores[A-1] * valores[B-1]
    print('{} * {} = {}'.format(valores[A-1], valores[B-1], total))

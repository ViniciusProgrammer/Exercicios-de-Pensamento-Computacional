def valores(num_valores):
    valor = (f'{num_valores}')
    return valor


def textos(num_textos):
    textos = (f'{num_textos}')
    return textos
    
    
num_valores = [] 
num_textos = []

num1 = int(input('Digite a quantidade de numeros que deseja incluir:'))

for c in range(0, num1):
    num_valores.append(int(input('Digite um numero:')))

num2 = int(input('Digite a quantidade de textos que deseja incluir:'))

for i in range(0, num2):
    num_textos.append(input('Digite um texto:'))
    
print('Lista de numeros:')

for k in num_valores:
    print(k)

print('Lista de textos:')

for t in num_textos:
    print(t)

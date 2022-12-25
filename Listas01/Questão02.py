num = int(input('Qual numero gostaria de checar os divisores?'))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1
print(f'O numero {num} tem {div} divisores.')

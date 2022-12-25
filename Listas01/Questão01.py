lista = ['primeiro', 'segundo', 'terceiro', 'quarto']
tot_area = 0
for item in lista:
    print(f'Digite os dados pro {item} cômodo')
    comprimento = float(input('C: '))
    largura = float(input('L: '))
    tot_area += (comprimento*largura)
    print('A área deste cômodo é {:.0f} m²'.format(comprimento*largura))
print('A área total da casa é {} m²'.format(tot_area))

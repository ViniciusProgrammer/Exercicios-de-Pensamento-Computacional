from math import floor

dias = int(input('Qual o numero de dias? '))
semanas = dias / 7
diasSemana = int((semanas - int(semanas)) * 8)

if dias == 0:
    print('{} dias equivale a nenhum dia.'.format(dias))
if semanas < 2 and semanas >= 1:
    if diasSemana == 0:
        print('{} dias equivalem a {:.0f} semana!'.format(dias, semanas))
    else:
        print('{} dias equivalem a {:.0f} semana'.format(dias, floor(semanas)), end=' ')
elif semanas >= 2 or semanas < 1 and semanas != 0:
    if diasSemana == 0:
        print('{} dias equivalem a {:.0f} semanas!'.format(dias, floor(semanas)))
    elif diasSemana == 3:
        print('{} dias equivalem a {:.0f} semana'.format(dias,floor(semanas)), end=' ')
    else:
        print('{} dias equivalem a {:.0f} semanas'.format(dias, floor(semanas)), end=' ')

if (diasSemana == 1):
    print('e 1 dia!')
elif (diasSemana > 1):
    print('e {} dias!'.format(diasSemana))


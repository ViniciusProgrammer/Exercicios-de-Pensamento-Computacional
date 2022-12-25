def media_aritmetica(notas):
    media = ((notas[0]) + (notas[1]) + (notas[2])) / 3
    return media


def media_ponderada(notas):
    media = ((notas[0] * 5) + (notas[1] * 3) + (notas[2] * 2)) / 10
    return media


notas = []
print('Quais sao as notas?')

for c in range(0, 3):
    notas.append(float(input('')))
letra = input('Que tipo de media voce quer?')
if letra.upper() == 'A':
    print('A media e: {}'.format(media_aritmetica(notas)))
elif letra.upper() == 'P':
    print('A media e: {}'.format(media_ponderada(notas)))

print('Informe os lados')
l1 = int(input(''))
l2 = int(input(''))
l3 = int(input(''))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print('Os lados [{}, {}, {}] representam um triângulo equilatero'.format(l1, l2, l3))
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('Os lados [{}, {}, {}] representam um triângulo escaleno'.format(l1, l2, l3))
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Os lados [{}, {}, {}] representam um triângulo isosceles'.format(l1, l2, l3))
else:
    print('Os lados [{}, {}, {}] não representam um triângulo'.format(l1, l2, l3))

from math import floor
s_atual = float(input('Qual o salário atual?'))
ajuste = float(input('Qual a porcentagem de ajuste?'))
print('O reajuste foi de {:.0f} reais e {:.1f} centavos.'.format(floor(s_atual * ajuste /100), 
(s_atual * ajuste/100 - int(s_atual * ajuste/100)) * 100))
print('O valor final do salário é {:.1f} reais e {:.1f} centavos.'.format(floor(s_atual + (s_atual * ajuste/100)),
(s_atual + (s_atual * ajuste/100 - int(s_atual + (s_atual * ajuste/100))))* 100))

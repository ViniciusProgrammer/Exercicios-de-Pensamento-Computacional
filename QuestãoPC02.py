valor_divida = float(input('Qual e o valor inicial da divida (apenas o numero)? '))
multa = float(input('Qual o valor da multa por dia de atraso? '))
dias = float(input('Quantos dias esta em atraso? '))
print('O valor da divida e R${}'.format(valor_divida + (multa*dias)))

km_inicial = int(input('Qual o valor da kilometragem inicial?'))
km_final = int(input('Qual o valor da kilometragem final?'))
litros = float(input('Quantos litros foram consumidos na viagem?'))
print('O valor de consumdo médio é de: {:.1f} Km/L'.format((km_final - km_inicial)/litros))

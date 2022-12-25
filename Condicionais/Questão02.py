salario = float(input('Qual o seu salário? R$'))
financiamento = float(input('Qual o valor que deseja contratar? R$'))
if financiamento <= (5 * salario):
    print('Financiamento Concedido!')
else:
    print('Financiamento Negado!')
print('Agradecemos por nos consultar!')

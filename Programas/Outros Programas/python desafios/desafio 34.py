print('=========AUMENTO SALARIAL=========')
salario = float(input('Digite o valor do salário do funcionário: R$ '))

if salario < 1250.00:
    a1 = ((salario/100) * 15) + salario
    print('O salario aumentou de R${:.2F} para R${:.2F}'.format(salario, a1))
else:
    a2 = ((salario/100) * 10) + salario
    print('O salario aumentou de R${:.2F} para R${:.2F}'.format(salario, a2))
n = float(input('Digite o valor do salário do funcionário: R$ '))
desc = n*15/100
a = n + desc

print('O valor inicial do salário do funcionário é igual a R$ {:.2f}.\n Os 15 por cento desse valor é igual a R$ {:.2f}.\n Portanto, o valor de salário com os aumentos irá ser igual a R$ {:.2f}'.format(n, desc, a))
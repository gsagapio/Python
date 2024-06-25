n = float(input('Digite o preço do produto: R$ '))
npreço = n*5/100
d = n - npreço
a = n + npreço

print('O preço inicial do produto é R$ {:.2f}.\n O valor do desconto de 5% é igual a R$ {:.2f}.\n O preço final com o desconto aplicado é R$ {:.2f}. \n Já o preço com aumento de 5% é igual a R$ {:.2f}.'.format(n, npreço, d, a))
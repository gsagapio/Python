#Exercício 10 função dicionário produtos

def calcula_valor_total(produtos):
    valor_total = 0
    for produto, preco in produtos.items():
        valor_total += preco
    return valor_total

produtos = {'batata': 8.00, 'linguiça': 3.50, 'filé': 7.50, 'queijo': 3.00}
resultado = calcula_valor_total(produtos)
print(resultado)

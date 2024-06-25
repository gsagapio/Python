print('-'*25)
print('   LOJA SUPER BARATÃO')
print('-'*25)

total = mil = cont = menor = 0
barato = ' '

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço

    if preço > 1000:
        mil += 1
    
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
            break

print('-'*10, ' Fim do programa ', '-'*10)

print(f'''O total da compra foi R${total:.2f}
Temos {mil} produto(s) custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${menor:2f}.''')

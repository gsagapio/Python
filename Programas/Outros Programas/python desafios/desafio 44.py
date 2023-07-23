print ('======== SIMULADOR DE COMPRA ========')
preço = float(input('Preço total da compra: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual é a forma de pagamento? '))

if opção == 1:
    valor = preço - ((preço / 100) * 10)
    print('Por pagar com essa forma de pagamento, irá receber 10 por cento de desconto! \nPortanto, ao invés de pagar R${:.2f} irá pagar R${:.2f}.'.format(preço, valor))

elif opção == 2:
    valor = preço - ((preço / 100) * 5)
    print('Por pagar com essa forma de pagamento, irá receber 5 por cento de desconto! \nPortanto, ao invés de pagar R${:.2f} irá pagar R${:.2f}.'.format(preço, valor))

elif opção == 3:
    print('Por pagar com essa forma de pagamento, não receberá nenhum desconto ou juros! \nPortanto, irá pagar R${:.2f}.'.format(preço))

elif opção == 4:
    
    parcelas = int(input('Pagará em quantas parcelas? '))
    valor = preço + ((preço / 100) * 20)
    x = valor / parcelas

    print('Por optar por essa forma de pagamento, irá pagar com 20 por cento de juros! \nPortanto, ao invés de pagar R${:.2f} o preço final ao todo será R${:.2f}. \nE cada parcela custará R${:.2f}'.format(preço, valor, x))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.')

print('Obrigado, tenha um bom dia e volte sempre!')
print('=========PREÇO DA VIAGEM=========')
viagem = float(input('Qual será a distância da viagem em KM? '))

if viagem <= 200:
    print('Uma viagem de {} custará R${:.2f}'.format(viagem, viagem * 0.50))
else:
    print('Uma viagem de {} custará R${:.2f}'.format(viagem, viagem * 0.45))
dias = float(input('Por quantos dias alugou o carro? '))
km = float(input('Por quantos quilometros ele rodou? '))
preço = (dias * 60) + (km * 0.15)

print('O preço final a pagar pelos dias utilizados ({}) e pelos quilometros rodados ({}km) é igual a: R$ {:.2f}'.format(dias, km, preço))
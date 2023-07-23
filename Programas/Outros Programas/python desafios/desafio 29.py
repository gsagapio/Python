print('-----VOCÊ FOI PARADO POR UM RADAR-----')
vel = float(input('Qual é a velocidade do seu carro em KM? '))

if vel >= 80:
    multa = (vel - 80) * 7
    print('O seu carro ultrapassou o limite de velocidade de 80km! A multa a ser paga é de R${:.2f}'.format(multa))
    
else:
    print('O seu caro está dentro do limite de velocidade, continue assim!')

print('Tenha um bom dia e dirija com segurança.')
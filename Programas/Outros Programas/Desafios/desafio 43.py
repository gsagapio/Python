print('<=====IMC=====>')

peso = float(input('Quanto você pesa? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso, pois seu IMC é {:.1f}'.format(imc))

elif imc >= 18.5 and imc < 25:
    print('Peso Ideal, pois seu IMC é {:.1f}'.format(imc))

elif 25 <= imc < 30:
    print('Sobrepeso, pois o seu IMC é {:.1f}'.format(imc))

elif imc > 30 and imc < 40:
    print('Obesidade, pois o seu IMC é {:.1f}'.format(imc))

else:
    print('Obesidade mórbida, pois o seu IMC É {:.1f}'.format(imc))
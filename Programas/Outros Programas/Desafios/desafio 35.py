print('=========FORMA UM TRIâNGULO?=========')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o compprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos {}, {} e {} formam um TRIÂNGULO.'.format(r1, r2, r3))
else:
    print('Os segmentos {}, {} e {} não formam um TRIÂNGULO.'.format(r1, r2, r3))
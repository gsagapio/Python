b = float(input('Qual é a largura da sua parede em metros? '))
h = float(input('Qual é a altura da sua parede em metros? '))
area = b*h
tinta = area/2
print('As medidas da sua parede são {} X {}, portanto, a sua area é igual a {}m²'.format(b, h, area))
print('Com base nisso, precisará de {} litros de tinta para conseguir pintá-la.'.format(tinta))
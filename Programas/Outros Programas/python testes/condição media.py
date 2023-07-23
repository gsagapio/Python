n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi igual a {:.1f}'.format(media))

if media >= 6.0:
    print('Sua média foi boa, parabens!')
else:
    print('Sua média foi ruim, estude mais!')
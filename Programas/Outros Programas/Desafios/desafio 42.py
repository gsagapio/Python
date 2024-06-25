print('<====TRIANGULOS====>')

n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem formar um triângulo ', end = '')
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')

else:
    print('Os segmentos acima não podem formar um triângulo.')
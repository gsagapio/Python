fatorial = int(input('Digite um número que você deseja saber o fatorial: '))
contador = fatorial
f = 1
print('Calculando {}! = '.format(contador), end = '')

while contador > 0:
    print('{}'.format(contador), end = '')
    print(' X ' if contador > 1 else ' = ', end = '')
    f *= contador
    contador -= 1
print('{}.'.format(f))
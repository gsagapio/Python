print('=^'*10)
print('Taboada / Break')
print('=^'*10)


while True:
    num = int(input('Digite um valor para saber a sua taboada (Digite um número negaivo se quiser parar): '))

    if num < 0:
        break

    for c in range(1, 11):
        print('{:2} x {:2} = {:2}'.format(num, c, (num*c)))

print('TABOADA ENCERRADA')

    
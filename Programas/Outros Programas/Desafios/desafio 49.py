print('===TABOADA===')

n = int(input('Digite um numero inteiro: '))

for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(n, c, (n*c)))
n = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=" ")
        total = total + 1

    else:
        print('\033[31m', end=" ")

    print('{} '.format(c), end=" ")

print('\n\033[mO número {} foi divisivel {} vez(zes).'.format(n, total))

if total == 2:
    print('Por isso ele é primo.')

else:
    print('Poe isso ele não é primo.')
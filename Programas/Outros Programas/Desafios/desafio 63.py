print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int (input('Qual é a quantidade de termos que vocÊ quer mostrar meu querido? '))

termo1= 0
termo2 = 1

print('{} > {} '.format(termo1, termo2), end = '')

contador = 3

while contador <= n:
    termo3 = termo1 + termo2
    print('> {} '.format(termo3), end = '')
    contador = contador + 1
    termo1 = termo2
    termo2 = termo3
print('Fim')
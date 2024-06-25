print('=' * 15)
print('Somando e contando valores (coisa de louco meu colega)')
print('=' * 15)

n = 0
contador = 0
soma = 0

n = int(input('Digite um número [Digite 999 para parar]: '))
while n != 999:
    contador = contador + 1 #ou contador += 1
    soma = soma + n
    n = int(input('Digite um número [Digite 999 para parar]: '))

print('Você digitou {} numeros antes de 999 e a soma entre eles é {}.'.format(contador, soma))
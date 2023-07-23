soma = 0
contador = 0

for c in range (0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1

print('A quantidade de valores pares é igual a {} e a soma deles é igual a {}.'.format(contador, soma))

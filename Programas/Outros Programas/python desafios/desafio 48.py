soma = 0
cont = 0
for c in range(3, 501, 6):
    soma = soma + c
    cont = cont + 1
print('A soma de todos os valores multiplos de 3 e ímpares é igual a {}.'.format(soma))
print('Entre 1 e 500 existem {} valores que se encaixam nas condições.'.format(cont))
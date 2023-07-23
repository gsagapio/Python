from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for c in range(1, 8):
    data = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - data

    if idade >= 21:
        print('A {}º pessoa já atingiu a maioridade, ela tem {} anos.'.format(c, idade))
        totalmaior += 1
    else:
        print('A {}º pessoa ainda não atingiu a maioridade, ela tem {} anos.'.format(c, idade))
        totalmenor += 1

print('Um total de {} já são maiores e {} ainda são menores de idade.'.format(totalmaior, totalmenor))

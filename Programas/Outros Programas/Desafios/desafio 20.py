from random import shuffle
nome1 = str(input('Digite o primiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))
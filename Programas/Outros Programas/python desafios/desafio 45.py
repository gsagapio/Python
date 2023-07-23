from random import randint
from time import sleep
print ('======== JO KEN PO ========')
itens = ('Pedra', 'Papel', 'Tesoura')

print('''ESCOLHA A SUA JOGADA:
[1] Pedra
[2] Papel
[3] Tesoura''')

jogada = int(input('Qual jogada você escolhe? 1, 2 ou 3? '))
maquina = randint(0, 2)

print('JO...')  
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
if jogada == 1 and maquina == 0: 
    print('-=' * 10)
    print('EMPATE. \nVocê escolheu Pedra e o computador também escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 1 and maquina == 1:
    print('-=' * 10)
    print('DERROTA. \nVocê escolheu Pedra e computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 1 and maquina == 2:
    print('-=' * 10)
    print('VITÓRIA. \nVocê escolheu Pedra e o computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 2 and maquina == 0:
    print('-=' * 10)
    print('VITÓRIA. \nVocê escolheu Papel e computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 2 and maquina == 1:
    print('-=' * 10)
    print('EMPATE. \nVocê escolheu Papel e o computador também escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 2 and maquina == 2:
    print('-=' * 10)
    print('DERROTA. \nVocê escolheu Papel e computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 3 and maquina == 0:
    print('-=' * 10)
    print('DERROTA. \nVocê escolheu Tesoura e computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 3 and maquina == 1:
    print('-=' * 10)
    print('VITÓRIA. \nVocê escolheu Tesoura e o computador escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

elif jogada == 3 and maquina == 2:
    print('-=' * 10)
    print('EMPATE. \nVocê escolheu Tesoura e computador também escolheu {}.'.format(itens[maquina]))
    print('-=' * 10)

else:
    print('Jogada inválida, tente novamente!')
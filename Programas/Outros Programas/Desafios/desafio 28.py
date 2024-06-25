import random
from time import sleep
print('Vou pensar em um número entre 0 e 5...')
print('-=-'*15)
num = int(input('Em que número eu pensei? '))
print('-=-'*15)
n = [0, 1, 2, 3, 4, 5]
escolha = random.choice(n)

print('PROCESSANDO...')
sleep(3)

if num == escolha:
    print('Você acertou, parabéns!')
else:
    print('Infelizmente você errou, sinto muito. Eu pensei no número {} e você pensou no número {}'.format(escolha, num))
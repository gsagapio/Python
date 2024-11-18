#Modulos com import

import random

for i in range(5):
    print(random.randint(1, 10))

#Modulos com from import

from random import *

for i in range(7):
    print(randint(1, 10))

#Forçar termino de codigo com modulo sys

import sys

while True:
    print('Digite "sair" para terminar a execução do programa.')
    resposta = input()
    
    if resposta == 'sair':
        sys.exit()
    print('Você digitou ', resposta, ' e não "sair"')
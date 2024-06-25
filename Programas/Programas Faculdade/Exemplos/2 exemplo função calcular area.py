#Exemplo 2 Criar uma função que calcula a área de um círculo

import math

def areacalculo(raio):
    area = math.pi * raio ** 2
    return print(area)

raio = 2
area = areacalculo(raio)
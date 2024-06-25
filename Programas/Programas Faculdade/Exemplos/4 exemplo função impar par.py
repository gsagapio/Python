#Exemplo 4 Criar uma função que recebe um número ­e verifica se ele é par ou ímpar
import random
def parimpar(numero):
    if numero % 2 == 0:
        print(numero, "é um número par, somente coisa boa")
    else: 
        print(numero, "é um numero impar, não chega a ser uma coisa ruim")
        
numero = random.randint(1, 100)
parimpar(numero)

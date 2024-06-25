#Exemplo 9 Criar uma função que recebe um número variável de argumentos e retorna a soma deles
import math
def soma (*argumentos):
    resultado = 0
    for numero in argumentos:
        resultado += numero
    return print(resultado)

resultado = soma(4, 3, 2, 1)
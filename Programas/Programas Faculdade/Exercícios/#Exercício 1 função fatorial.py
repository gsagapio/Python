#Exercício 1 função fatorial

def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat

numero = 4
resultado = fatorial(numero)
print(resultado)

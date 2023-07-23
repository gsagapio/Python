#Exercício 4 função true false

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numero = 4
resultado = eh_primo(numero)
print(resultado)

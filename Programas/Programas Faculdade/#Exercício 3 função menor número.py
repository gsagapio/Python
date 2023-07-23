#Exercício 3 função menor número

def menor(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

numero1 = 2
numero2 = 4
resultado = menor(numero1, numero2)
print(resultado)

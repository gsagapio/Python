#exemplo 6 Criar uma função que recebe dois números e retorna o quociente e o resto da divisão inteira entre eles

def divisao(numero1, numero2):
    resto = numero1 % numero2
    quociente = numero1 // numero2
    return quociente, resto

resultado = divisao (10, 5)
print (resultado)
#exemplo 8 Criar uma função que recebe um número x e uma função f e aplica f a x

def funçaoaplicaçao(x, f):
    return f(x)

def dobro(x):
    return x * 2

numero = float(input('Digite um numero por gentileza: '))
resultado = funçaoaplicaçao(numero, dobro)
print ("O dobro de", numero, "é", resultado)
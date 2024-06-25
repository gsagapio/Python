    #while impar ou par
par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1 
print('Você digitou {} numeros pares e {} numeros impares.'.format(par, impar))
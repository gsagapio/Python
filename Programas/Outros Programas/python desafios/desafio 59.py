num = float(input('Digite um número: '))
num2 = float(input('Digite o segundo número: '))
print('''As opções são:
      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos numeros
      [5] fim ''')

opção = 0

while opção != 5:
    opção = int(input('Qual opção você escolhe? '))

    if opção == 1:
        print('A soma entre {} e {} é igual a {}.'.format(num, num2, num + num2))
    elif opção == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(num, num2, num * num2))
    elif opção == 3:
        if num > num2:
            print('O primeiro número, {}, é maior que o segundo, {}.'.format(num, num2))
        elif num == num2:
            print('Não há numero maior, ambos são iguais.')
        else:
            print('O segundo número, {}, é maior que o primeiro, {}.'.format(num2, num))
    elif opção == 4:
        num = float(input('Digite um número novamente: '))
        num2 = float(input('Digite o segundo número novamente: '))
    
    elif opção == 5:
        print('Fim do programa')

    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')

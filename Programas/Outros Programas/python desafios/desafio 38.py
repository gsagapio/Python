print('===VALORES===')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor, {}, é maior que o segundo valor, {}.'.format(num1, num2))
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo valor, {}, é maior que {}.'.format(num2, num1))
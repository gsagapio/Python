print ('<=====CONVERTOR=====>')

num = int(input('Digite um número inteiro: '))
print('''Escolha uma daas bases para a conversão: 
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido em binário se torna {}'.format(opção, bin(num)[2:]))

elif opção == 2:
    print ('{} convertido em octal se torna {}'.format(opção, oct(num)[2:]))

elif opção == 3:
    print('{} convertido em hexadecimal se torna {}'.format(opção, hex(num)[2:]))

else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
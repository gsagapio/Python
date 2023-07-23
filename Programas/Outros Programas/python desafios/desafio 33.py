print('=========MAIOR E MENOR=========')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite ooutro númeero: '))
n3 = int(input('Digite mais um número: '))

#maior valor
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
else:
    print('O maior número é {}'.format(n3))
    
#menor valor
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
else:
    print('O menor número é {}'.format(n3))
print('FIM')
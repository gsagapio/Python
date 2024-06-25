print('GERADDOR DE PA')
print('-=' * 10)
n1 = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))

termo = n1
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end = '')
    termo += razao
    cont +=1 

print('FIM')
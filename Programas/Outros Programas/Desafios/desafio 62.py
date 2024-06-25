print('GERADDOR DE PA')
print('-=' * 10)
n1 = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razao da PA: '))

termo = n1
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end = '')
        termo += razao
        cont +=1 

    print('Pausa')
    mais = int(input('Quer mais quantos termos? '))
print('Fim')

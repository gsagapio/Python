from time import sleep
n = int(input('''Está preparado para ter uma surpresa? 
[1] SIM
[2] NÃO
[3] Qual surpresa?
Qual a sua decisão? '''))

if n == 1:
    for c in range(0, 11):
        print(10 - c)
        sleep(0.5)
    print('!!!BOOOMMMM!!!')

elif n == 3:
    print('Tem que digitar 1 para saber, animal. Execute novamente.')

else: 
    print('Sem graça.')
    print('FIM')

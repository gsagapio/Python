from datetime import date
print('<=====ATLETA=====>')

atual = date.today().year
ano = int(input('Digite o ano em que você nasceu: '))
idade = atual - ano

if idade <= 9:
    print('Você tem {} ano(s) atualmente, é classificado como atleta MIRIM.'.format(idade))

elif idade <= 14:
    print('Você tem {} ano(s) atualmente, é classificado como atleta INFANTIL.'.format(idade))

elif idade <= 19:
   print('Você tem {} ano(s) atualmente, é classificado como atleta JUNIOR.'.format(idade))

elif idade <= 25:
    print('Você tem {} ano(s) atualmente, é classificado como atleta SÊNIOR.'.format(idade))
    
else:
    print('Você tem {} ano(s) atualmente, é classificado como atleta MASTER.'.format(idade))


 

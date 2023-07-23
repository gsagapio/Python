from datetime import date
print('<====Alistamento Militar====>')

atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano

print('Quam nasceu em {} completa {} anos no ano atual.'.format(ano, idade))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')

elif idade > 18:
    n = atual - (idade - 18)
    print('Você passou do tempo de alistamneto. Faz {} ano(s) que você deveria ter se alistado, que foi em {}.'.format((idade - 18), n))

elif idade < 18:
    n = atual - (18 - idade)
    print('Você ainda não chegou na idade de alistamento. Faltam {} ano(s) para você se alistar, que será em {}.'.format((ano - idade), n))
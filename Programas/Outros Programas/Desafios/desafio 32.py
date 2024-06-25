from datetime import date
print('=========ANO BISSEXTO=========')
ano = int(input('Digite qual ano quer analisar: (Digite 0 se quiser analisar o ano atual)'))

bi = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if ano == 0:
    ano = date.today().year

if ano == bi:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'. format(ano))
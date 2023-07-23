frase = str(input('Digite uma frase: ')).strip()
a =  frase.upper().count('A')
p = frase.upper().find('A')+1
u = frase.upper().rfind('A')+1
print('A letra A aparece em uma quantidade de vezez igual a {}'.format(a))
print('A primeira letra A apareceu na posição {}'.format(p))
print('A ultima letra A aparece na posição {}'.format(u))
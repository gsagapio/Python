nome = str(input('Qual é o seu nome completo? ')).strip()
n = nome.upper().split()
print('Seu nome possuí Silva? {}'.format('SILVA' in n))
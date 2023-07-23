nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print('Que nome lindo você tem!', nome)
else:
    print('Seu nome é tão normal!', nome)

print('Bom dia {}!'.format(nome))
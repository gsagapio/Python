somaidade = 0
mediaidade= 0

maioridademan = 0
nomevelho = ''

totalmulher = 0

for p in range (1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridademan = idade
        nomevelho = nome
    
    if sexo in 'Mn' and idade > maioridademan:
        maioridademan = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totalmulher += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais veho tem {} anos e se chama {}.'.format(maioridademan, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher))
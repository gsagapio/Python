idh = 0
idm = 0
conth = 0
contm = 0
cont = 0

while True:
    print('='*15)

    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa, Masculino ou Feminino [M/F]: ')).strip().upper()[0]


    if sexo in 'M':
        idh = idade
        conth += 1
    if idade > 18:
        cont += 1

    elif sexo in 'F':
        if idade < 20:
            contm += 1
            if idade > 18:
                cont += 1

    n = str(input('Quer contnuar? [S/N]')).strip().upper()[0]

    if n == 'N':
        break

print(f'No total, {conth} homens foram cadastrados. {contm} mulheres tem menos de 20 anos e {cont} tem mais de 18 anos.')
    
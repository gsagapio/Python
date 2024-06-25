from random import randint

print('=^'*15)
print('PAR OU IMPAR')
print('=^'*15)

v = 0

while True:
    jogador = int(input('Diga um valor (de 0 a 10): '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end = ' ')

    print('Deu par' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')
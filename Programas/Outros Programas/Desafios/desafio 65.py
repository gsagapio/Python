resposta = 'S'
media = 0
soma = 0
quantia = 0
maior = 0
menor = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quantia = quantia + 1

    if quantia == 1:
        maior = menor = num

    else: 
        if num > maior:
            maior = num
        elif num < menor:
            menor = maior

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
media = soma / quantia
print('VocÊ digitou {} numeros e a media foi {}.'.format(quantia, media))
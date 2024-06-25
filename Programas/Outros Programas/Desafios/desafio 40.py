print('<===MÉDIA===>')

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print('A media das suas notas {} e {} foi {}. Portanto, você foi APROVADO.'.format(n1, n2, media))
elif media < 5:
    print('A sua media entre {} e {} foi de {}. Portanto, você foi REPROVADO.'.format(n1, n2, media))
else:
    print('A media das suas notas {} e {} é igual a {} e está entre 5.0 e 6.9, portanto, você está de RECUPERAÇÃO.'.format(n1, n2, media))
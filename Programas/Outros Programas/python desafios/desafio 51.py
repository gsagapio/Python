n1 = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))

for c in range(n1, n1 * 11, razao):
    print(c, end=" ")
print('FIM')
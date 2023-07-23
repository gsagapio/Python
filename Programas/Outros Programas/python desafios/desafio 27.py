nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(n[0], n[len(n)-1]))
nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome== 'João' or nome== 'Maria' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Paulo Gabriel Fernanda Giovana':
    print('Nome comum, mas bonito.')
    
else:
    print('Seu nome é bem normal.')

print('Tenha uum bom dia {}!'.format(nome))
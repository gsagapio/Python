# Criar uma função que recebe um dicionário de nomes e idades e retorna o nome da pessoa mais velha

def maisvelha(dicionario):
    nomevelho = ' '
    idadevelho = 0
    
    for nome, idade in dicionario.items():
        if idade > idadevelho:
            idadevelho = idade
            nomevelho = nome   
    return nomevelho

nomeidade = {'Gustavo': 18, 'Silva': 24, 'Agapio': 22}
nomevelho = maisvelha (nomeidade)
print(nomevelho)
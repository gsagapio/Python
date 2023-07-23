#Exemplo 5 Criar uma função que recebe um texto e retorna o número de vogais nele

def calculovogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return print("A quantidade de vogais no texto é: ", contador)

texto = 'abcdefghijklmnopqrstuvwxyz'
vogal = calculovogais(texto)
            
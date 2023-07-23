#Exemplo 3 Criar uma função que recebe uma lista d­­e números e retorna o maior deles

def omaiornumero(lista):
    maiornumero = lista[0]
    for numero in lista:
        if numero > maiornumero:
            maiornumero = numero
    return print("O maior número da lista é: ", maiornumero)

numeros = [2, 4, 6, 8, 10, 16, 12, 14]
maiornumero = omaiornumero(numeros)
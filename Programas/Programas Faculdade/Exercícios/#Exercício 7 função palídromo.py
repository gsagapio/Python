#Exercício 7 função palídromo

def eh_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    return texto == texto[::-1]

texto = "Essa frase é um palidromo"
resultado = eh_palindromo(texto)
print(resultado)

#Exercício 5 função número de palavras

def conta_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = "Quantas palavras tem aqui?"
resultado = conta_palavras(texto)
print(resultado)

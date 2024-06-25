#Exercício 8 função angramas

def sao_anagramas(texto1, texto2):
    texto1 = texto1.lower().replace(' ', '')
    texto2 = texto2.lower().replace(' ', '')
    return sorted(texto1) == sorted(texto2)

texto1 = "maca"
texto2 = "cama"
resultado = sao_anagramas(texto1, texto2)
print(resultado)

#Exercício 9 função nome mais longo

def encontra_mais_longo(*textos):
    mais_longo = ''
    for texto in textos:
        if len(texto) > len(mais_longo):
            mais_longo = texto
    return mais_longo

texto1 = "texto"
texto2 = "mais"
texto3 = "longo desse código"
resultado = encontra_mais_longo(texto1, texto2, texto3)
print(resultado)

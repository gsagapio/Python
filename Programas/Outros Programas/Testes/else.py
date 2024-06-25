nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (nota1+nota2)/2

#verificação
if mediafinal >= 7.0:
    print("A média: %.1f - Aprovado"% mediafinal)

else:
    print("A média: %.1f - Reprovado "% mediafinal)
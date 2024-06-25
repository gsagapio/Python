media = 0
soma = 0
nomemaisvelho = str
maisvelho = 0
menosdevinte = 0
for pessoa in range(1,5):
    nome =input(f"Nome ")
    idade =int(input(f"idade "))
    sexo =input(f"sexo F/M ")
    soma+= idade
    if pessoa == 1 and sexo == "M":
        nomemaisvelho = nome
        maisvelho+=idade
    if idade > maisvelho and sexo =="M":
        maisvelho+=idade
        nomemaisvelho = nome
    if sexo == "F" and idade > 20:
        menosdevinte+=1
media = soma/5
print(F"A MEDIA DA SOMA É {media}")
print(F"O NOME DO HOMEM MAIS VELHO É {nomemaisvelho}")
print(F"QUANTIDADE DE MULHERES COM MENOS DE 20 É {menosdevinte}")
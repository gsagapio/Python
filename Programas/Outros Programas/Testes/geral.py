frase = 'Curso em Vídeo Python'

print(frase[0:21:2]) #Vai printar do 0 até o 21 caractere pulando de 2 em 2

print(frase[:5]) #Vai começar antes do dois pontos, ou seja, do início, já que não há nada escrito

print(frase[15:]) #Vai começar do 15 até o final

print(frase[9::3]) #entre o os dois pontos não há nada, então vai contar do 9 até o final pulando em 3 em 3

print(len(frase)) #Vai mostrar o comprimento da string

print(frase.count('a')) #Vai contar quantas vezes aparece a letra na frase (diferencia A de a)

print(frase.count('o',15,80)) #Vai mostrar quantos "o" tem entre a 15º letra e a última

print(frase.find('Python')) #Vai mostrar de onde começou a sequência de string

print('Curso'in frase) #Existe "Curso" em frase? True ou False

print(frase.replace('Python', 'Android')) #Irá substituir "Python" por "Android"

print(frase.upper()) #Deixará toda a frase em caixa alta

print(frase.lower()) #Deixará toda a frase em letras minúsculas

print(frase.capitalize()) #Todas as letras ficarão em letra minúscula, e a primeira ficará em caixa alta

print(frase.title()) #As primeiras letras de cada palavra ficarão em maiúsculas


frase2 = '   Aprenda Python   '

print(frase2.strip()) #Vai remover todos os espaços inúteis antes e depois da string

print(frase2.rstrip()) #Removerá os espaços inúteis a direita

print(frase2.lstrip()) #Removerá os espaços inúteis a esquerda

print(frase.split()) #Onde houver espaços o split fará uma divisão

dividido = frase.split()

print(dividido[2][3])

print(''.join(frase.split()))

print(frase[::-1]) #Vai escrever ao contrário

if 'Curso' in frase:
    print('YES')

else:
    print('NO')

frase_invertida = frase[::-1]

print(frase_invertida)
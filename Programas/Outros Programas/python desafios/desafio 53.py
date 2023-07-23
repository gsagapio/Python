frase = str(input('Digite uma frase: ')).strip().upper()
#.strip() tira os espaçoes entre as palavras
#.upper() as deixa maiúsculas na hora de comparar

palavras = frase.split()#divide as palavras e gera uma lista
junto = ''.join(palavras)#junta as palavras, junta a lista
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
   inverso += junto[letra]
print(junto, inverso)  
if inverso == junto:
   print('Temos um palindromo!')
else:
   print('A frase não é um palindromo')

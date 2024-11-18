# Verificar a faixa etária
idade = 20

if idade < 4:
    print("Bebê")
elif idade < 10:
    print("Criança")
elif idade < 14:
    print("Pré-adolescente")
elif idade < 19:
    print("Adolescente")
else:
    print("Adulto")

# Imprimir "Olá Mundo" 5 vezes
contador = 0

while contador < 5:
    print("Olá Mundo")
    contador += 1

# Solicitar nome até que o nome seja "Luiz"
while True:
    name = input('Digite seu nome: ')
    if name == 'Luiz':
        break

print("Obrigado")

# Verificar se o nome é "Gustavo" e solicitar senha
while True:
    print("Digite seu nome.")
    nome = input()
    
    if nome != 'Gustavo':
        continue  # Volta ao início do loop se o nome não for "Gustavo"
    
    print("Olá Gustavo, digite sua senha.")
    password = input()
    
    if password == '123':
        break  # Sai do loop se a senha estiver correta

print("Obrigado")
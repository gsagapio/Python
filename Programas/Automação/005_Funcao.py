#Função retorna nome

def hello(name):
    print('Olá', name)

print('Antes de chamar a função')
hello('Gustavo')
print('Depois de chamar a função')

#Função hora extra
def calcular_salario(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    
    if horas <= 40:
        salario = horas * taxa
    else:
        horas_ex = horas - 40
        salario = 40 * taxa + (horas_ex * (1.5 * taxa))
    
    return salario

str_horas = input('Digite a quantidade de horas trabalhadas: ')
str_taxa = input('Digite a taxa: ')
salario_calculado = calcular_salario(str_horas, str_taxa)

print('O valor do salario é: R$', salario_calculado)

#Função IMC

def calcula_imc(peso, altura):
    print(peso / altura ** 2)

calcula_imc(peso = 78, altura = 1.81)

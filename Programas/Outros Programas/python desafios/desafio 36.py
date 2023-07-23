print ('<=====EMPRÉSTIMO BANCÁRIO=====>')

valor = float(input('Qual o valor da casa que planeja comprar? R$ ')) 
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))

mensalidade = (valor / anos) / 12
limite = (salario / 100) * 30

if mensalidade > limite:
    print('A sua mensalidade é {:.2f}, isso ultrapassa o seu limite, sendo acima de 30 por cento do seu salario de {:.2f}.'.format(mensalidade, salario))
    print('EMPRÉSTIMO BANCÁRIO REPROVADO')

elif mensalidade <= limite: 
    print ('Para pagar uma casa de {:.2f} em {} anos, a prestação será de {:.2f}'.format(valor, anos, mensalidade))
    print('EMPRÉSTIMO APROVADO')

print('<=====PROCESSO FINALIZADO=====>')

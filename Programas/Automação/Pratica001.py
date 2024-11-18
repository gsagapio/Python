import random

secretNumber = random.randint(1, 20)
print('Estou pensanto em um numero de 1 a 20')

for tentativas in range(1, 7):
    print('Tente adivinhar o numero')
    guess = int(input())
    
    if guess < secretNumber:
        print('Sua tentatia foi muito baixa.')
    elif guess > secretNumber:
        print('Sua tentativa foi muito alta.')
    else:
        break

if guess == secretNumber:
    print('Muito bem, você acertou o número em ', str(tentativas), ' tentativas.')
else:
    print('Que pena, você não conseguiu acertar o número que era: ', str(secretNumber))

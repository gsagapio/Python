import  math
angulo = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O seno do ângulo {} é igual a {:.2f}'.format(angulo, sen))
print('O cosseno do ângulo {} é igual a {:.2f}'.format(angulo, cos))
print('A tangente do ângulo {} é igual a {:.2f}'.format(angulo, tan))
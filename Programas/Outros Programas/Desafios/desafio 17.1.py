import math
oposto = float(input('Digite o cateto oposto do triângulo retângulo: '))
adjacente = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hipotenusa = math.hypot(oposto, adjacente)

print('A hipotenusa do cateto oposto {} e do adjascente {} é igual a {}'.format(oposto, adjacente, hipotenusa))

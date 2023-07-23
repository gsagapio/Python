a = input("Informe o valor da variável A: ")
b = input("Informe o valor da variável B: ")

if (a>b):
    aux = a;
    a = b;
    b = aux;
print ("O valor da variável A agora é: ", a);
print("O valor da variável B agora é: ", b);

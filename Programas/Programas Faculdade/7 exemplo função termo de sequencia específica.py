#exemplo 7 Criar uma função que recebe um número n e retorna o n-ésimo termo da sequência de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + (fibonacci(n-2))
    
n = 9
fibonacciresult = fibonacci(n)
print("O", n, "termo da sequencia de Fibonacci é", fibonacciresult)
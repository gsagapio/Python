def division(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        print('Error: Invalid argument. Division by zero is not allowed.')
        return None
    
    except TypeError:
        print('Error: Invalid type. Please provide numerical values.')
        return None
    
    finally:
        print('Finalizando.')

# Testando a função division
print(division(33, 2))       # Saída: 16.5
print(division(12, 'a'))     # Saída: Error: Invalid type.
print(division(5, 0))        # Saída: Error: Invalid argument.
print(division(1, 3))        # Saída: 0.333...

def test(x):
    if not isinstance(x, int):
        raise TypeError('Only integers are allowed.')
    
    if x < 0:
        raise ValueError('Sorry, no numbers below zero.')

# Testando a função test
print(test(10))  # Saída: None (sem erro)

# Asserts
y = "hello"

assert y == "hello", "y should be 'hello'"  # Não gera erro
assert y == "goodbye", "y should be 'goodbye'"  # Gera erro: AssertionError
# 1. Recursão
# 2. Divisão e conquista
# 3. Programação dinâmica
# 4. Algoritmos gananciosos

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(900))
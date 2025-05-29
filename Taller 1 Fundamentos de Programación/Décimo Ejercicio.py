def próximo(n):
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return b

n = int(input("Ingrese un número: "))
print("El next es:", próximo(n))

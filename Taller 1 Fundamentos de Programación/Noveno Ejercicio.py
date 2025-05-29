masimomasimo = int(input("Ingrese un número: "))
a, b = 0, 1
print("Fibonacci menores o iguales a", masimomasimo, ":")
while a <= masimomasimo:
    print(a, end=" ")
    a, b = b, a + b

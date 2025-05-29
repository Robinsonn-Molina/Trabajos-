# Leemo el número 
n = int(input("Ingrese un número entero positivo: "))

# Miramos si es un cuadrado perfecto
i = 1
es_cuadrado = False

while i * i <= n:  # Probar cuadrados hasta que lleguemos a n
    if i * i == n:
        es_cuadrado = True
        break # El break por si se cumple la condición, entonces seguimo
    i += 1

# Mostramos el resultado
if es_cuadrado:
    print(f"{n} es un cuadrado perfecto, su raíz cuadrada es {i}.")
else:
    print(f"{n} NO es un cuadrado perfecto.")

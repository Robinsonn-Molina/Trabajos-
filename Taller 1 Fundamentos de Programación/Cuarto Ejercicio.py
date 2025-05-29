# Leemo los numerinhos 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Miramos si son ambos pares o ambos impares
if (a % 2 == b % 2):  
    # Calculamos el MCD con el método de Euclides (30 mins buscando)
    while b != 0:
        a, b = b, a % b  
    print(f"El MCD es: {a}")

else:  
    # Si no, guardamos los valores originales de a y b
    original_a = a
    original_b = b

    # Calculamos el MCD primero
    while b != 0:
        a, b = b, a % b  

    # Calcular el MCM
    mcm = (original_a * original_b) // a  
    print(f"El MCM es: {mcm}")

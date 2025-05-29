suma_pares = 0  # Acumulador 
contador_pares = 0  # Contador 
continuar = True  # Variable de control

print("Ingrese números enteros (Si no, escriba 'fin' para terminar):")

# Bucle de 'continuar'
while continuar:
    entrada = input("Ingrese un número: ") 
    if entrada == "fin":  # Si el usuario escribe "fin", en teoría se cambia la variable de control
        continuar = False
    else:
        numero = int(entrada)  # Pasamos la entrada a entero

        if numero % 2 == 0:  # Verificamos si es par
            suma_pares += numero  # Sumamos el número par
            contador_pares += 1  # Contamos el número par ingresado

# Miramos si hay pares antes de calcular la media
if contador_pares > 0:
    media_pares = suma_pares / contador_pares  # Calculamos la media
    print(f"La media de los números pares ingresados es: {media_pares:.2f}")
else:
    print("No se ingresaron números pares.")  # Si no hay pares, se imprime este mensaje

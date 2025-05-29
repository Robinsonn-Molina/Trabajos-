# Leemos el entero
n = int(input("Ingrese un número entero: "))

# Recorremo los números enteros desde 1 hasta n
for i in range(1, n + 1):
    mensaje = ""  # Guardamos la divisibilidad
    
    # Verificar divisibilidad por 2, 3 y 5
    if i % 2 == 0:
        mensaje += "Divisible por 2"
    if i % 3 == 0:
        mensaje += " y " if mensaje else ""  # Agregar "y" si tenemos un mensaje antes
        mensaje += "Divisible por 3"
    if i % 5 == 0:
        mensaje += " y " if mensaje else ""  # Agregar "y" si tenemos un mensaje antes
        mensaje += "Divisible por 5"

    # Imprimimo
    if mensaje:  # Si hay divisibilidad, mostramos el mensaje
        print(f"{i}. {mensaje}")
    else:  # Si no es divisible por 2, 3 o 5, solo imprimimos el número
        print(i)

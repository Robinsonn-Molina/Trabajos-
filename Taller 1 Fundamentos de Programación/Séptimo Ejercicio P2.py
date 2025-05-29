positivos = 0
negativos = 0
suma_positivos = 0
suma_negativos = 0

while True:
    numero = int(input("Introduce el número (0 para no finalizar): "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
        suma_positivos += numero
    else:
        negativos += 1
        suma_negativos += numero

promedio_positivos = suma_positivos / positivos if positivos > 0 else 0
promedio_negativos = suma_negativos / negativos if negativos > 0 else 0

print("\nResultados:")
print(f"Cantidad de positivos: {positivos}")
print(f"Promedio de positivos: {promedio_positivos}")
print(f"Cantidad de negativos: {negativos}")
print(f"Promedio de negativos: {promedio_negativos}")

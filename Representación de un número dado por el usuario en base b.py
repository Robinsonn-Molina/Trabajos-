numero = int(input("Ingresa un número decimal: "))
base = int(input("Ingresa la base (2-10): "))

if 2 <= base <= 10:
    resultado = ""
    while numero > 0:
        resultado = str(numero % base) + resultado
        numero //= base
    if resultado == "":
        resultado = "0"
    print(f"El número en base {base} es: {resultado}")
else:
    print("La base debe estar entre 2 y 10.")

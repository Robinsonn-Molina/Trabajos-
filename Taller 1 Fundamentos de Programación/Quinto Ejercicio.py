# Entrada 
num = int(input("Ingrese un número entero: "))

# Conversión a base 2
numero = num
resultado = ""
while numero > 0:
    residuo = numero % 2
    resultado = str(residuo) + resultado
    numero = numero // 2
print(f"Base 2 (Binario): {resultado if resultado != '' else '0'}")

# Conversión a base 4
numero = num
resultado = ""
while numero > 0:
    residuo = numero % 4
    resultado = str(residuo) + resultado
    numero = numero // 4
print(f"Base 4: {resultado if resultado != '' else '0'}")

# Conversión a base 8
numero = num
resultado = ""
while numero > 0:
    residuo = numero % 8
    resultado = str(residuo) + resultado
    numero = numero // 8
print(f"Base 8 (Octal): {resultado if resultado != '' else '0'}")

# Conversión a base 16
numero = num
resultado = ""
digitos = "0123456789ABCDEF"
while numero > 0:
    residuo = numero % 16
    resultado = digitos[residuo] + resultado
    numero = numero // 16
print(f"Base 16 (Hexadecimal): {resultado if resultado != '' else '0'}")

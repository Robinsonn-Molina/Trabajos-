numero = input("Ingrese un número: ")
resultado = ""

for i in range(len(numero)):
    cifra_entera = int(numero[i])
    suma = cifra_entera + 1
    if suma == 10:
        nueva_cifra = "0"
    else:
        nueva_cifra = str(suma)
    resultado += nueva_cifra

print("Número ready:", resultado)
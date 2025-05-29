frase = input("Frase aqui: ")
n = int(input("Orden de cesar: "))

paraseparar = " "
FraseN = ""
palabra = ""

for letra in frase:
    LetraOrdenada = ord(letra)
    if (65 < LetraOrdenada < 90) or (97 < LetraOrdenada  < 122):
        if 90 < (LetraOrdenada + n) < 96 or (LetraOrdenada + n) > 122:
            FraseN = FraseN + chr((LetraOrdenada + n) - 26)
        else:
            Frasen = FraseN + chr((LetraOrdenada + n))
    else:
        FraseN = FraseN + letra

print(FraseN)


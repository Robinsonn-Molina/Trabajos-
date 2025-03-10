frase = input("Ingresa una frase: ")

palabra = ""
lista_palabras = []
indice = 0  # Contador M

for caracter in frase:
    if caracter == " ":
        if palabra != "":
            lista_palabras += [palabra]  # Probar si el += me quedo bien 
            palabra = ""
    else:
        palabra += caracter

if palabra:  # Agregar la última palabra si no termina en espacio creo
    lista_palabras += [palabra]

print("Palabras separadas:", lista_palabras)

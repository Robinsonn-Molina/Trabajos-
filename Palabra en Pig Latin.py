palabra = input("Ingrese una palabra: ")

if palabra[0] in "aeiouAEIOU": #revisar si use adecuadamente el 0 en llaves y el in 
    resultado = palabra + "way"
else:
    resultado = palabra[1:] + palabra[0] + "ay"

print("Palabra en Pig Latin:", resultado)

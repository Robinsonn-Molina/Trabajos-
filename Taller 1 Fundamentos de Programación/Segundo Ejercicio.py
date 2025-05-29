n = int(input("Ingrese un número mayor que 2: "))
encontrado = False  # La variable de controol

while not encontrado: #30 mins buscando el not 
    es_primo = True
    i = 2
    while i * i <= n and es_primo:
        if n % i == 0:
            es_primo = False
        i += 1
    
    if es_primo:
        encontrado = True  # Decimos que encontramos el primo
    else:
        n -= 1  # Vamos pa atrás buscando en el número anterior

print("El número primo más cercano es:", n)

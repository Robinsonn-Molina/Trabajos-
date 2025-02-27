m = int(input())
penultimo = 0
ultimo = 1
i = 2
suma = ultimo + penultimo
print(penultimo)
print(ultimo)
while suma < m:
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    if ultimo < m:
        print(ultimo)
    i = i + 1

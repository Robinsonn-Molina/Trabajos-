n = int(input("Ingresa un número límite: "))

lista = [i for i in range(n + 1) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0]

print("Números divisibles por 2, 3 o 5:", lista)

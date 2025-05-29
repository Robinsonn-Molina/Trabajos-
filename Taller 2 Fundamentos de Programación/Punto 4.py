def minmultcuad(n):
    x = 1
    i = 2
    while i * i <= n:
        cont = 0
        while n % i == 0:
            n //= i
            cont += 1
        if cont % 2 == 1:
            x *= i
        i += 1
    if n > 1:
        x *= n
    return x

casos = int(input("Cuántos casos: "))
for _ in range(casos):
    num = int(input("Número: "))
    print(minmultcuad(num))


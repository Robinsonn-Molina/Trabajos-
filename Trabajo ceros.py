n = int(input("Introduzca n: "))
nbak = n
m = 0
factor = 1
while n > 0 :
    r = n % 2
    n = n // 10
    m = r * factor + m
    factor = factor * 100 
print(str(m) + " -> " + str(nbak))
print(f"{nbak} -> {m}")
print("{} -> {}".format(m, nbak))

def fx(x, c):
    r = 0
    for i in range(len(c)):
        r += c[i] * x**i
    return r

def area(c):
    a = 0
    dx = 1 / 1000
    for i in range(1000):
        x = i * dx
        y = fx(x, c)
        if y < 0: y = 0
        if y > 1: y = 1
        a += y * dx
    return a

while True:
    ent = input()
    if ent == "0":
        break
    num = list(map(float, ent.split()))
    g = int(num[0])
    cof = num[1:]
    a = area(cof)
    b = 1 - a
    if abs(a - b) <= 0.001:
        print("JUSTO")
    else:
        print("CAIN" if a > b else "ABEL")

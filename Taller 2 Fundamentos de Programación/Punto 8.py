def rom(n):
    v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    r = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res = ''
    for i in range(len(v)):
        while n >= v[i]:
            res += r[i]
            n -= v[i]
    return res

while True:
    n = int(input())
    if n == 0:
        break
    print(rom(n))

cadena = "abcfga"
N = 5

carunic = []
[carunic.append(c) for c in cadena if c not in carunic]

if N > len(carunic):
    print("Error: N mayor que caracteres únicos.")
else:
    sel = carunic[:N]
    print(f"Caracteres únicos: {''.join(carunic)}")
    print(f"Elementos usaos: {''.join(sel)}")

    def genperm(paso, usaos):
        if len(paso) == len(sel):
            print(''.join(paso))
            return
        for i in range(len(sel)):
            if not usaos[i]:
                usaos[i] = True
                paso.append(sel[i])
                genperm(paso, usaos)
                paso.pop()
                usaos[i] = False

    genperm([], [False]*len(sel))

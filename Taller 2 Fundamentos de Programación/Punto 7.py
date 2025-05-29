while True:
    n = int(input())
    if n == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(n)]
    sup = inf = True
    for i in range(n):
        for j in range(n):
            if j > i and mat[i][j] != 0:
                sup = False
            if j < i and mat[i][j] != 0:
                inf = False
    print("SI" if sup or inf else "NO")


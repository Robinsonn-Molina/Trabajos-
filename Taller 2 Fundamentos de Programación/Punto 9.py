nums = list(map(int, input().split()))
s = int(input())
v = set()
us = set()

for a in nums:
    b = s - a
    p = (min(a,b), max(a,b))
    if b in v and p not in us:
        print(f"{p[0]}, {p[1]}")
        us.add(p)
    v.add(a)

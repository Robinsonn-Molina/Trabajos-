import math, random, matplotlib.pyplot as plt

x = float(input("x: "))
y = float(input("y: "))
vec = [x, y]

def unir():
    ang = random.uniform(0, 2*math.pi)
    return [math.cos(ang), math.sin(ang)]

def proy(v, u):
    esc = v[0]*u[0] + v[1]*u[1]
    return [esc*u[0], esc*u[1]]

u1 = unir()
u2 = unir()
p1 = proy(vec, u1)
p2 = proy(vec, u2)

plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color='b', label='vec')
plt.quiver(0, 0, p1[0], p1[1], angles='xy', scale_units='xy', scale=1, color='r', label='p1')
plt.quiver(0, 0, p2[0], p2[1], angles='xy', scale_units='xy', scale=1, color='g', label='p2')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
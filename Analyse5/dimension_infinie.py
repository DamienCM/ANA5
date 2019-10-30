import numpy as np
import matplotlib.pyplot  as plt
import os


# Question 1
def integrale(f, a, b, n=10 ** 6):
    X = np.linspace(a, b, n)
    Y = f(X)
    S = np.sum(Y[1:-1]) + (Y[0] + Y[-1]) / 2
    S = S * (b - a) / n
    return S


def derivee(f, xo, dt=10 ** -6):
    return (f(xo + dt) - f(xo - dt)) / (2 * dt)


def F(f):
    def f_longueur(x):
        return np.sqrt(1 + derivee(f, x) ** 2)

    return integrale(f_longueur, -1, 1)


def G(f):
    return integrale(f, -1, 1)


# Question 2

def fonction_1(x):
    return 1 - x ** 2


def fonction_2(x):
    return 1 - x ** 4


def fonction_3(x):
    return np.sin(np.pi / 2 * (1 - x))


def fonction_4(x):
    return np.sqrt(1.001 - x ** 2)


X = np.linspace(-1, 1, 10 ** 6)

Y1 = fonction_1(X)
Y2 = fonction_2(X)
Y3 = fonction_3(X)
Y4 = fonction_4(X)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

ax1.plot(X, Y1, label="f(x) = 1 - x ^ 2")
ax1.axis('equal')
F1 = F(fonction_1)
G1 = G(fonction_1)
fig1.suptitle("F=" + str(round(F1, 5)) + "     G=" + str(round(G1, 5)) + "   G - F = " + str(round(G1 - F1, 5)))
ax1.grid()
fig1.legend(loc='lower left')
fig1.savefig('./out/fonction_1')

ax2.plot(X, Y2, label="f(x) = 1 - x ^ 4")
ax2.axis('equal')
F2 = F(fonction_2)
G2 = G(fonction_2)
fig2.suptitle("F=" + str(round(F2, 5)) + "     G=" + str(round(G2, 5)) + "   G - F = " + str(round(G2 - F2, 5)))
ax2.grid()
fig2.legend(loc='lower left')
fig2.savefig('./out/fonction_2')

ax3.plot(X, Y3, label='sin(pi / 2 * (1 - x))')
ax3.axis('equal')
F3 = F(fonction_3)
G3 = G(fonction_3)
fig3.suptitle("F=" + str(round(F3, 5)) + "     G=" + str(round(G3, 5)) + "   G - F = " + str(round(G3 - F3, 5)))
ax3.grid()
fig3.legend(loc='lower left')
fig3.savefig('./out/fonction_3')

ax4.plot(X, Y4, label='sqrt(1 - x ^ 2)')
ax4.axis('equal')
F4 = F(fonction_4)
G4 = G(fonction_4)
fig4.suptitle("F=" + str(round(F4, 5)) + "     G=" + str(round(G4, 5)) + "   G - F = " + str(round(G4 - F4, 5)))
ax4.grid()
fig4.legend(loc='lower left')
fig4.savefig('./out/fonction_4')

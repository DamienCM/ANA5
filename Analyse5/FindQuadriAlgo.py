import math
from sympy import *
import matplotlib.pyplot as plt
import tikzplotlib
import numpy as np
#On travaille sur R2, on commence par initialiser notre coté qui est égal à 1.

#Norme euclidienne
def Norme2(a,b):
    Xa, Ya, Xb, Yb = a[0], a[1], b[0], b[1]
    return math.sqrt((Xa-Xb)**2+(Ya-Yb)**2)

class Segment:
    def __init__(self,A,B):
        self.dep = A
        self.arr = B
    def milieu(self):
        return (self.dep[0] + self.arr[0])/2
    def longeur(self):
        return Norme2(self.dep,self.arr)
    def XDep(self):
        return self.dep[0]
    def YDep(self):
        return self.dep[1]
    def XArr(self):
        return self.arr[0]
    def YArr(self):
        return self.arr[1]

class Cercle:
    def __init__(self,C,R):
        self.centre = C
        self.rayon = R
    def equation(self):
        x, y = symbols('x y')
        return (x-self.centre[0])**2 + (y-self.centre[1])**2 - self.rayon**2

def TrouveTriangle(segL1,cote):
    s = Segment(segL1[0], segL1[1])
    coord = [[s.XDep(),s.YDep()],[s.XDep(),s.YDep()-cote],[s.XArr(),s.YArr()]]
    coord.append(coord[0])
    xs,ys = zip(*coord)
    circle = plt.Circle((1,-2),3,fill=False)
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    ax.plot(xs, ys)
    x1, y1 = [3/2, 3.9], [-1/2, -1.3]
    plt.plot(x1, y1, marker='o')
    ax.plot((1), (-2), 'o', color='y')
    plt.axis("equal")
    plt.grid(True)
    tikzplotlib.save("test.tex")
    plt.show()
    return xs,ys

def TrouveQuadri(segL1,cote):
    x, y = symbols("x y")
    s = Segment(segL1[0],segL1[1])
    c = Cercle((segL1[0]),cote)
    solution = solve(c.equation(),y)[0].subs(x,s.milieu())
    coord = [[c.centre[0],c.centre[1]],[s.milieu(),solution],[2,1]]
    coord.append(coord[0])
    xs, ys = zip(*coord)
    plt.figure()
    plt.plot(xs,ys)
    plt.axis("equal")
    plt.grid(True)
    tikzplotlib.save("test.tex")
    plt.show()
    return solution


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
    return np.sqrt(1-x**2)

X = np.linspace(-1, 1, 50)

plt.figure()
F1 = F(fonction_1)
G1 = G(fonction_1)
plt.plot(X,fonction_1(X))
plt.axis("equal")
plt.grid(True)
tikzplotlib.save("test.tex")
plt.show()



import numpy as np
import matplotlib.pyplot as plt


def integrale_trapeze(a, b, f, n=10 ** 6):
    X = np.linspace(a, b, n)
    Y = f(X)
    I = np.sum(Y) - 0.5 * (Y[0] + Y[-1])
    I = I * (b - a) / n
    return I


def derivee(f, a, n=10 ** -6):
    return (f(a + n) - f(a - n)) / (2 * n)




def r(t):
    return None


def teta(t):
    return None


def L(r):
    def integrande_L(t):
        return (r(t) ** 2 + derivee(r, t) ** 2) ** 0.5

    return integrale_trapeze(0, 2 * np.pi, integrande_L)


def A(r):
    def integrande_A(t):
        return r(t) ** 2

    return 0.5 * integrale_trapeze(0, 2 * np.pi, integrande_A)


# On determine a,b,c,d
# a=1/2pi
# puis numeriquement b,c,d

def r_a(t):
    return 1 + t - t


a = 1 / (2 * np.pi)


def r_b(t):
    return 2 + np.cos(t)


b = 1 / L(r_b)


def r_c(t):
    return 2 + np.cos(5 * t)


c = 1 / L(r_c)


def r_d(t):
    return 1 + t ** 2 * (2 * np.pi - t) ** 2


d = 1 / L(r_d)


figs, axs = plt.subplots(4,1,sharex=True,figsize=(8,15))
X = np.linspace(0, 2 * np.pi, 10 ** 6)
Y_a = a * r_a(X)
Y_b = b * r_b(X)
Y_c = c * r_c(X)
Y_d = d * r_d(X)
Ys=[Y_a,Y_b,Y_c,Y_d]

As=[round(a**2*A(r_a),5),round(b**2*A(r_b),5),round(c**2*A(r_c),5),round(d**2*A(r_d),5)]

titles=["a","b(2+cos(t))","c(2+cos(5t))","d(1+t^2(2pi-t)^2)"]
labels=["a="+str(round(a,5))+"\nL(r)=1"+"\nA(r)="+str(As[0]), "b="+str(round(b,5))+"\nL(r)=1"+"\nA(r)="+str(As[1]), "c="+str(round(c,5))+"\nL(r)=1"+"\nA(r)="+str(As[2]), "d="+str(round(d,5))+"\nL(r)=1"+"\nA(r)="+str(As[3])]



for i in range(4):
    axs[i].plot(X,Ys[i],label=labels[i])
    axs[i].set_title("r(t)=" + titles[i])
    axs[i].legend(loc="upper right")
    axs[i].grid()
    axs[i].set_yticks(np.array([0, 0.1, 0.2, 0.3]))
axs[-1].set_xlabel("t")
plt.subplots_adjust(hspace=0.5)
plt.savefig(".\out\courbe_fermee_obtimale_1.pdf")

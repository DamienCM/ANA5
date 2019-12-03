import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-1, 1, 5000)
n=300
Lambda = np.geomspace(10**-8,1, n)
Lambda=np.append(Lambda,np.linspace(10**-8,1,n))
Lambda=np.sort(Lambda,axis=None)
temp=np.ones(2*n)
Lambda=Lambda-temp
Lambda=Lambda[1:-1]
Lambda=Lambda[Lambda != 0]


def f(x, L):
    return (((L * x + 1) * (L * x - 1) * np.sqrt(-1 / (L ** 2 * x ** 2 - 1))) - (L ** 2 - 1) * np.sqrt(
        -1 / (L ** 2 - 1))) / L


for i in range(len(Lambda)):
    L = Lambda[i]
    fig, ax = plt.subplots(figsize=(7,7))
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))
    Y = f(X, L)
    ax.set_xlabel("x")
    ax.set_ylabel('y')
    ax.plot(X, Y, label="Lambda=" + str(round(L,5)))
    ax.grid()
    fig.legend(loc=4)
    fig.suptitle("Courbe fermée optimale pour une longueur fixée",size=15)
    plt.savefig("./out/anim/fig" + str(i) + ".png")
    plt.close(fig)
    print(i)
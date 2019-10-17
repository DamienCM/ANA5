#importation des modules
from math import sqrt
from sympy import diff, symbols, latex

#la fonction qui permet de calculer le périmètre d'un triangle
def P(a,b,c):
    return a + b + c

#la fonction qui permet de calculer l'Aire d'un triangle (Héron), s est le demi-périmètre

def A(a,b,c):
    s = P(a,b,c) / 2
    try:
        return sqrt(s*(s-a)*(s-b)*(s-c))
    except:
        return "Ce n'est pas un triangle"

#calcul gradient fonction 3 variable
def grad(f):
    a, b, c, s = symbols('a b c s')
    scalaires = []
    for i in a, b, c:
        lat = latex(diff(str(f), i))
        scalaires.append(lat)
        print(lat)
    return scalaires

print(grad("sqrt(s*(s-a)*(s-b)*(s-c))"))


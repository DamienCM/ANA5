# importation des modules
from math import sqrt
from Outils import grad


# la fonction qui permet de calculer le périmètre d'un triangle
def P(a, b, c):
	return a + b + c


# la fonction qui permet de calculer l'Aire d'un triangle (Héron), s est le demi-périmètre
def A(a, b, c):
	s = P(a, b, c) / 2
	try:
		return sqrt(s * (s - a) * (s - b) * (s - c))
	except:
		return "Ce n'est pas un triangle"


#calcul du grad d'une fonction de 3 variables
print(grad("sqrt(s*(s-a)*(s-b)*(s-c))","a","b","c"))

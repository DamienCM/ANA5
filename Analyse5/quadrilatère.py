from Outils import grad

#cas 2
#calcul du grad d'une fonction de 5 variables
#print(grad("sqrt(s*(s-x)*(s-w)*(s-d))+sqrt(t*(t-y)*(t-z)*(t-d))","x","y","z","w","d"))

#cas 3
#calcul du grad d'une fonction de 4 variables
print(grad("sqrt((s-x)*(s-y)*(s-z)*(s-1))","x","y","z","d"))
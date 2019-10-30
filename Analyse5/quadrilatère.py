from Analyse5.Outils import grad

# calcul du grad d'une fonction de 5 variables
print(grad("sqrt(s*(s-x)*(s-w)*(s-d))+sqrt(t*(t-y)*(t-z)*(t-d))", "x", "y", "z", "w", "d"))

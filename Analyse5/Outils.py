from sympy import diff, latex, Symbol


# calcul gradient fonction n variables
def grad(f, *argv):
    arguments = []
    for arg in argv:
        arg = Symbol(str(arg))
        arguments.append(arg)
    scalaires = []
    for i in arguments:
        lat = latex(diff(str(f), i))
        scalaires.append(lat)
        print(lat)
    return scalaires

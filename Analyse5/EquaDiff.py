from sympy import *

f = Function('f')
k = Function('k')
x = Symbol('x')

def F(exp):
    return Integral(sqrt(1 + diff(exp)**2),(x,-1,1))


print(latex(F(f(x))))
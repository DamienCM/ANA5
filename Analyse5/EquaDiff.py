from sympy import *
from sympy.parsing.sympy_parser import parse_expr
y = Function('y')
k = Function('\eta')
x = Symbol('x')
c = Symbol('c')

def F(expr):
    return Integral(sqrt(1 + diff(expr)**2),(x,-1,1))
def IPP(u,vP):
    terme1,terme2 = u*vP,u.diff(x)*vP
    return terme1.subs(x,1)-terme1.subs(x,-1)-Integral(terme2,(x,-1,1))

diff = latex(F(y(x)+k(x))-F(y(x)))
u = y(x).diff(x)/(sqrt(1+(y(x).diff(x))**2))
vP = k(x)
d = IPP(u,vP)
d = d.subs(k(1),0)
d = d.subs(k(-1),0)
print(dsolve(Derivative(y(x), (x, 2))/sqrt(Derivative(y(x), x)**2 + 1) -
              Derivative(y(x), x)**2*Derivative(y(x), (x, 2))/(Derivative(y(x), x)**2 + 1)**(Rational(3,2))-2,y(x),ics={y(-1):0, y(1):0}))

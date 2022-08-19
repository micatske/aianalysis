from sympy import *
import inspect
from fractions import Fraction
init_printing()


f,g=Function("f",real=True),Function("g",real=True)
x=Symbol("x")
xi=Symbol("xi")
F_f=Function("fhat")
s=Symbol("s")
p=Symbol("p")



class Lp(Function):
    nargs = (1, 2)
    @classmethod
    def eval(cls, p,f):
        if p.is_Number:
            if p.is_zero:
                return oo
            elif p is S.Infinity:
                return maximum(f(x),x) #TBD
        else:
                return  (integrate(Abs(f(x))**p,x))**(1/p)
        

class F_Hs(Function):
    nargs = (1, 2)
    @classmethod
    def eval(cls, s,Ff):
        if s.is_Number:
            if s.is_zero:
                return oo
            elif s is S.Infinity:
                return maximum(Ff(xi),xi) #TBD
        else:
                return ( integrate(Abs(xi)**(2*s) * Abs(Ff(xi))**2,xi))**(1/2)
            
class F_HS(Function):
    nargs = (1, 2)
    @classmethod
    def eval(cls, s,Ff):
        if s.is_Number:
            if s.is_zero:
                return oo
            elif s is S.Infinity:
                return maximum(Ff(xi),xi) #TBD
        else:
                return ( integrate((1+Abs(xi)**2)**(s) * Abs(Ff(xi))**2,xi))**(1/2)
from sympy import *
import inspect
from fractions import Fraction
init_printing()

s=Symbol("s")
p=Symbol("p")
f=Symbol("f")

class Lp(Function):
    @classmethod
    def eval(cls, p, f):
       pass

    def _latex(self, printer):
        p, f = self.args
        _p, _f = printer._print(p), printer._print(f)
        return r'\left \| %s \right \|_{L^{%s}}' % (_f, _p)
    
class hom_Hs(Function):
    @classmethod
    def eval(cls, s, Ff):
        pass
    def _latex(self, printer):
         s,Ff = self.args
         _s,_Ff = printer._print(s), printer._print(Ff)
         return r'\left \|  %s \right \|_{\dot{H}^{%s}}' % (_Ff,_s)
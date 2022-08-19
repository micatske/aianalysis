from sympy import *
f,g=Function("f",real=True),Function("g",real=True)
x=Symbol("x")

class Lp(Function):
    @classmethod
    def eval(cls, p):
        if p.is_Number:
            if p.is_zero:
                return oo
            elif p is S.Infinity:
                return maximum(Lp(x),x)
            

    def _eval_is_real(self):
        return self.args[0].is_real

p=2
p=Symbol("p")
L=Function("lp",real=True)(p)
L=integrate(abs(f(x))**p, x)
print(lp)
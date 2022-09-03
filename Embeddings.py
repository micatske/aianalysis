class Sobolev_Embed(Function):
    @classmethod
    def eval(cls, k, p,q,l ,f):
        pass
    def _latex(self, printer):
         k,p,q,l,f = self.args
         _k,_p,_q,_l,_f = printer._print(k),printer._print(p), printer._print(q),printer._print(l),printer._print(f)
         if k==1 and l==0:
             return r'\left \|  %s \right \|_{L^{ %s *}} \leq \left \|  %s \right \|_{W^{1,%s}}' % (_f,_p,_f,_p)
         if (1/p-1/q+(k-l)/n==0):
             return r'\left \|  %s \right \|_{W^{%s,%s}} \leq \left \|  %s \right \|_{W^{%s,%s}}' % (_f,_l,_q,_f,_k,_p)
         if n<p*k and q+l==k-n/p:
             return r'\left \|  %s \right \|_{C^{%s,%s}} \leq \left \|  %s \right \|_{W^{%s,%s}}' % (_f,_q,_l,_f,_k,_p)
             

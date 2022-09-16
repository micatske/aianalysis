# aimath

The project is designed to automatically estimate functions in symbolic form
---
## Function Spaces

We define function spaces $L^p$, $W^{k,p}$, $\dot H^s$, $H^s$, $C^{r,\alpha}$ by using the sympy, each of then taking a function symbol and parameter as input and output their corresponding norms 

## Sobolev Embedding

We build the [Sobolev inequality] (https://en.wikipedia.org/wiki/Sobolev_inequality) for the. Here we just need to input our function and it will output all possible embedding spaces. As a common rule. We know that they are in a linear realtion. So we just pick 10 possible pairs where each pairs are ratioal numbers.


## Para Product 

We build the Bony's Paraproduct decomposition (https://www.math.ucla.edu/~tao/247b.1.07w/notes6.pdf). We include the high-high, low-high, low-low paraproduct. Moreoever, we also include the usueful operator $\nabla$ and $\triangle$ for the function. The paraproduct can be used with the Sobolev Embedding and Holder inequality to estimate functions.

For instance, if we call
```
Paraproduct(nabla*f,lap*g)
```
we get

$$
\\sum_{k=-\\infty}^{\\infty} 2^{3 k} P_{k}f P_{k}g + \\sum_{\\substack{-\\infty \\leq j \\leq k - 10\\\\-\\infty \\leq k \\leq \\infty}} 2^{j} 2^{2 k} P_{j}f P_{k}g + \\sum_{\\substack{-\\infty \\leq j \\leq k - 10\\\\-\\infty \\leq k \\leq \\infty}} 2^{2 j} 2^{k} P_{j}g P_{k}f
$$


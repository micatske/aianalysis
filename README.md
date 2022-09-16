# aimath

The project is designed to automatically estimate functions in symbolic form
---
## Function Spaces

We define function spaces $L^p$, $W^{k,p}$, $\dot H^s$, $H^s$, $C^{r,\alpha}$ by using the sympy, each of then taking a function symbol and parameter as input and output their corresponding norms 

## Sobolev Embedding

We build the [Sobolev inequality] (https://en.wikipedia.org/wiki/Sobolev_inequality) for the. Here we need to input our function, which will output all possible embedding spaces as a common rule. We know that they are in a linear relation. So we pick 10 possible pairs where each pair are rational numbers.


## Para Product 

We build the Bony's Paraproduct decomposition (https://www.math.ucla.edu/~tao/247b.1.07w/notes6.pdf). We include the high-high, low-high, and low-high paraproduct. Moreover, we also have the helpful operator $\nabla$ and $\triangle$ build-in. The paraproduct can be used with the Sobolev Embedding and Holder inequality to estimate functions.

For instance, if we want to calculate the paraproduct of 

$$
\nabla f * \triangle g= \pi_{hh}(\nabla f * \triangle g)+ \pi_{hl}(\nabla f * \triangle g)+\pi_{lh}(\nabla f * \triangle g),
$$

we can simply call:
```
Paraproduct(nabla*f,lap*g)
```

The output will be in latex as the following:

$$
\\sum_{k=-\\infty}^{\\infty} 2^{3 k} P_{k}f P_{k}g + \\sum_{\\substack{-\\infty \\leq j \\leq k - 10\\\\-\\infty \\leq k \\leq \\infty}} 2^{j} 2^{2 k} P_{j}f P_{k}g + \\sum_{\\substack{-\\infty \\leq j \\leq k - 10\\\\-\\infty \\leq k \\leq \\infty}} 2^{2 j} 2^{k} P_{j}g P_{k}f
$$


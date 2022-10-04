# aimath

The project is designed to automatically estimate functions in symbolic form
---
## Function Spaces

We define function spaces $L^p$, $W^{k,p}$, $\dot H^s$, $H^s$, $C^{r,\alpha}$ by using the sympy, each of then taking a function symbol and parameter as input and output their corresponding norms.

For instance, we call 

```
Lp(p,f)
```

to define the standard $L^p$ space for function $f$.

## Sobolev Embedding

We build the [Sobolev inequality] (https://en.wikipedia.org/wiki/Sobolev_inequality) for the. Here we need to input our function, which will output all possible embedding spaces as a common rule. We know that they are in a linear relation. So we pick 10 possible pairs where each pair are rational numbers.

For $f$ in space $W^{k,p}(\mathbb{R}^n)$, we call 

```
Sobolev_Embed_auto(k,p,n,f)
```
to get a list of embedded spaces.

Example: For $f \in W^{2,2}(\mathbb{R})$, we call

```
Sobolev_Embed_auto(2,2,1,f**2)
```

And we have 

$$
\\left[ \\left \\|  f^{2} \\right \\|_{C^{0,\\frac{3}{2}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{1}{6},\\frac{4}{3}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{1}{3},\\frac{7}{6}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{1}{2},1}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{2}{3},\\frac{5}{6}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{5}{6},\\frac{2}{3}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{1,\\frac{1}{2}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{7}{6},\\frac{1}{3}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{4}{3},\\frac{1}{6}}}, \\  \\left \\|  f^{2} \\right \\|_{C^{\\frac{3}{2},0}}\\right]
$$


For $f \in W^{2,2}(\mathbb(\R)^4)

```
Sobolev_Embed_auto(2,2,4,f)
```

We have

$$
\\left[ \\left \\|  f \\right \\|_{W^{\\frac{1}{25},100}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{25}{97},\\frac{450}{29}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{39}{82},\\frac{757}{90}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{52}{75},\\frac{75}{13}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{41}{45},\\frac{180}{41}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{35}{31},\\frac{287}{81}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{101}{75},\\frac{199}{67}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{97}{62},\\frac{225}{88}}}, \\  \\left \\|  f \\right \\|_{W^{\\frac{139}{78},\\frac{101}{45}}}, \\  \\left \\|  f \\right \\|_{W^{2,2}}\\right]
$$
## Para Product 

We build the [Bony's Paraproduct decomposition](https://www.math.ucla.edu/~tao/247b.1.07w/notes6.pdf). We include the high-high, low-high, and low-high paraproduct. Moreover, we also have the helpful operator $\nabla$ and $\triangle$ build-in. The paraproduct can be used with the Sobolev Embedding and Holder inequality to estimate functions.

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


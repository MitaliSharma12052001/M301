# <a name="d1">  Definition 1 </a>

**Complete metric space**:

every **cauchy** sequence **converges** in the space.



# <a name="t1"> Theorem 1</a>

## proposition

 $\mathbb{R}$  is a [complete](#d1) metric space 

## proof



### Claim 1

  $\{x_{n}\} _ {1}^\infty$  is bounded 





#### pf



for  $\epsilon=1 \gt 0$  $\exists $ N $\in \mathbb{N}$ st $\forall$ $m,n \ge N$ we have $|x_n - x_m|lt 1$

in particular,



$|x_n - x_N|\lt 1 $ $\implies$ $x_N-1\lt x_n\lt x_N+1$ $\forall$  $n \ge N$

set $a:=\min\{x_1,x_2,\dots,x_{N-1},x_N-1\}$ , $b:=\max\{x_1,x_2,\dots,x_{N-1},x_N+1\}$

therefore $a\le x_n\le b \ \forall n \in \mathbb{N}$ , i.e., $\{x_n\}$ is bounded.



### Claim 2

 $\{x_{n}\} _ {1}^\infty$ converges to the same limit as its convergent subsequences obtained from **Bolzanno-Weirsstrass Thm** 

#### pf



Let $\epsilon\gt 0$ 

by cauchy-ness, $\exists N_0$ st $\forall m,n\ge N_0$ $|x_m-x_n|\lt \epsilon/2$

by convergence of the subsequence $\{x_{n_k}\}$ to $x$ , $\exists K_0$ st $\forall K\ge K_0$ $|x-x_{n_k}|\lt \epsilon/2$

let $K_1$ be such that $n_{K_1}\ge N_0$ , now set $K=\max\{K_0,K_1\}$ and $N=n_K=\max\{n_{K_1}\,n_{K_0}\}\ge N_0$

now, $|x-x_n|=|x-x_N+x_N-x_n|\le |x-x_N| + |x_{n_K}-x_n| \lt \epsilon/2+\epsilon/2 =\epsilon$ , $\forall n\ge N$

this proves that the sequence converges in $\mathbb{R}$





# <a name="t2"> Theorem 2</a>

## proposition

 $\{\Sigma_1^n\frac{1}{k} - \ln(n)\} _ {n=1}^\infty$ converges 

## proof

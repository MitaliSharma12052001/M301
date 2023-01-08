# <a name="d1"> Definition 1 </a>
**Complete metric space**
every **cauchy** sequence **converges** in the space.

# <a name="t1">Theorem 1</a>
## proposition
 $\mathbb{R}$ is a [complete](#d1) metric space 
## proof

### Claim 1
  $\{x_{n}\} _ {1}^\infty$ is bounded 


#### pf

for  $\epsilon=1 > 0$ $\exists $N $\in \mathbb{N}$st $\forall$$m,n \ge N$we have $|x_n - x_m|<1$
in particular,

$|x_n - x_N|<1 $$\implies$$x_N-1<x_n<x_N+1$$\forall$ $n \ge N$
set $a:=\min\{x_1,x_2,\dots,x_{N-1},x_N-1\}$, $b:=\max\{x_1,x_2,\dots,x_{N-1},x_N+1\}$
therefore $a\le x_n\le b \ \forall n \in \mathbb{N}$, i.e., $\{x_n\}$is bounded.

### Claim 2
 $\{x_{n}\} _ {1}^\infty$ converges to the same limit as its convergent subsequences obtained from **Bolzanno-Weirsstrass Thm** 
#### pf

Let $\epsilon>0$





# <a name="t2">Theorem 2</a>
## proposition
$\{\Sigma_1^n\frac{1}{k} - \ln(n)\} _ {n=1}^\infty$ is bounded 
## proof

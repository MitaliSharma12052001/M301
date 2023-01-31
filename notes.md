# Complete metric space
every **cauchy** sequence **converges** in the space.

# Completness of $\mathbb{R}$
## proposition
 $\mathbb{R}$  is a complete metric space 
## proof

### Claim 1
  $\{x_{n}\} _ {1}^\infty$  is bounded 


#### pf

for  $\epsilon=1 \gt 0$  $\exists$ N $\in \mathbb{N}$ st $\forall$ $m,n \ge N$ we have $|x_n - x_m|\lt 1$
in particular,

$|x_n - x_N|\lt 1$ $\implies$ $x_N-1\lt x_n\lt x_N+1$ $\forall$  $n \ge N$
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


# Divergence of the harmonic series
## proposition
 $\{x_n\}=\{\Sigma_1^n\frac{1}{k} - \ln(n)\} _ {n=1}^\infty$ converges  with the rate $\gamma$ 
## proof
### claim 1
$x_n=\Sigma_{k=1}^{n-1}(\frac{1}{k}-log(\frac{k+1}{k}))+\frac{1}{n}$
### claim 2
$\frac{1}{k}-log(\frac{k+1}{k})=\int_0^{1/k}\frac{t}{1+t}dt$
### bounds
$\frac{1}{2k(k+1)}=\int_0^{1/k}\frac{t}{1+\frac{1}{k}}dt \le \int_0^{1/k}\frac{t}{1+t}dt \le \int_0^{1/k}\frac{t}{1+0}dt=\frac{1}{2k^2}$

which gives

$\frac{1}{n}+\Sigma_{k=1}^{n-1}\frac{1}{2k(k+1)}\le x_n \le \frac{1}{n}+\Sigma_{k=1}^{n-1}\frac{1}{2k^2} $

so that

$\frac{\pi^2}{12}-\frac{1}{2}\le liminf x_n \le limsup x_n \le \frac{\pi^2}{12}$, 

giving $x_n$ is bounded.
### monotonicity
also, ${x_n}$ is decreasing, because

$x_{n+1}-x_n=$ $\frac{1}{n+1}$ $-log(1-\frac{1}{n+1})$ $ =\frac{1}{n+1}-(\frac{1}{n+1}+ \frac{1}{2(n+1)^2}+\dots)\lt 0$

### Euler's Constant
now $x_n$ converges, to say $\gamma$ $\in [\frac{\pi^2}{12} -\frac{1}{2}, \frac{\pi^2}{12}]$

so that $\frac{1}{n}$ diverges like $\gamma+log(n)$

# Some Inequalities
## Cauchy Inequality
### proposition
for two vectors $\mathbf{x},\mathbf{y}$ in $\mathbb{R}^n$ or $\mathbb{C}^n$
we have $\Sigma|x_iy_i|\le ||\mathbf{x}||||\mathbf{y}||$ , in the standard metric, and it's induced norm.
### proof

first note that for any reals $a\ge 0, b\ge 0$ we have $(a-b)^2\ge 0$

that is $a^2+b^2\ge 2ab$

now, putting $a_i:=\frac{|x_i|}{||\mathbf{x}||}$ and $b_i:=\frac{|y_i|}{||\mathbf{y}||}$

we get $a_ib_i\le$  $\frac{1}{2}$ $(\frac{|x_i|^2}{||\mathbf{x}||^2}$ $+$  $\frac{|y_i|^2}{||\mathbf{y}||^2})$

giving

$\Sigma \frac{|x_iy_i|}{||\mathbf{x}||||\mathbf{y}||}$  $\le \Sigma$ $\frac{1}{2}(\frac{|x_i|^2}{||\mathbf{x}||^2}$ $+$ $\frac{|y_i|^2}{||\mathbf{y}||^2})$ $=1$
i.e, $\Sigma |x_iy_i|\le$ $||\mathbf{x}||||\mathbf{y}||$
### Remark / Corollory
if $\{x_n\}, \{y_n\}$ are square-summable sequnces in $\mathbb{R}$ or $\mathbb{C}$ then,

$\Sigma|x_iy_i| \le ||\{x_n\}||_ 2||{y_n}||_ 2$


## Minkowsky's Inequality
### proposition
$(\Sigma|xi+y_i|^p)^{1/p}$ $\le$ $||x_i||_ p + ||y_i||_ p$ 
### proof for p=2
$\Sigma|xi+y_i|^2$ $=$  $\Sigma(|xi+y_i|)(|x_i+y_i|)$ $\le$ $\Sigma(|xi+y_i|)(|x_i|+|y_i|)$  $$ $$  \le$ $\Sigma(|x_i+y_i|(||\mathbf{x}||_ 2+||\mathbf{y}_ 2||)$ $\le$ $||\mathbf{x}||_ 2+||\mathbf{y}_ 2||$
### generalization
indexing set becomes $\mathbb{R}$ leads to integrability

## Schwarz  Inequality 
### proposition
In a hilbert space $\mathbb{H}$ over a field $\mathbb{K}$ $\mathbb{R}$ or $\mathbb{C}$

$|\lt \mathbb{x},\mathbb{y}\gt |\le ||\mathbb{x}||||\mathbb{y}||$

### proof
if either of $\mathbb{x}$ or $\mathbb{y}$ is $0$ then the inequality trivially holds. so, wlog, neither is $0$.

set $A:=||\mathbb{x}||^2$, $B:=|\lt \mathbb{x},\mathbb{y}\gt |$ ,$C:=||\mathbb{y}||^2$

choose $\alpha \in \mathbb{C}$ with $|\alpha|=1$ and $\alpha \lt y,x\gt =|\lt y,x\gt |=|\lt x,y\gt |$

for $t \in \mathbb{R}$

$0\le |x-t\alpha y|^2= \lt x-t\alpha y, x-t\alpha y\gt $ $=\lt x,x-t\alpha y\gt -t\alpha\lt y,x-t\alpha y\gt $ $=\lt x,x\gt  - t\bar{\alpha}\lt x,y\gt   -t\alpha\lt y,x\gt  +t^2|\alpha|^2\lt y,y\gt $

$0\le A -t*2B+ t^2C$

putting $t=B/C$, 
$0\le A -B^2/C$ $\implies AC\ge B^2$

# $\pi, e,\ and\ 1$
## proposition
$\int_{\mathbb{R}}e^{-\pi x^2}dx=1$
## proof
### claim 1
#### proposition
$\int_0^{\infty}e^{-\pi x^2}dx$ is a real number.
#### proof
set $x_n:=\int_{0}^ne^{-\pi x^2}dx$

now, $x_{n+1}-x_n=\int_n^{n+1}e^{-\pi x^2}dx \gt 0$ so that $x_n$ is an **increasing sequence**.

but also,

$x^2\gt x\ \forall x\gt 1$
hence

$x_n=\int_{0}^ne^{-\pi x^2}dx \le \int_0^1 1dx + \int_{1}^ne^{-\pi x}dx \le 1+\frac{e^{-\pi}}{\pi}$, is **bounded**.

### claim 2
#### proposition
$2*\int_0^{\infty}e^{-\pi x^2}dx=\int_{-\infty}^{\infty}e^{-\pi x^2}dx$
#### proof
$2*\int_0^{\infty}e^{-\pi x^2}dx$ $=\int_0^{\infty}e^{-\pi x^2}dx$ $+\int_0^{\infty}e^{-\pi x^2}dx$
$=\int_0^{\infty}e^{-\pi x^2}dx - \int_0^{-\infty}e^{-\pi x^2}dx$  $=\int_0^{\infty}e^{-\pi x^2}dx + \int_{-\infty}^0e^{-\pi x^2}dx$  $=\int_{-\infty}^{\infty}e^{-\pi x^2}dx$
### computation

$(\int_{-\infty}^{\infty}e^{-\pi x^2}dx)^2=$$\int_{-\infty}^{\infty}e^{-\pi x^2}dx*\int_{-\infty}^{\infty}e^{-\pi y^2}dy$ $=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{-\pi (x^2+y^2)}dx$ $\because$ no co-dependency of functions in integral.

$=\int_{0}^{2\pi}\int_{0}^{\infty}e^{-\pi (r^2)}rdrd\theta$ , transforming the rectangular measure $dxdy$ to the sector $rdrd\theta$, Jacobian being $\begin{bmatrix} cos\theta & -rsin\theta \\  sin\theta & rcos\theta \\ \end{bmatrix}$

$=\int_{0}^{2\pi}d\theta*\frac{1}{2\pi}\int_{0}^{\infty}e^{-(\pi r^2)}d(\pi r^2)$ $=1*(e^{-\infty}-e^0)=1$
# Hilbert Spaces
## definition
For a vector space $\Omega$ over the field $K=$ $\mathbb{R}$ or $\mathbb{C}$

we have the standard inner product, which induces a norm and thus a metric

A metric space *complete* with respect to this metric is called a **Hilbert Space**.
## Examples
1. $\mathbb{C}^n$ under the standard inner product $\lt \mathbf{x},\mathbf{y}\gt =\Sigma_0^nx_i\bar{y}_ i$
2. $l^2(\mathbb{N})$ over $\mathbb{C}$ under the inner product $\lt \mathbf{x},\mathbf{y}\gt =\Sigma_{i \in \mathbb{N}}x_i\bar{y}_ i$ , generalization of $\mathbb{C}^n$
3. 
## Closed Subspaces
### claim
Any closed subspace $U$ of $H$ is also complete
### proof
take a cauchy sequence $\{x_n\} \in U$ since this sequence belongs to $H$ as well, it converges to some $x \in H$ but $U$ is closed, thus $x\in U$
# Orthogonality
## Definition
$x$ is said to be orthogonal to $y$, i.e, $x \perp y$ when $\lt x,y\gt =0$ 
## The orthogonal space
For any non empty subset $S\subseteq H$ of a hilbert space $H$ over $\mathbb{C}$ we define 

$S^{\perp}:=\{y\in H\ |\ \lt x,y\gt =0 \ \forall\ x \in S\}$

so that we have:
1. $S\cap S^{\perp}\subseteq \{0\}$
2. for a non empty subset $S_1\subseteq S_2$ , $S_1^{\perp}\supseteq S_2^{\perp}$
3. $S^{\perp}$ forms a closed linear subspace of $H$

## Propositions for a closed linear subspace M of the complex Hilbert Space $H$.
### Extreme Value Thm
#### proposition
$\forall x\in H$ associate a $d_x:=inf\{||x-y||\ |\ y\in M\}$
Then $\exists !\ y_x\in M$ such that $d_X=||x-y_x||$
#### proof
##### claim 1
A closed **convex** subset $C$ of $H$ contains a **unique** vector of smallest norm.
#### pf of claim 1
set $d:=inf\{||x|| :\ x\in C\}$, now $\exists \{x_n\}$ in $C$ such that $||x_n||\rightarrow d$.

i.e, $\exists N\in \mathbb{N}$ such that $||x_n||^2\le d^2+\epsilon/4$  $\forall \ n \ge N$

but $(x_m+x_n)/2 \in C$ $\forall\ m,n \in \mathbb{N}$ by convexity.

So that, $||\frac{(x_m+x_n)}{2}|| \ge d$ , but by parallellogram law, $||(x_m-x_n)||^2=2||x_m||^2+2||y||^2-||x_m+x_n||^2 \le $ $4d^2+\epsilon-4d^2$

i.e, $\{x_m\}$ is cauchy in the closed, and hence complete subset $C$, hence $x_m\rightarrow x\in C$.

now $|||x||-||x_n|||\le ||x_n-x||\le \epsilon$ $\forall n\ge N(\epsilon)\in \mathbb{N}$, thus  $||x||=lt_{n\rightarrow {\infty}}||x_n||=d$

also, such an $x$ is unique, because otherwise

$(||\frac{x+x'}{2}||)^2=\frac{||x||^2}{2}+\frac{||x'||^2}{2}-(||\frac{x-x'}{2}||)^2\lt d^2$ but $\frac{x+x'}{2}\in C$ so this contradicts the infimum property of d.
#### tying the ribbon
construct for each $x\in M$  $C_x:=\{x-y |\ \forall\ y \in M\}$
this is closed, since $M$ is. And convex too.

$\because$ $z_1=x-y_1\in C_x$ and $z_2=x-y_2\in C_x$ $\implies tz_1+(1-t)z_2=-ty_1+x-y_2+ty_2=x-(ty_2+y_2+y_1) \in C_x$ because $ty_2+y_2+y_1\in M$, a vector space over $\mathbb{C}$
now since $C_x$ is a closed convex subset, it has a unique element of minimum norm, and we are done.

### Gram Schmidt
#### proposition
for a proper subspace, $\exists\ z \ne 0 \in H$ such that $\lt z,y\gt =0\ \forall\ y \in M$
#### proof
let $x\in H\backslash M$ $\implies x\ne 0$, set $d:=inf\{|x-y|\ | y\in M\}$ $\therefore \exists!\ y\in M$ such that $d=|x-y|$

Now set $z:=x-y$

Since $0\in M$ $\therefore d\le ||x-0||=||x||$, similarly $d\le||z||$

but $z\ne 0$

also, $|z-a|=|x-y-a|=|x-(y+a)|\ge d=|z|\ \forall a \in M$

so that $|z-a|^2-|z|^2\ge0\implies 0\le\lt z-a,z-a\gt -\lt z,z\gt =\lt z-a,z\gt  - \lt z-a,a\gt  - \lt z,z\gt =-\lt a,z\gt -\lt z,a\gt +\lt a,a\gt $

choose $\alpha\in \mathbb{C}$ so that $|\alpha|=1$ and $\alpha(\lt a,z\gt )=|\lt a,z\gt |$

put $a=\alpha b$ for some $b \in M$

thus $|\alpha b|^2-|\lt b,z\gt |-|\lt b,z\gt |\ge0 \implies |b|^2\ge 2\lt b,z\gt $

now put $b=\lt c,z\gt * c$ for some $c\in M$

$|\lt c,z\gt |^2|c|^2\ge 2\lt \lt c,z\gt * c,z\gt =2*|\lt c,z\gt |\lt c,z\gt \implies \lt c,z\gt \lt c,z \gt |c|^2\ge 2*\lt c,z\gt $ $\implies \lt c,z \gt (|c|^2-2)\ge 0$

but we can choose $|c|=1$ so that $\lt c,z\gt \le 0 \implies <c,z>=0$ for any $c \in M$ with $|c|=1$ and since any $a \in M$ can be written as $|a|.\frac{a}{|a|}=|a|.c$ such that $|c|=1$ we get $<a,z>=|(|a|)|<c,z>=0$ $\forall a \in M$
hence ${z}\perp M$
### Closure
#### proposition
If $N$ is another closed linear subspace of $H$ with $M\perp N$ then $M+N$ is also a closed subspace of $H$.
#### proof
Trivially, $M+N$ is a vector subspace of $H$

Now let $\{z_n\} \in M+N$ be a convergent sequence, converging to $z\in H$.

we have for each $z_n$, $z_n=x_n+y_n$ with $x_n\in M$ and $y_n \in N$ such that $\lt x_i,y_j \gt=0\ \forall\ i,j \in \mathbb{N}$

$|z_m-z_n|^2=|x_m+y_m-x_n-y_n|^2=|(x_m-x_n)+(y_m-y_n)|^2=|x_m-x_n|^2+|y_m-y_n|^2$

but $\{z_n\}$ is cauchy, and hence so are $\{x_n\}$ and $\{y_n\}$.

This gives that they converge in $H$, but since they are sequences in closed spaces $M$ and $N$ respectively, they converge in them.

so that $z:=x+y\in M+N$

but this $z$ is the limit of $\{z_n\}$

since $|z_m-z|^2=|x_m+y_m-x-y|^2=|(x_m-x)+(y_m-y)|^2=|x_m-x|^2+|y_m-y|^2$$\rightarrow 0$
### Decompositionm                 
#### proposition
$H=M\oplus M^{\perp}$
#### proof
Trivially $H\supseteq M+M^{\perp}$
Note that both $M$ and $M^{\perp}$ are closed linear subspaces of $H$ and so is $N:=M+M^{\perp}$

now consider $H\supsetneq M+M^{\perp}$  $\implies \exists\ z\ne 0 \in H\backslash N $ such that $\lt z,x \gt =0\ \forall\ x \in N$, i.e. $\lt a+0,z\gt=0$ and $\lt 0+b,z\gt=0$ for $a \in M, b \in M^{\perp}$ because $0$ belongs to both.
this gives $z\in M^{\perp}$ and $z\in M$ which means $z=0$ a contradiction.

so that $H=N$
Now the to prove the uniqueness in decomposition, we see that $M\cap M^{\perp}=0$ so that $a+b=a'+b'\iff a-a'=b'-b$ but $a-a' \in M$ and $b-b'\in M^{\perp}$ giving that both are equal to $0$

# Algebra
a family of subsets $\mathscr{F}$ of a non empty set $\Omega$ is called a $\sigma$ algebra when
1. $\mathscr{F}\subseteq2^{\Omega}$
2. $\Omega\in \mathscr{F}$
3. $A\in \mathscr{F} \implies A^C \in \mathscr{F}$
4. $\{A_n\}_ 1^N\subseteq \mathscr{F} \implies \bigcup_1^N\in \mathscr{F}$
# $\sigma$ algebra
a family of subsets $\mathscr{A}$ of a non empty set $\Omega$ is called a $\sigma$ algebra when
1. $\mathscr{A}\subseteq2^{\Omega}$
2. $\Omega\in \mathscr{A}$
3. $A\in \mathscr{A} \implies A^C \in \mathscr{A}$
4. $\{A_n\}_ 1^{\infty}\subseteq \mathscr{A} \implies \bigcup_1^{\infty}\in \mathscr{A}$
## Generating $\sigma$ algebras
1. For any indexing set $I$ if $F_i$, $i\in I$ is a $\sigma$ algebra of subsets of $\Omega\ne \phi$ then, $\bigcap_{i\in I} F_i$ is a also $\sigma$ algebra of subsets of $\Omega$
2. For $\Omega\ne \phi$ and $\mathscr{A}\subseteq 2^{\Omega}$, $F:=\{A\subseteq \Omega\ |\ A\in G$ $\forall \sigma$ algebras $G$ with $ \mathscr{A}\subseteq G \}$ forms a $\sigma$ algebra of subsets of $\Omega$
# Measure Space
The tuple $(\Omega, \mathscr{A})$, $\mathscr{A}$ being a $\sigma$ algebra of the subsets of $\Omega$
# Pre Measure
A function $\mu: \mathscr{A}\rightarrow [0,\infty]$ satisfying
1. $\mu(\phi)=0$
2. Finite Additivity: $\mu(\bigsqcup_1^NA_i)=\Sigma_1^N\mu (A_i)$
# Measure
A function $m: \mathscr{A}\rightarrow [0,\infty]$ satisfying
1. $m(\phi)=0$
2. Countable Additivity: $m(\bigsqcup_1^{\infty}A_i)=\Sigma_1^{\infty}m(A_i)$
## Examples
1. Dirac Measure
pick a $\omega\in \Omega$. define $d_{\omega}(A)=\begin{cases}1,  & \text{if $\omega \in A$} \\ 0, & \text{if $\omega \notin$ A} \end{cases}$
2. Counting Measure
$m(A)=\begin{cases} |A|, & \text{if $A$ is finite} \\ \infty, & \text{otherwise} \end{cases}$
# Outer Measure
A map $\mu: 2^{\Omega}\rightarrow [0,\infty]$ satisfying
1. $\mu(\phi)=0$
2. $A\subseteq B \implies \mu(A)\le \mu(B)$, respects poset ordering.
3. Countable Subadditivity: $\mu(\bigcup_1^{\infty}A_i)\le\Sigma_1^{\infty}\mu(A_i)$
# Lebesgue Algebra
## construction
**idea**: Basically construct a $\sigma$ algebra so that the outer measure restricted to the algebra forms a measure.
$\mathscr{L}_ {\mu}:=\{A\in \Omega\ |\ \mu(B)=\mu(B\cap A)+\mu(B\cap A^C) \ \forall B \in 2^{\Omega}\}$
## proof of construction being a $\sigma$ algebra
### prop 1 and 2
the first two properties are trivial.
### Countable Unions
to prove countable union containment we first prove finite union containment
#### Base Case
Set $A=A_1\sqcup (A_1^C\cap A_2)=A_1\cup A_2$ , $A_0:=(A_1^C\cap A_2)$
note that $B=(B\cap A)\sqcup (B\cap A^C) \implies \mu(B)\le \mu(B\cap A) + \mu (B\cap A^C) \le$ $\mu (B\cap A_1)+ \mu(B\cap A_0) + \mu(B\cap A^C_1\cap A^C_2)$ $=\mu (B\cap A_1)+ \mu((B\cap A_1^C) \cap A^C_2) + \mu((B\cap A^C_1) \cap A_2)$ $\mu(B\cap A_1) + \mu(B\cap A_1^1)=\mu(B)$
Hence all the inequalities must be equalities, so that $\mu(B)=\mu(B\cap A)+\mu(B\cap A^C)$ for any arbitrary $B$. So that $A\in \mathscr{L}_ {\mu}$
#### Induction
$A_i \in F \implies \bigcup_1^nA_i\in F $, i.e. $F$ is an algebra
#### Limiting case
define $C_i:=A_i\backslash\bigcup_1^{i-1}A_j$, So that $\bigcup A_i=\bigsqcup C_i$

now $E_n:=\bigsqcup_1^nC_i\in F$ and $A=\bigcup E_i$

for any $B \in 2^{\Omega}$ $\mu(B)=\mu(B\cap E_n)+\mu(B\cap E_n^C)$ $\ge \mu(B\cap E_n)+\mu(B\cap A^C)$ $=\Sigma_1^n(B\cap C_i)+\mu(B\cap A^C)$

taking $limsup$, $\mu(B)\ge \mu(B\cap A) + \mu(B\cap A^C) \ge \mu(B\cap A \bigcup B \cap A^C)=\mu(B)$

so that $A\in F$, i.e., $F$ is a $\sigma$ algebra

## restriction forms a pre-measure
### claim
for any $B \in 2^{\Omega}$ and disjoint $A_i\in \mathscr{L}_ {\mu}$ we have $\mu(\bigsqcup_1^n(B\cap A_i))=\Sigma_1^n\mu(B\cap A_i)$
### proof
holds trivially for $n=1$

#### induction
suppose the result holds upto $n=k$

now consider the orthogonal like relations for any $B\in 2^{\Omega}$
1. $B\bigcap(\sqcup_{i=1}^{k+1} A_i)\bigcap A_{k+1}=B\bigcap A_{k+1}$
2. $B\bigcap(\sqcup_{i=1}^{k+1} A_i)\bigcap A_{k+1}^C=B\bigcap(\sqcup_{i=1}^{k}A_i)$

but from the relation in $\mathscr{L}_ {\mu}$, $B\bigcap(\sqcup_{i=1}^{k+1}A_i)=\mu(B\bigcap A_{k+1})+\mu(B\bigcap(\sqcup_{i=1}^{k}A_i))$ and by induction hypothesis, the claim holds.



## restriction forms a measure
set $A:=\bigsqcup_1^{\infty}A_i$ for $A_i\in \mathscr{L}_ {\mu}$

now since $\mu$ is an outer measure, $\mu(A)\le \Sigma A_i$

But since $\mu$ forms a pre-measure on $\mathscr{L}_ {\mu}$, so $\mu(A)\ge \mu(A\bigcap (\sqcup_1^n A_i))=\Sigma_1^nA_i$

but $A$ is independent of $n$ so that $\mu(A)\ge\Sigma A_i$

thus $\mu(A)=\Sigma A_i$

# Set Function to Outer Measure
If we have a map $\mu : S\subseteq 2^{\Omega}\rightarrow [0,\infty]$ such that $\mu(\phi)=0$

then we can construct an outer measure

$\mu^* (A)=inf\{\Sigma\mu(A_n)\ |\ \exists \{A_n\} \in S, A\subseteq \bigcup A_n \}$

## respecting the poset order

obvious because if $A\subseteq B$ then a cover of $B$ covers $A$ also
## vanishing at $\phi$
obvio
## countable subadditivity

the cases when either side is $\infty$ are trivially true. So consider the finite case, wherein there exists a cover of $A$ with a finite $\mu$ sum.
Let $\epsilon \gt 0$ then $\forall n\ge 1$ $\exists$ a sequence $\{A_{nm}\}_ {m\in \mathbb{N}}$ such that $A_n\in \bigcup A_{nm}$

then from the infimum property, $\mu^* (A_n)\ge \Sigma\mu(A_{nm})-\frac{\epsilon}{2^n}$

also, $\mu^* (\bigcup A_ n)\le \Sigma_ n\Sigma_ m\mu(A_ {nm}) \le \Sigma_n(\mu^* (A_n)+\frac{\epsilon}{2^n})=\Sigma\mu^* (A_n)+\epsilon$

since epsilon was arbitrary, we have that $\mu^* $ is countably subadditive

## remark
additionally, if $\mu$ is countably sub-additive on $S$ then, for any $A\in S$ we can construct a sequence $\{A_n\}:=A,\phi,\phi,\phi,\dots$ so that $A\subseteq \bigcup A_n$, which gives $\mu^* (A)\le \mu(A)$

also, $\mu(A)\le \Sigma\mu(A_n)$ for any sequence of $A_n$ such that $\bigcup A_n\supseteq A$ since $\mu$ is countably sub-additive.

which gives that $\mu^* (A)=inf(\{\Sigma\mu(A_n)\})\ge \mu(A)$
hence $\mu^* (A)=\mu(A)$
## uniqueness
let $S_1\subseteq S_2\subseteq 2^{\Omega}$ such that $\mu: S_1\rightarrow [0,\infty]$ with  $\mu(\phi)=0$

### claim
now if we set $\nu(A)=\mu^* (A)$ then $\nu^* (A)=\mu^* (A)\ \forall\ A\in 2^{\Omega}$
### proof
ignoring the trivial case where $\nu^* (A)=\infty$, we prove that $\nu^* (A)\le \mu^* (A)$

choose any $\epsilon\gt 0$, for any sequence $A_n$ covering $A$ we have $\mu^* (A)\le\Sigma\mu(A_n)\le $

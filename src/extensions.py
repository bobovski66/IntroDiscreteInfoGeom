"""Additional worked developments inserted before each chapter's exercises."""
EXTENSIONS={
1:r'''
## Reversing an update and checking a formula

An explicit formula is more than a shortcut. It lets us answer an inverse question: which initial composition would produce a given final composition? For a constant relative multiplier $r>0$, the odds relation $O_t=r^tO_0$ gives $O_0=O_t/r^t$. Convert the observed final proportion to odds, divide by the accumulated multiplier, and convert back to a proportion. These operations reverse the update when both types are present.

::: {.example title="Reconstructing an initial composition"}
After four steps with relative multiplier $3/2$, the A proportion is $3/5$. Its final odds are $3/2$. Dividing by $(3/2)^4=81/16$ gives initial odds $8/27$. The initial A proportion was therefore $(8/27)/(1+8/27)=8/35$. Substituting $x_0=8/35$ into the explicit formula recovers $3/5$ at step four.
:::

Sometimes the multiplier is unknown instead. If both $O_0$ and $O_t$ are known, then $r^t=O_t/O_0$. For example, doubling the odds in three steps requires $r=2^{1/3}$ per step. This is a relative multiplier. Many absolute pairs $(w_A,w_B)$ have this ratio, so compositions alone do not determine absolute population growth.

The exact solution can be verified by **mathematical induction**. First check the initial step $t=0$, where the formula returns $x_0$. Then assume the formula holds at a particular step $t$. Substituting into the recurrence and canceling its common denominator gives the same formula with $t+1$ in place of $t$. These two statements establish the formula for every nonnegative integer step. Induction is particularly well suited to recurrences because the proof follows the way the sequence is constructed.

## Replenishment gives an affine recurrence

Repeated multiplication is one useful mechanism; partial replacement is another. Suppose a fixed-size collection replaces a fraction $\lambda$ of its members each round with an external source whose A proportion is $q$. The next composition is
$$x^+=(1-\lambda)x+\lambda q,\qquad 0<\lambda\leq1.$$
This is an **affine recurrence**, consisting of a multiple of $x$ plus a constant. Its fixed point is $q$. Subtracting that fixed point gives a pure multiplication rule for the error:
$$x^+-q=(1-\lambda)(x-q).$$
Thus $x_t=q+(1-\lambda)^t(x_0-q)$. This technique, shifting coordinates to a fixed point, will recur in later chapters.

::: {.example title="Replacing one quarter of a collection"}
Let $x_0=0.8$, let the external source have proportion $q=0.2$, and replace one quarter each round. Then $x_t=0.2+0.6(3/4)^t$. The first two new values are $0.65$ and $0.5375$. Every step removes one quarter of the remaining difference from the source composition. It does not remove one quarter of the current A proportion.
:::

The multiplying-growth model and the replacement model can be distinguished by their formulas. Positive multiplication preserves absence. Replacement introduces A from the source whenever $q>0$ and $\lambda>0$, even if A is initially absent. Choosing a recurrence therefore includes choosing the mechanisms that can change a population.

## A calculation routine

To compute an update reliably, make a short table with columns for the old proportion, multiplier, and product. Add the products to obtain $Z$, then divide every product by $Z$. Check the new sum before rounding the displayed values. Store more digits than are printed, since feeding rounded output back into the next step changes the recurrence. Finally, compare a simple diagnostic, such as the two-type odds ratio, with its expected update. An independent identity often detects an indexing error that a unit-sum check alone would miss.
''',
2:r'''
## A general no-crossing test

The coexistence proof illustrates a reusable finite method. Suppose an update can be written $x^+=x+G(x)$ and $q$ is a proposed interior fixed point. If algebra produces
$$x^+-q=(x-q)R(x),\qquad 0<R(x)<1,$$
then the new error has the old sign and smaller magnitude. A trajectory cannot cross $q$. The resulting monotone bounded sequence converges, and checking fixed points identifies the limit. The decisive work is the factorization and the bound on $R$.

If instead $-1<R(x)<0$, the error reverses sign while shrinking in magnitude. This describes an alternating approach whenever the estimate holds throughout a region preserved by the update. If $R$ depends on the state, evaluating it at one point proves only a one-step statement there. A uniform bound over the relevant region is needed for a conclusion about the whole run.

::: {.example title="A recurrence that alternates exactly"}
The affine rule $x^+=3/4-x/2$ maps $[0,1]$ into $[1/4,3/4]$. Its fixed point is $q=1/2$, and $x^+-q=-(x-q)/2$. Starting at $x_0=0.2$ gives $0.65$, $0.425$, and $0.5375$. The error is exactly $(-1/2)^t(x_0-q)$. This simple recurrence separates the ideas of crossing an equilibrium and failing to converge: crossing can accompany steady error reduction.
:::

## Boundary behavior from encounter scores

When A is rare, $x$ is close to zero, so its score is close to $b$ and B's score is close to $d$. The comparison $b-d$ determines whether a small positive A proportion rises in the next step. When B is rare, $x$ is close to one, so the relevant comparison is $a-c$. These are the endpoint values of the score difference. They are obtained from the encounter interpretation before any trajectory is calculated.

If $b>d$ and $a<c$, each type has an advantage when rare. The score difference changes from positive to negative, producing an interior equality. If $b<d$ and $a>c$, each type is disadvantaged when rare, and the interior equality is a threshold. The other sign combinations can give one type a consistent advantage. These observations organize the algebra of a two-strategy table.

::: {.example title="Checking an advantage at low frequency"}
For the coexistence table, a rare A meets mostly B and scores close to $4$, while common B scores close to $1$. A therefore increases when introduced at a small positive proportion. Near the A vertex, rare B scores close to $3$ while common A scores close to $2$, so B increases. Both endpoint comparisons agree with the interior equality at $3/4$. Starting exactly at an endpoint still leaves it fixed because the multiplier rule does not introduce absent types.
:::

## From a score table to a reproducible experiment

A numerical report should specify the encounter convention, the table, the score-to-multiplier conversion, the intensity, the initial state, and the number of steps. Each item affects the calculation. A plot labeled only with a table omits part of the recurrence.

For a two-type experiment, record the score difference and the updated proportion at several states. Check that the observed direction agrees with the sign identity. Then ask a separate question about crossing: is the new state still on the same side of an interior fixed point? Finally, compare any proposed long-run description with an exact error estimate when one is available. This sequence of calculations links model assumptions, algebra, and numerical observations without requiring a formula for every trajectory.
''',
3:r'''
## Reading distances and contours in a triangle

Barycentric coordinates have another useful interpretation. The perpendicular distance from a point to side $AB$, divided by the triangle's full altitude, is $p_C$. To verify this, note that the side is horizontal and that the point's height is $(\sqrt3/2)p_C$. By symmetry, the same statement holds for the other two coordinates and their opposite sides. Lines of constant $p_C$ are therefore parallel to side $AB$.

::: {.example title="Recovering a composition from height ratios"}
Suppose a point lies at one fifth of the full altitude from side $AB$ and at one half of the full altitude from side $BC$. The first measurement gives $p_C=1/5$, and the second gives $p_A=1/2$. The remaining coordinate is $p_B=3/10$. The three normalized distances add to one because they are barycentric coordinates.
:::

A contour of a function is a set of states with the same function value. For the coordinate product, a contour is described by $p_Ap_Bp_C=c$. The product is zero on the boundary and at most $1/27$ in the interior. Product contours surround the center, but a one-step decrease in product does not specify a unique direction along a contour or a unique next coordinate. A scalar diagnostic compresses a two-dimensional state into one number, so it necessarily discards some detail.

## Counting the interior and the boundary

The stars-and-bars argument extends to $k$ types. Nonnegative integer counts summing to $N$ are encoded by $N$ stars and $k-1$ bars, so their number is $\binom{N+k-1}{k-1}$. Empty groups correspond to zero counts. If every count must be positive, first give one token to each type. The remaining $N-k$ tokens can be distributed freely, giving $\binom{N-1}{k-1}$ states when $N\geq k$.

For three types, the number of boundary states is the total minus the strictly positive count. For $N\geq3$, this is
$$\binom{N+2}{2}-\binom{N-1}{2}=3N.$$
One can also count $N+1$ points on each of three edges and subtract three to correct the double counting of vertices. The two answers agree. Comparing two counting arguments is a useful way to verify a combinatorial formula.

::: {.example title="A larger lattice"}
At $N=8$, there are $\binom{10}{2}=45$ total states and $\binom72=21$ strictly positive states. The remaining $24$ are on the boundary. A uniform distribution over these 45 lattice vertices would be a probability model on compositions. It is different from independently sampling eight individuals from a uniform three-type population: the latter assigns each count vector a multinomial weight.
:::

## Sampling can change support

At a positive state, deterministic positive multiplication keeps every type present. A sample of $N$ individuals can omit a type by chance. On an edge of the triangle, a sampling model without mutation cannot restore the missing type, because its sampling probability is zero. A finite sampled population may therefore reach an edge and subsequently evolve on that edge, even when a deterministic trajectory remains in the interior for every finite step.

This observation explains why a deterministic trajectory and a simulated finite population should be labeled separately. Both can be useful descriptions. The deterministic rule isolates state-dependent reweighting; the sampled model also includes fluctuations associated with finitely many individuals. Chapter 4 provides exact probabilities for those fluctuations.
''',
4:r'''
## Conditional probability and dependent draws

If an event $B$ has positive probability, the **conditional probability** of $A$ given $B$ is $P(A\mid B)=P(A\cap B)/P(B)$. Here $A\cap B$ means that both events occur. Rearranging gives the multiplication rule $P(A\cap B)=P(B)P(A\mid B)$. Independence is the special case in which conditioning on one event does not change the probability of the other.

An outcome tree can therefore represent dependent observations as well. Its branch probabilities must be conditioned on the path already followed. The product along a path still gives the leaf probability. What changes is the branch labeling.

::: {.example title="Two red tokens without replacement"}
A box has three red and two blue tokens. The probability of two red draws without replacement is $(3/5)(2/4)=3/10$. With replacement it is $(3/5)^2=9/25$. In the first procedure, observing a red token changes the available composition. The second red branch must use the updated box, rather than the initial probability.
:::

## Why multinomial probabilities add to one

There are $k^N$ ordered length-$N$ samples from $k$ labels. Each receives its product probability. Summing over all possible labels at the first position, then the second, and continuing gives
$$\sum_{i_1,\ldots,i_N}p_{i_1}\cdots p_{i_N}=(p_1+\cdots+p_k)^N=1.$$
Grouping these ordered samples by their count vectors replaces each collection of equal products with its multiplicity times one product. The resulting sum is exactly the sum of the multinomial probabilities. This establishes normalization and explains the multinomial expansion as a grouping of outcomes.

At $N=2$ with three labels, there are nine ordered samples but only six count vectors. The vectors $(2,0,0)$, $(0,2,0)$, and $(0,0,2)$ each have multiplicity one. The three other vectors each have multiplicity two. Counting a vector once without this factor would omit ordered outcomes.

## A finite bound on sampling error

Variance can control the probability of a large error using a simple comparison of sums. For a random variable $X$ with mean $\mu$, every outcome satisfying $|X-\mu|\geq a$ contributes at least $a^2$ to the squared deviation. Therefore
$$\operatorname{Var}(X)=\mathbb E[(X-\mu)^2]\geq a^2P(|X-\mu|\geq a),$$
and hence $P(|X-\mu|\geq a)\leq\operatorname{Var}(X)/a^2$. This is **Chebyshev's inequality**. The argument works for a finite distribution by comparing the indicated terms in its expectation sum.

For an empirical binary proportion, it gives
$$P(|\widehat p-p|\geq\varepsilon)\leq\frac{p(1-p)}{N\varepsilon^2}\leq\frac{1}{4N\varepsilon^2}.$$
The last inequality follows from $p(1-p)=1/4-(p-1/2)^2\leq1/4$. This bound is often conservative, but it is valid for every $p$ under independent sampling.

::: {.example title="Choosing a sample size from a bound"}
To make the probability of an empirical error of at least $0.1$ no greater than $0.05$, uniformly over binary probabilities, it is sufficient that $1/(4N(0.1)^2)\leq0.05$. Solving gives $N\geq500$. A sharper calculation for a specified $p$ can use the exact binomial probabilities. The bound provides a guaranteed size without that longer calculation.
:::

A probability bound concerns repetitions of the stated sampling procedure. It does not certify that an already observed empirical table lies within the tolerance. The model, its independence assumption, and its sample size remain part of the conclusion.
''',
5:r'''
## Entropy of a pair of observations

Let $X$ and $Y$ have joint probabilities $p_{ij}=P(X=i,Y=j)$. Their joint entropy is $H(X,Y)=-\sum_{i,j}p_{ij}\ln p_{ij}$. The marginal probability of $X=i$ is $p_i=\sum_jp_{ij}$. When $p_i>0$, write $r_{j\mid i}=p_{ij}/p_i$ for the conditional table of $Y$ given that value of $X$.

Using $p_{ij}=p_i r_{j\mid i}$ and splitting the logarithm gives the **chain rule**
$$H(X,Y)=H(X)+\sum_i p_iH(Y\mid X=i).$$
The second term averages the entropy of the conditional tables. Values of $i$ with probability zero contribute zero. The formula states that describing a pair can be organized as describing the first label and then describing the second label given the first.

If the observations are independent, every conditional table equals the marginal table of $Y$, so $H(X,Y)=H(X)+H(Y)$. Applying this repeatedly gives entropy $NH(p)$ for an independent length-$N$ sample from $p$. This is the average surprisal of an ordered sample; it is different from the logarithm of the number of samples in one count class.

::: {.example title="Dependence changes joint uncertainty"}
Let $X$ be a fair binary label. If $Y=X$, the two possible pairs are $(0,0)$ and $(1,1)$, each with probability $1/2$. Joint entropy is one bit: knowing the first label determines the second. If $Y$ is instead an independent fair label, all four pairs have probability $1/4$, giving two bits of joint entropy. The marginal tables are the same in the two cases, while their dependence differs.
:::

## Coding blocks improves fractional averages

Return to three equally likely labels. A single-label prefix code with lengths $(1,2,2)$ averages $5/3$ bits per label. For a block of two labels there are nine equally likely ordered pairs. A binary tree can assign seven of these pairs length three and the remaining two length four. Its Kraft sum is $7/8+2/16=1$, and such a tree can be formed by splitting one leaf of a complete depth-three tree into two children.

The expected length per pair is $(7\cdot3+2\cdot4)/9=29/9$ bits, or $29/18\approx1.6111$ bits per original label. This is closer to $\log_23\approx1.5850$ than $5/3\approx1.6667$. The calculation exhibits how whole-number lengths for blocks allow smaller fractional averages per symbol.

::: {.example title="An explicit two-label code"}
List the nine ordered pairs as $AA,AB,AC,BA,BB,BC,CA,CB,CC$. Assign the first seven the words $000,001,010,011,100,101,110$, and assign the last two $1110,1111$. No word prefixes another. Each pair is equally likely, so the expected length is $29/9$ bits per pair, as calculated above.
:::

## Interpreting a change of labels

Entropy depends on probabilities and is unchanged by merely renaming or permuting labels. Splitting or merging categories is a different operation. Splitting a label into two distinguishable sublabels can increase entropy because there is more to specify. Merging labels can remove that distinction. For example, merging the two probability-$1/4$ labels in $(1/2,1/4,1/4)$ gives $(1/2,1/2)$ and reduces entropy from $3/2$ bits to one bit. Later, a stochastic channel will provide a general language for such recording operations.
''',
6:r'''
## Likelihood ratios accumulate by addition

Suppose two models $q$ and $p$ assign positive probabilities to the same labels. For an ordered sample $(i_1,\ldots,i_N)$, the likelihood ratio is $\prod_{t=1}^Nq_{i_t}/p_{i_t}$. Its logarithm is the sum of the individual log-likelihood ratios. If the sample really follows $q$ independently, the expected value of each summand is $D(q\|p)$. Linearity of expectation gives expected total log-likelihood ratio $ND(q\|p)$.

This expectation does not require every observed sample to favor $q$. A particular run may contain unusual outcomes that favor $p$. The divergence concerns average evidence under the specified sampling model. Reversing the model that generates the data changes the averaging weights and changes the relevant directed divergence.

::: {.example title="Evidence can point either way in a single trial"}
Let $q=(3/4,1/4)$ and $p=(1/2,1/2)$. Observing the first label contributes $\ln(3/2)>0$ to the log-likelihood ratio in favor of $q$. Observing the second contributes $\ln(1/2)<0$. Averaging with probabilities $3/4$ and $1/4$ gives $D(q\|p)\approx0.1308>0$. The expected evidence favors the generating model even though one possible observation favors the other.
:::

## A finite method for avoiding zero estimates

Given counts $n_i$, one may add a positive number $\alpha$ to every count and normalize:
$$\widetilde p_i=\frac{n_i+\alpha}{N+k\alpha}.$$
This **additive smoothing** produces a positive table, including for labels not observed in the sample. If $N>0$, it can be written as a mixture of the empirical table and uniform:
$$\widetilde p=\frac{N}{N+k\alpha}\widehat p+\frac{k\alpha}{N+k\alpha}u.$$
The added counts have an explicit weight. For a fixed $\alpha$, that weight decreases as more observations arrive. Smoothing is a choice of estimator; the empirical likelihood-maximizing property by itself does not force it.

::: {.example title="A sample with an unobserved category"}
For counts $(4,1,0)$ and $\alpha=1$, the smoothed table is $(5/8,2/8,1/8)$. It is the mixture $(5/8)(4/5,1/5,0)+(3/8)(1/3,1/3,1/3)$. Every category now receives a positive probability. A later observation of the third label has finite surprisal under this table, whereas it would have infinite surprisal under the unsmoothed empirical table.
:::

## A symmetric discrepancy built from two directed ones

Although relative entropy is directed, a symmetric finite comparison can be formed by introducing the midpoint $m=(p+r)/2$:
$$\operatorname{JS}(p,r)=\frac12D(p\|m)+\frac12D(r\|m).$$
This is the **Jensen--Shannon divergence**. By the entropy-mixture identity, it also equals $H(m)-(H(p)+H(r))/2$. It is symmetric and nonnegative. It is finite even for disjoint supports, because the midpoint is positive wherever either input is positive.

Furthermore, $m_i\geq p_i/2$ gives $\ln(p_i/m_i)\leq\ln2$ on the support of $p$, so $D(p\|m)\leq\ln2$. The same argument holds for $r$, and consequently $\operatorname{JS}(p,r)\leq\ln2$. For two disjoint pure states the value is exactly $\ln2$. This provides another example of deriving a useful finite bound by comparing coordinates directly.
''',
7:r'''
## A sum-of-squares proof of the overlap bound

The inequality used to bound overlap can be established directly. For any two lists $a_i,b_i$, expansion gives the identity
$$\left(\sum_i a_i^2\right)\left(\sum_i b_i^2\right)-\left(\sum_i a_ib_i\right)^2
=\sum_{i<j}(a_ib_j-a_jb_i)^2.$$
Every term on the right is nonnegative. This proves Cauchy--Schwarz by finite algebra. Set $a_i=\sqrt{p_i}$ and $b_i=\sqrt{r_i}$ to obtain $1-B(p,r)^2\geq0$. Equality requires $\sqrt{p_ir_j}=\sqrt{p_jr_i}$ for every pair. For probability tables, these conditions force the same normalized proportions and hence $p=r$.

This identity also makes the geometry concrete. A dot product cannot exceed the product of the lengths because the difference of their squares is a sum of nonnegative squares. The familiar angle formula is therefore compatible with the algebra of finite lists.

## The same overlap in independent repeated observations

Suppose one model assigns table $p$ to each of $N$ independent observations and another assigns table $r$. Their distributions on ordered samples have square-root overlap
$$\sum_{i_1,\ldots,i_N}\sqrt{p_{i_1}r_{i_1}\cdots p_{i_N}r_{i_N}}
=\left(\sum_i\sqrt{p_ir_i}\right)^N=B(p,r)^N.$$
The equality follows by expanding a product of $N$ identical finite sums. If $p\ne r$, then $B<1$, so this overlap decreases with sample size. The corresponding spherical distance between the full sample distributions is $2\arccos(B^N)$. More observations can make two distinct sampling models more distinguishable.

::: {.example title="Overlap after several independent observations"}
Take $p=(0.9,0.1)$ and $r=(0.1,0.9)$. A single observation has overlap $0.6$. Two independent observations have overlap $0.36$, and five have overlap $0.07776$. The distributions being compared now live on $2^N$ ordered samples. We can calculate their overlap without listing those samples, because the independent-product structure factors the sum.
:::

## A numerical table near a boundary

For binary $x$, its arc coordinate is $2\arcsin\sqrt{x}$. At $x=0$, $0.01$, $0.04$, and $0.09$, these coordinates are approximately $0$, $0.2003$, $0.4027$, and $0.6094$. The corresponding square roots are $0$, $0.1$, $0.2$, and $0.3$. The table helps explain why square-root coordinates spread out small probabilities.

::: {.example title="Two small perturbations"}
Changing $x$ from $0.01$ to $0.02$ gives spherical distance approximately $0.0834$. Changing it from $0.49$ to $0.50$ gives distance approximately $0.0200$. The first pair has the same absolute probability difference as the second but a larger square-root separation. Both comparisons are finite and use the exact angle formula.
:::

For a statistical application, the labels and the observation procedure must be fixed before comparing tables. Adding an unused zero-probability label to both tables changes none of the overlap, Hellinger, or spherical formulas. Merging existing labels is different and can change the values. This distinction prepares the channel calculations in Chapter 10.
''',
8:r'''
## Counting moves before assigning geometric costs

For two count vectors $a$ and $b$ with the same total, define their total surplus
$$S=\sum_{i:a_i>b_i}(a_i-b_i)=\frac12\sum_i|a_i-b_i|.$$
The surplus equals the total deficit because the counts have the same sum. One token transfer can remove at most one surplus token. Therefore at least $S$ transfers are required to turn $a$ into $b$. This number is attainable: repeatedly move a token from a surplus category to a deficit category until every count agrees.

This proves the minimum number of transfers when every edge costs one. It does not automatically solve the geometrically weighted problem, since different transfers can have different spherical lengths. The cost function determines which optimization problem is being solved.

::: {.example title="Minimum number of moves"}
To transform $(5,1,0)$ into $(1,2,3)$, category A has four surplus tokens. Categories B and C need one and three, respectively. At least four moves are necessary and four suffice, for example $(5,1,0)$ to $(4,2,0)$ to $(3,2,1)$ to $(2,2,2)$ to $(1,2,3)$. Each intermediate vector sums to six. A shortest spherical-weighted route must be found using the actual edge weights.
:::

## Midpoints from a normalization calculation

The square-root midpoint can be found without inverse trigonometric functions. Begin with $v_i=\sqrt{p_i}+\sqrt{r_i}$. Its squared length is $2+2B$. Normalize $v$ to unit length and square the entries:
$$g_i=\left(\frac{v_i}{\sqrt{2+2B}}\right)^2.$$
This is exactly the midpoint formula. The construction treats both endpoints equally and keeps every entry nonnegative. It also shows that if a label is absent at both endpoints, it remains absent at the midpoint and along the whole spherical interpolation.

For a midpoint between two three-label tables, the same arithmetic that computes overlap therefore supplies all its coordinates. The trigonometric formula is needed to choose general equal arc fractions, but halfway has a simpler form.

## Measuring a path from a finite list

Given states $p^{(0)},\ldots,p^{(M)}$, define its polygonal spherical length as $\sum_{j=0}^{M-1}d(p^{(j)},p^{(j+1)})$. This definition uses a finite sum. Refining a list by inserting a new state cannot lower that sum, because the triangle inequality gives $d(a,b)\leq d(a,c)+d(c,b)$. If the inserted state lies in order on the same shortest arc, equality holds.

::: {.example title="A detour through a pure state"}
Let $p=(1,0,0)$ and $r=(0,1,0)$. The direct distance is $\pi$. A route through the third pure state has two legs, each of length $\pi$, for a total of $2\pi$. A route through $(1/2,1/2,0)$ has two legs of length $\pi/2$ and is shortest. The intermediate state and the permitted path both matter.
:::

When a graph algorithm reports a route, verify its adjacency and independently sum the reported edge costs. When comparing with a direct geodesic, check that the endpoints are identical in both calculations. These straightforward checks distinguish a feasible route, a measured route length, and a proof that no shorter allowed route exists.
''',
9:r'''
## Quantifying what an update has gained

The exact optimization identity gives more than the optimizer. Compare its objective with that of keeping the current table $p$. Since $D(p\|p)=0$, the old objective is $J(p)=\eta p\cdot s$. The gain is
$$J(r)-J(p)=\ln Z-\eta p\cdot s=D(p\|r).$$
Thus the improvement is itself a directed relative entropy. Comparing the new objective expression $J(r)=\eta r\cdot s-D(r\|p)$ with the old one gives the further identity
$$\eta(r-p)\cdot s=D(r\|p)+D(p\|r).$$
Both terms on the right are nonnegative. For a single update, the average of the scores used in that update must improve, unless it stays unchanged. The two directions of KL appear together because the calculation compares the tables in both roles.

::: {.example title="Both directed costs in a binary step"}
For $p=(1/2,1/2)$, scores $(0,1)$, and $\eta=\ln3$, the update is $r=(1/4,3/4)$. Its average score rises by $1/4$. Multiplying by $\ln3$ gives approximately $0.2747$. The two divergences are approximately $0.1308$ and $0.1438$, and their sum is the same value. The identity checks the update and clarifies the contribution of each directed discrepancy.
:::

## How concentrated can an update become?

Let $s_{\min}$ and $s_{\max}$ be the smallest and largest scores on the support of $p$. Since $Z$ is a weighted average of their exponentials,
$$e^{\eta s_{\min}}\leq Z\leq e^{\eta s_{\max}}.$$
For any two available labels, $r_i/r_j=(p_i/p_j)e^{\eta(s_i-s_j)}$. This ratio provides a direct way to understand intensity: increasing $\eta$ magnifies score differences while preserving the contribution of the starting ratios.

For a uniquely highest fixed score at label $m$, divide the fixed-score solution's numerator and denominator by $e^{t\eta c_m}$. Every other contribution contains $e^{-t\eta(c_m-c_j)}$, which approaches zero. The leading probability therefore approaches one. If several labels tie, divide by their common leading factor instead. Their initial weights remain in the denominator and determine the final ratios within the tied set.

## Updating from likelihoods

Suppose a hypothesis label $i$ has prior probability $p_i$, and an observation $y$ has conditional likelihood $L_i=P(y\mid i)$. The joint probability of hypothesis and observation is $p_iL_i$. Adding over hypotheses gives $P(y)=\sum_i p_iL_i$. Conditional probability then gives
$$P(i\mid y)=\frac{p_iL_i}{\sum_jp_jL_j}.$$
This is Bayes' rule for a finite hypothesis set. If all likelihoods are positive, set $s_i=\ln L_i$ and $\eta=1$ to obtain the exponential update exactly.

::: {.example title="Posterior odds from one observation"}
Two hypotheses have prior probabilities $1/3$ and $2/3$. A positive test result has likelihoods $3/4$ and $1/4$ under the hypotheses. The unnormalized posterior weights are $1/4$ and $1/6$, with total $5/12$. The posterior is $(3/5,2/5)$. Prior odds $1/2$ have been multiplied by likelihood ratio $3$, producing posterior odds $3/2$.
:::

For several observations, multiplication of likelihoods is justified when they are conditionally independent given the hypothesis. The condition concerns independence within each hypothesis model. Without it, a joint likelihood or sequential conditional likelihoods must replace the simple product.
''',
10:r'''
## Solving the three-node walk exactly

The particular walk introduced earlier can be solved by tracking two contrasts. Write
$$a_t=p_{1,t}-p_{3,t},\qquad b_t=p_{1,t}-2p_{2,t}+p_{3,t}.$$
Substituting the three update equations and collecting coefficients gives
$$a_{t+1}=\frac34a_t,\qquad b_{t+1}=\frac14b_t.$$
Both are geometric sequences. Combining these contrasts with $p_{1,t}+p_{2,t}+p_{3,t}=1$ recovers the probabilities:
$$p_{1,t}=\frac13+\frac{b_t}{6}+\frac{a_t}{2},\quad
p_{2,t}=\frac13-\frac{b_t}{3},\quad
p_{3,t}=\frac13+\frac{b_t}{6}-\frac{a_t}{2}.$$
Because $(3/4)^t$ and $(1/4)^t$ approach zero, every initial table for this walk approaches uniform. This proves the claim for the stated matrix by two scalar recurrences, without needing a general matrix convergence theorem.

::: {.example title="An exact three-step distribution"}
From $(1,0,0)$, both initial contrasts are one. At step three, $a_3=27/64$ and $b_3=1/64$. The recovered table is $(35/64,21/64,8/64)$. Direct multiplication of the step-two table $(5/8,5/16,1/16)$ by the walk matrix gives the same answer.
:::

## Where the lost divergence goes under grouping

For deterministic groups $G_j$, define output masses $Q_j=\sum_{i\in G_j}q_i$ and $P_j=\sum_{i\in G_j}p_i$. Assume positive input tables. Within group $j$, form conditional tables $q_i/Q_j$ and $p_i/P_j$. Splitting the logarithm gives
$$D(q\|p)=D(Q\|P)+\sum_j Q_j D\left(q(\cdot\mid G_j)\middle\|p(\cdot\mid G_j)\right).$$
The first term is the discrepancy retained in the group labels. The second is the average discrepancy among labels inside a group. Every lost contribution is nonnegative. Equality under grouping occurs exactly when the two within-group conditional tables agree, equivalent to a constant ratio $q_i/p_i$ in each group.

::: {.example title="Retained and lost distinctions"}
For the four-label tables $(0.4,0.1,0.4,0.1)$ and $(0.1,0.4,0.1,0.4)$, adjacent-pair grouping gives the same output masses. All the divergence is in the conditional tables $(0.8,0.2)$ and $(0.2,0.8)$ within each pair. Grouping labels $1,3$ together instead gives outputs $(0.8,0.2)$ and $(0.2,0.8)$, while each within-group conditional table is uniform. This second grouping preserves the full divergence.
:::

## Composing observation rules

If channel $K$ is followed by channel $L$, the combined rule is the matrix product $LK$. Its entries are $(LK)_{hi}=\sum_jL_{hj}K_{ji}$. Each term represents passing through intermediate output $j$. Nonnegativity is immediate, and adding over $h$ gives one for every input column. Thus the composition is again a stochastic channel.

Applying data processing twice gives
$$D(LKq\|LKp)\leq D(Kq\|Kp)\leq D(q\|p).$$
The spherical distances obey the same succession of inequalities. This gives a mathematical description of a recording pipeline: sampling labels, adding noise, grouping outputs, and recording an even coarser category can be analyzed one finite operation at a time. A stage may preserve a particular pair's discrepancy, but a later common stage cannot restore a distinction already erased from those output tables.
''',
}

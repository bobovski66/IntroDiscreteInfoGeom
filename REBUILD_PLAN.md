# Rebuild: Discrete Calculus of Information (2026)

## Course thesis
A calculus-first companion to Introduction to Information Geometry. An algebra-prepared student learns finite differences, summation, difference equations, and lattice vector calculus, then uses them to study probability distributions, entropy, KL divergence, statistical distance, and graph information flows. Continuous calculus is not a prerequisite.

## Ten-week progression
1. **Finite differences and summation.** Sequences, first/second differences, discrete antiderivatives, telescoping sums, normalized growth.
2. **Difference equations and stability.** Fixed points, increments, geometric recurrences, feedback, payoff updates, finite-step stability.
3. **Vector calculus on the probability simplex.** Token lattices, neighboring probability states, directional differences, gradients, flux, discrete curl.
4. **Probability transport and conservation.** Stochastic matrices, edge currents, continuity equations, invariant distributions, sampling and finite outcomes.
5. **The discrete calculus of entropy.** Shannon entropy, forward differences, concavity on finite lattices, entropy-increasing moves, counting and coding.
6. **Relative entropy and Lyapunov differences.** KL divergence, finite-time changes of a potential, mixture contraction, discrete stability.
7. **Statistical distance and discrete Fisher geometry.** Square-root coordinates, Hellinger/spherical distance, local quadratic KL forms, edge lengths.
8. **Path sums and shortest statistical routes.** Discrete line integrals, graph gradients, weighted paths, refinement, comparison to Fisher-Rao arcs.
9. **Discrete information-driven dynamics.** Score fields, multiplicative weights, KL-penalized optimization, relative growth and natural-gradient analogies.
10. **Information flows on networks.** Graph divergence/Laplacian, Markov diffusion, mass conservation, entropy production under suitable hypotheses, data processing.

## Editorial and mathematical choices
- Start each week with a new operator or theorem, an exact calculation, and a worked application; distinguish discrete time from finite state spaces.
- Introduce the lattice $\mathcal P_N=\{(n_i/N):\sum n_i=N\}$ and its token-transfer edges. A neighboring move is $p\mapsto p+(e_i-e_j)/N$ when the donor count is positive.
- Use finite differences $\Delta a_n=a_{n+1}-a_n$ and discrete sums $\sum_{k=m}^{n-1}\Delta a_k=a_n-a_m$.
- For graph fields, orient every edge once and use one incidence convention consistently. Divergence is net outward flux and yields an exact continuity equation.
- Retain the original finite geometry, counting, sampling, cyclic dynamics and coding as applications rather than replacing them with abstract operator formalism.
- Distinguish exact Fisher–Rao arc length from the quadratic local approximation. At an interior state, $2D(p+\delta\|p)=\sum_i\delta_i^2/p_i+O(\|\delta\|^3)$; hence the local length is $\sqrt{\sum_i\delta_i^2/p_i}$ (not an extra factor of $\sqrt2$).
- Explain boundary behavior separately: local quadratic metric formulas assume positive coordinates, while square-root spherical distance remains finite at the simplex boundary.
- Rebuild and test all student-facing pages, 10 guided labs, 10 eight-question check-ins, interactive demonstrations, individual chapters, and the whole-book PDF from shared sources.

## Relationship to the continuous course
The companion starts with replicator ODEs, then the simplex, entropy and KL, the Fisher metric, natural gradients and Gaussian geometry. This course makes the corresponding discrete operators foundational, leading to exact finite calculus on probabilities and networks.
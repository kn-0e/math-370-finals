# Borsuk-Ulam Theorem Poster — Claude Code Instructions

## Overview

Create a LaTeX tikzposter for **Ken Lin**, Department of Mathematics, University of Massachusetts Amherst. The poster should match the style of the existing Cantor's Theorem poster (`cantors_theorem.pdf`) — same UMass color scheme (deep red `#881124` headers, clean white panels, UMass Amherst branding), same layout logic (three-column), and same tone (accessible to a non-specialist math audience).

---

## File to Produce

`borsuk_ulam_poster.tex` (and compiled `borsuk_ulam_poster.pdf`)

---

## UMass Theme Requirements

Use the same `UMassTheme.sty` 

## Poster Content

### Title Block
```
BORSUK-ULAM THEOREM
Ken Lin
Department of Mathematics, University of Massachusetts Amherst
```

---

### Column 1 (Left)

#### Box 1: Introduction & Motivation

> At any moment, there exist two antipodal points on Earth with *exactly* the same temperature and pressure.

This is not a coincidence — it is a theorem.

The **Borsuk-Ulam Theorem** (1933) says that any continuous map from a sphere into Euclidean space of one lower dimension must send some pair of antipodal points to the same value.

It was conjectured by Stanislaw Ulam and proved by Karol Borsuk. The result seems geometric but its proof is fundamentally topological — and its consequences reach far beyond geometry.

---

#### Box 2: Key Definitions

- **Sphere**: $S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}$. We work with $S^2$, the standard 2-sphere.
- **Antipodal points**: $P$ and $P' = -P$ on $S^2$, i.e. $(x,y,z)$ and $(-x,-y,-z)$.
- **Continuous map**: A map $F : S^2 \to \mathbb{R}^2$ with no jumps or tears.
- **Closed unit disk**: $D = \{z \in \mathbb{C} : |z| \leq 1\}$, boundary circle $T = \{|z|=1\}$.
- **$C(X)$**: The set of all continuous functions $f : X \to \mathbb{C}$.
- **$C^*(X)$**: Functions in $C(X)$ that never vanish.

---

#### Box 3: Main Theorem

**Theorem (Borsuk-Ulam, 1933)**

*Let $F : S^2 \to \mathbb{R}^2$ be continuous. Then there exists a pair of antipodal points $P$ and $P'$ such that $F(P) = F(P')$.*

Equivalently: no continuous map $F : S^2 \to \mathbb{R}^2$ can satisfy $F(P) \neq F(-P)$ for all $P$.

Include a small diagram: a sphere with two antipodal points $P, P'$ and arrows showing $F(P) = F(P')$ landing on the same point in $\mathbb{R}^2$.

---

### Column 2 (Center)

#### Box 4: Proof Strategy

The proof proceeds by **contradiction** using complex analysis. Identify $\mathbb{R}^2$ with $\mathbb{C}$.

**Step 1 — Assume no antipodal pair maps equally.**
Suppose $F(P) \neq F(P')$ for all $P \in S^2$. Define:
$$G : S^2 \to \mathbb{C}, \quad G(P) = F(P) - F(P')$$
Then $G \in C^*(S^2)$ (never zero), and $G(P) = -G(P')$ for all $P$.

**Step 2 — Parametrize via the upper hemisphere.**
Define $f \in C(D)$ by:
$$f(x+iy) = G\!\left(x,\, y,\, \sqrt{1-x^2-y^2}\right)$$
The map $(x+iy) \mapsto (x, y, \sqrt{1-x^2-y^2})$ sends the closed unit disk $D$ bijectively onto the upper hemisphere. Since $x^2+y^2 \leq 1$ follows from the sphere equation $x^2+y^2+z^2=1$, $f$ is well-defined and continuous on $D$.

**Step 3 — Inherit the antipodal condition on $T$.**
On the boundary circle $T$ (where $z=0$ on the sphere), antipodal points satisfy $G(-x,-y,0) = -G(x,y,0)$, so:
$$f(-z) = -f(z) \quad \forall z \in T$$
Thus $f \in C^*(D)$ with odd-symmetry on the boundary.

**Step 4 — Apply the logarithm proposition.**
By **Proposition 1** (Box 5), since $f \in C^*(D)$ and $D$ is simply connected, $\exists\, h \in C(D)$ with $f = e^h$.

**Step 5 — Derive the contradiction.**
Define $k(z) = \frac{1}{i\pi}[h(z) - h(-z)]$ for $z \in T$.

For $z \in T$: $\exp[i\pi k(z)] = f(z)/f(-z) = -1$, so $k(z)$ is always an **odd integer**.

Since $k$ is continuous and $T$ is connected, $k$ is constant. But:
$$k(1) = \frac{1}{i\pi}[h(1)-h(-1)], \qquad k(-1) = -k(1)$$
So $k = 0$ — but $0$ is **not** an odd integer. **Contradiction.** $\blacksquare$

---

#### Box 5: Key Proposition (Logarithm on a Disk)

**Proposition 1.** *If $f \in C^*(D)$, there exists $h \in C(D)$ such that $e^h = f$.*

*(Proof sketch omitted.)*

This works because $D$ is **simply connected** — the same argument fails on $T$, where $f(z) = z$ has no continuous logarithm.

---

### Column 3 (Right)

#### Box 6: Application — The Ham Sandwich Theorem

**Theorem (Stone–Tukey, 1942)**

*Given any three bounded measurable sets $A_1, A_2, A_3 \subset \mathbb{R}^3$, there exists a single plane that simultaneously bisects all three.*

The sets can be in any configuration — no parallelism or geometric conditions required.

**Proof via Borsuk-Ulam:**

**Step 1.** Each $\mathbf{n} \in S^2$ determines a unique plane $\Pi(\mathbf{n})$ bisecting $A_1$.

**Step 2.** Define $F : S^2 \to \mathbb{R}^2$ by the signed volume imbalances:
$$F(\mathbf{n}) = \bigl(\mu(A_2^+) - \mu(A_2^-),\;\; \mu(A_3^+) - \mu(A_3^-)\bigr)$$
where $A_i^\pm$ is the part of $A_i$ on the $\pm\mathbf{n}$ side of $\Pi(\mathbf{n})$, and $\mu$ denotes volume.

**Step 3.** Flipping $\mathbf{n} \to -\mathbf{n}$ swaps the sides, so $F(-\mathbf{n}) = -F(\mathbf{n})$.

**Step 4.** By **Borsuk-Ulam**, $\exists\, \mathbf{n}^*$ with $F(\mathbf{n}^*) = (0,0)$.

The plane $\Pi(\mathbf{n}^*)$ bisects all three sets simultaneously. $\blacksquare$

Include a small diagram: three blobs (two bread slices + ham) cut by a single plane.

---

#### Box 7: Why Simple Connectivity Matters

The proof hinges on one topological distinction: $D$ is **simply connected** but $T$ is not.

- On $D$: every loop contracts to a point $\Rightarrow$ continuous logarithms exist
- On $T$: the loop $z \mapsto z$ cannot contract $\Rightarrow$ $\log z$ has no continuous branch

This is why the proof must pass from the sphere through the hemisphere to the disk — to gain simple connectivity and unlock the logarithm in Proposition 1.

---

#### Box 8: Conclusions & Further Directions

**Key takeaways:**
- Any continuous $F : S^2 \to \mathbb{R}^2$ must collide on some antipodal pair
- The proof uses only continuity, complex exponentials, and simple connectivity
- The argument generalizes to $S^n \to \mathbb{R}^n$ for all $n$

**Open directions:**
- **Ljusternik-Schnirelmann**: $S^n$ cannot be covered by $n$ closed antipode-free sets
- **Topological Radon Theorem**: any $2d+2$ points in $\mathbb{R}^d$ can be split so their convex hulls intersect
- Connections to **Brouwer's Fixed Point Theorem** and degree theory

---

#### Box 9: Acknowledgements

The author thanks the UMass Amherst Department of Mathematics for support and guidance.

---

## Compilation Instructions

```bash
# Requires: texlive-full or equivalent, tikzposter package
pdflatex borsuk_ulam_poster.tex
pdflatex borsuk_ulam_poster.tex   # run twice for cross-references
```

If `UMassTheme.sty` is needed and not present, define all colors and box styles inline in the preamble to replicate the Cantor poster appearance exactly.

Poster dimensions: **A0 landscape** (same as Cantor poster).

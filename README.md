# Discrete Information Geometry

**Finite Differences, Probability, and Information Flows** is a ten-week course beginning with algebra and finite updates. Probability, logarithms, matrix notation, and the needed trigonometry are introduced in the readings. Calculus is not a prerequisite.

The course develops a discrete calculus of information: finite differences and summation, difference equations, directional differences on probability lattices, graph gradients and divergence, entropy production, KL Lyapunov functions, Fisher–Rao distance, and discrete information-driven dynamics. Counting, normalized growth, multiplicative weights, and finite channels remain applications.

## Course materials

- [Course landing page](index.html) and [teaching guide](guide.html)
- [Complete textbook PDF](textbook/pdf/discrete_information_geometry.pdf)
- [Complete self-contained LaTeX file](textbook/latex/discrete_information_geometry.tex)
- Ten individual chapter PDFs and LaTeX files, linked below
- Ten original demonstrations plus the shared operator explorer, fifty guided laboratory investigations, and eighty check-in questions with explanatory feedback
- 120 textbook exercises, sixty selected exercise solutions, worked examples, and eleven vector figures

| Week | Topic | Materials | Chapter |
| --- | --- | --- | --- |
| 1 | Sequences, differences, and discrete integration | [Read](readings/week01.html) · [Demo](demos/week01.html) · [Lab](labs/week01.html) · [Quiz](quizzes/week01.html) | [PDF](textbook/pdf/chapter01.pdf) · [TeX](textbook/latex/chapter01.tex) |
| 2 | Difference equations, feedback, and stability | [Read](readings/week02.html) · [Demo](demos/week02.html) · [Lab](labs/week02.html) · [Quiz](quizzes/week02.html) | [PDF](textbook/pdf/chapter02.pdf) · [TeX](textbook/latex/chapter02.tex) |
| 3 | Discrete gradients on the probability simplex | [Read](readings/week03.html) · [Demo](demos/week03.html) · [Lab](labs/week03.html) · [Quiz](quizzes/week03.html) | [PDF](textbook/pdf/chapter03.pdf) · [TeX](textbook/latex/chapter03.tex) |
| 4 | Probability transport and conservation | [Read](readings/week04.html) · [Demo](demos/week04.html) · [Lab](labs/week04.html) · [Quiz](quizzes/week04.html) | [PDF](textbook/pdf/chapter04.pdf) · [TeX](textbook/latex/chapter04.tex) |
| 5 | Entropy and its discrete derivatives | [Read](readings/week05.html) · [Demo](demos/week05.html) · [Lab](labs/week05.html) · [Quiz](quizzes/week05.html) | [PDF](textbook/pdf/chapter05.pdf) · [TeX](textbook/latex/chapter05.tex) |
| 6 | Relative entropy and discrete Lyapunov theory | [Read](readings/week06.html) · [Demo](demos/week06.html) · [Lab](labs/week06.html) · [Quiz](quizzes/week06.html) | [PDF](textbook/pdf/chapter06.pdf) · [TeX](textbook/latex/chapter06.tex) |
| 7 | Discrete Fisher geometry and statistical distance | [Read](readings/week07.html) · [Demo](demos/week07.html) · [Lab](labs/week07.html) · [Quiz](quizzes/week07.html) | [PDF](textbook/pdf/chapter07.pdf) · [TeX](textbook/latex/chapter07.tex) |
| 8 | Path sums, circulation, and statistical geodesics | [Read](readings/week08.html) · [Demo](demos/week08.html) · [Lab](labs/week08.html) · [Quiz](quizzes/week08.html) | [PDF](textbook/pdf/chapter08.pdf) · [TeX](textbook/latex/chapter08.tex) |
| 9 | Discrete natural-gradient ideas and learning dynamics | [Read](readings/week09.html) · [Demo](demos/week09.html) · [Lab](labs/week09.html) · [Quiz](quizzes/week09.html) | [PDF](textbook/pdf/chapter09.pdf) · [TeX](textbook/latex/chapter09.tex) |
| 10 | Graph divergence, diffusion, and information flow | [Read](readings/week10.html) · [Demo](demos/week10.html) · [Lab](labs/week10.html) · [Quiz](quizzes/week10.html) | [PDF](textbook/pdf/chapter10.pdf) · [TeX](textbook/latex/chapter10.tex) |

## Mathematical scope

Finite steps are treated as mathematical models in their own right. Linear multiplier rules include a positivity condition. The balanced cyclic selection example has an exact finite product-decrease identity. Square-root geometry uses the categorical radius-two sphere, its angular distance, and explicit spherical interpolation. Multiplicative weights solves a KL-penalized finite objective by an algebraic identity. The network chapter proves data processing with log-sum and Cauchy–Schwarz inequalities and solves a three-node walk through scalar difference equations.

This calculus-first edition follows the broad progression of [Introduction to Information Geometry](https://bobovski66.github.io/IntroInfoGeom/), with finite proofs and combinatorial investigations for students entering through algebra. The [teaching guide](guide.html) maps the topics between the two courses and gives pacing, assessment, and capstone suggestions.

## View and publish

The website uses static HTML, CSS, and JavaScript. No installation or web build step is needed to serve the committed pages. For local viewing:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/`.

For GitHub Pages, choose **Settings → Pages → Deploy from a branch → main → / (root)**. The root `.nojekyll` file ensures that the static files are served directly. Once configured, the course address is `https://bobovski66.github.io/IntroDiscreteInfoGeom/`.

Mathematical typesetting uses MathJax 3.2.2 from a CDN. The core demonstrations and quizzes do not depend on MathJax. Compiled PDFs support offline reading. Lab answers, quiz selections, and optional completion marks are stored locally in the browser when storage is available. They are not sent to an instructor. Each lab can export its questions and answers as an HTML document with typeset mathematical expressions.

## Edit and rebuild

The editable reading sources are `src/ch01.md` through `src/ch10.md`, with additional worked developments in `src/extensions.py`. The calculus-first titles, laboratory prompts, check-ins, and objectives are in `src/calculus_curriculum.py` and are applied in `src/course.py`. The guide source is `src/guide_body.html`. The same sources generate HTML readings and textbook chapters. Exact vector figures are defined in `src/figures.py` and embedded directly in the LaTeX files using TikZ and PGFPlots.

Rebuilding requires Python 3, Pandoc, pdfLaTeX with common TeX Live packages (including Palatino, TikZ, PGFPlots, and standalone), and Poppler's `pdftocairo`:

```bash
python3 scripts/build.py
```

The build produces eleven complete LaTeX documents and eleven PDFs: the whole book and the ten individual chapters. Each LaTeX document includes its own preamble and vector figures and compiles independently without external image files. For example:

```bash
pdflatex discrete_information_geometry.tex
pdflatex discrete_information_geometry.tex
```

Run these commands from the directory containing the selected `.tex` file. The second pass resolves the contents and cross-references. Generated compiler files are ignored by Git.

## Verification

```bash
node tests/math.test.js
python3 scripts/verify.py
```

The numerical checks cover normalization, exact trajectories, support conventions, finite cyclic product identities, mixture contraction, spherical interpolation, KL-penalized optimization, channel contraction, and shortest token routes. The structural checker verifies local links, the course inventory, self-contained LaTeX sources, and compiler warnings. Run it after rebuilding so the compilation logs are available.

The web layout supports narrow screens, keyboard-operated controls, visible focus, reduced-motion preferences, and explicit labels. Quizzes retain explanatory feedback after reload, and lab exports preserve mathematical expressions and the written answers.

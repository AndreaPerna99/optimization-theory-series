# Episode 6 · Deep Landscapes: Neural Network Optimization

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 4, second half |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md), [Ep 3](../ep03_lagrange-kkt-svm/README.md), [Ep 5](../ep05_loss-least-squares-regularization/README.md) |
| Anchor | image and text classifiers |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** A neural network has millions of parameters and a landscape no one can picture. Why can we train it at all, and what goes wrong?

**Technical content.**
- **Neural networks as functions with many layers,** trained by gradient descent; backpropagation as the chain rule applied layer by layer (brief).
- **Vanishing and exploding gradients** in deep networks, and why optimization becomes harder as gradients shrink or blow up through many layers. Standard remedies.
- **Adaptive optimizers:** RMSprop and Adam, which adapt step sizes per parameter for more effective optimization in non-convex landscapes. Built up from Episode 1's momentum and step-size problem.
- **Dropout** as a regularization technique that temporarily ignores neurons during training, making models more robust.
- **Applications:** image recognition (training models to classify images accurately); natural language processing (minimizing errors in sentiment analysis).
- **Recap:** regularization for generalizable, stable models; adaptive optimizers for navigating complex landscapes.
- **Preview:** from one learner to many: distributed optimization.

**Precise statements.**
- *Vanishing/exploding.* The gradient with respect to an early layer is a product of one Jacobian per later layer. If those factors typically shrink vectors, the gradient decays roughly exponentially with depth (vanishing); if they typically stretch vectors, it grows exponentially (exploding). Standard remedies: ReLU-type activations, careful initialization (Xavier/He), normalization layers, residual connections, and gradient clipping for exploding gradients.
- *RMSprop.* $v_k = \beta_2 v_{k-1} + (1-\beta_2) g_k^2$, update $x_{k+1} = x_k - \alpha\, g_k / (\sqrt{v_k} + \delta)$, all operations per coordinate.
- *Adam.* $m_k = \beta_1 m_{k-1} + (1-\beta_1) g_k$ (momentum), $v_k$ as in RMSprop, bias corrections $\hat m_k = m_k/(1-\beta_1^k)$ and $\hat v_k = v_k/(1-\beta_2^k)$, update $x_{k+1} = x_k - \alpha\, \hat m_k / (\sqrt{\hat v_k} + \delta)$. Common defaults $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\delta = 10^{-8}$ (called $\epsilon$ in the Adam paper).
- *What adaptivity does and doesn't fix.* Per-coordinate scaling fixes a narrow valley that is **aligned with the coordinate axes**. It does not fix a valley that runs diagonally; momentum helps in both cases. Show both honestly.
- *Dropout.* During training each unit is zeroed with probability $p$ and the remaining ones are scaled by $1/(1-p)$ ("inverted dropout"); at test time all units are used without scaling. It acts like training an ensemble of thinned networks and discourages units from relying on each other.
- *Non-convex landscapes.* In high dimensions, theory and experiments suggest that saddle points are far more common than bad local minima. Present this as evidence, not a theorem.

**Key visuals.**
- A gradient signal travelling backward through layers, shrinking or exploding (bar heights per layer).
- The narrow valley from Episode 1: plain GD zigzags, momentum smooths it, Adam rescales the axes. Then the same valley rotated 45°, where Adam's advantage disappears and momentum still helps.
- Dropout: neurons blinking off at random during training.
- An image classifier's and a sentiment classifier's decision boundary or loss curve evolving during training, rather than generic "AI is used for X" stock shots.

**Corrections.** The PDF lists the applications generically. They should be shown through what the optimizer does (loss falling, decision boundary forming), so they stay visual and on-topic.

**Callbacks.** Momentum and the pendulum (1), the zigzag and $\kappa$ (1), SGD noise (5), regularization (5).

**Closing line.** When the path is long, the signal from your mistakes can fade or explode. Good improvement needs a way to hear feedback clearly at every step.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_deep.py` | `HookDeep` | **Millions of parameters.** A landscape no one can picture; Why can we train it at all? |
| 2 | `s02_backprop.py` | `Backprop` | **Backpropagation.** Layers as functions; Chain rule applied layer by layer |
| 3 | `s03_vanishing_exploding.py` | `VanishingExploding` | **Vanishing and exploding gradients.** Product of Jacobians through depth; Signal bars shrinking or exploding per layer |
| 4 | `s04_remedies.py` | `Remedies` | **Keeping the signal alive.** ReLU, Xavier/He initialization, normalization; Residual connections, gradient clipping |
| 5 | `s05_adaptive_optimizers.py` | `AdaptiveOptimizers` | **Momentum, RMSprop, Adam.** Built from Episode 1's momentum and step size; Narrow valley: zigzag vs smooth vs rescaled |
| 6 | `s06_rotated_valley.py` | `RotatedValley` | **What adaptivity can't fix.** Same valley rotated 45 degrees; Adam's advantage disappears, momentum still helps |
| 7 | `s07_dropout.py` | `Dropout` | **Dropout.** Units blink off during training; Inverted dropout scaling 1/(1 - p) |
| 8 | `s08_applications.py` | `Applications` | **Images and sentiment.** Loss falling, decision boundary forming; Image recognition and sentiment analysis |
| 9 | `s09_saddles.py` | `Saddles` | **Saddles in high dimensions.** Evidence: saddles far more common than bad minima; Stated as evidence, not a theorem |
| 10 | `s10_recap_closing.py` | `RecapClosing` | **Recap and closing.** Regularization and adaptive optimizers; Closing line |

### Files

| Path | Holds |
|---|---|
| [episode.toml](episode.toml) | metadata and the timeline (the cut) |
| [script.md](script.md) | narration draft and shot list, scene by scene |
| [narration.toml](narration.toml) | final narration as timed segments |
| [scenes/](scenes/) | one manim scene per file |
| `assets/footage/` | video clips for this episode (not versioned; see [docs/PRODUCTION.md](../../docs/PRODUCTION.md)) |
| `assets/figures/` | still images and plots for this episode |
| `takes/` | recorded narration, one file per segment id, when the engine is `takes` |

### Build

```bash
./kg check 6                     # validate manifest, scenes and narration
./kg render 6 -q l               # draft render (480p15); -q h for release
./kg assemble 6 -q l             # join the timeline into one video
./kg narrate 6 -q l --check-only # synthesise narration and check timing
```

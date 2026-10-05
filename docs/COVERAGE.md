# Coverage Checklist

Every content item of the original PDF ([source/OptimizationTheoryPlan.pdf](source/OptimizationTheoryPlan.pdf)) and the episode that covers it. Update this table in the same change whenever an episode's content moves, so nothing from the PDF is ever lost silently. Episode folders are listed in [SERIES.md](../SERIES.md#series-map).

| PDF section | Items | Episode |
|---|---|---|
| Handwritten note (p. 1) | series renamed "Keep the Gradient" | series name ([SERIES.md](../SERIES.md)) |
| Handwritten edit (p. 2) | "Mastering" struck out of Video 1's title | 1 (title has no "Mastering") |
| Series introduction | optimization behind AI, ML, robotics, engineering; best solutions within constraints; journey from gradient descent and LP to healthcare, economics, autonomous systems | 0 (and series description) |
| **Video 0** · 1. What is optimization | definition and everyday meaning; why it matters (engineering, economics, AI, social sciences); reach across disciplines (business profit, predictive models) | 0 |
| Video 0 · 2. Examples | navigation apps; household budgeting; healthcare resource allocation; AI model training | 0 (healthcare also 11; AI also 5–6) |
| Video 0 · 3. Series preview | building blocks; themes and progression; practical examples in every video | 0 (series map) |
| Video 0 · 4. Expectations | what viewers gain; curiosity (natural and social systems); think broadly | 0 |
| **Video 1** · 1. Terminology | objective functions and constraints; 2D feasible region | 1 |
| Video 1 · 2. Gradient and GD | gradient; GD fundamentals; key formula; step size; iterations and path | 1 |
| Video 1 · 3. Examples | physics (pendulum, potential energy); ML (prices, images); data science (MSE) | 1 (pendulum reframed as momentum; MSE also 5) |
| Video 1 · 4. Significance | 3D cost landscape; practical takeaways | 1 |
| Video 1 · 5. Preview | GD as one tool; next: linear methods and duality | 1 |
| **Video 2** · 1. LP | what LP is; linear constraints and objectives (scheduling, budget); simplex and vertex jumps | 2 |
| Video 2 · 2. Solution types | local vs global; convexity; non-convex functions and saddle points | 2 (uniqueness corrected) |
| Video 2 · 3. Duality | primal and dual; application of duality | 2 (shadow prices), 3 (multiplier reveal) |
| Video 2 · 4. Applications | resource allocation; logistics and transportation | 2 |
| Video 2 · 5–6. Takeaways, preview | convexity; duality; next: constraints and sensitivity | 2 |
| **Video 3** · 1. Constrained problems | equality and inequality constraints; feasible regions; budget caps | 3 ("flexible limits" corrected) |
| Video 3 · 2. Lagrange and KKT | Lagrange multipliers; KKT; SVM example | 3 |
| Video 3 · 3. Sensitivity | purpose; decision-making applications (budgeting, supply chain) | 4 |
| Video 3 · 4. Anchors | mechanical engineering; financial planning | 4 |
| Video 3 · 5–6. Recap, preview | KKT and sensitivity summary; real-world practicality; next: ML | 3 and 4 |
| **Video 4** · handwritten note (p. 6) | optimization in computer vision, camera calibration | 5 |
| Video 4 · 1. Optimization in ML | MSE and cross-entropy; GD and SGD | 5 |
| Video 4 · 2. Overfitting and regularization | over- and underfitting; L1, L2; dropout | 5 (dropout in 6) |
| Video 4 · 3. NN challenges | vanishing and exploding gradients; Adam and RMSprop | 6 |
| Video 4 · 4. Examples | image recognition; NLP sentiment analysis | 6 |
| Video 4 · 5. Recap | regularization and robust models; adaptive optimizers | 5 and 6 |
| Video 4 · goal | link to KKT from Video 3 | 5 (regularization as constraint) |
| **Video 5** · 1. Basics | definition and importance; applications (multi-robot, sensor networks, collaborative AI) | 7 |
| Video 5 · 2. Graphs | network representation; adjacency and Laplacian | 7 |
| Video 5 · 3. Consensus | what consensus is; average consensus; applications (swarms, sensors, vehicles) | 7 |
| Video 5 · 4. Distributed GD | distributed gradient descent; gradient tracking | 8 (gradient tracking corrected; time-varying role in 12) |
| Video 5 · 5. SAR | SAR scenario; consensus in SAR | 8 |
| Video 5 · 6. Real-world | swarm robotics; sensor networks | 8 |
| Video 5 · 7–8. Recap, preview | summary; scalability; next: control and RL | 8 |
| **Video 6** · 1. Optimal control | definition and scope; application areas | 9 |
| Video 6 · 2. Formulation | cumulative cost objective; constraints and control inputs | 9 |
| Video 6 · 3. RL | intro to RL; policy optimization and control; Q-learning and value functions | 10 |
| Video 6 · 4. Quadrotor | quadrotor optimal control; dynamic adjustments | 9 (and 0 cold open) |
| Video 6 · 5. Applications | energy management; healthcare dose control; industrial robotics | 9 |
| Video 6 · 6–7. Recap, preview | summary; takeaways; next: interdisciplinary | 9 and 10 |
| **Video 7** · 1. Economics | resource allocation; utility and welfare; Pareto and multi-objective | 11 |
| Video 7 · 2. Social sciences | decision-making and fairness; welfare economics and policy; ethics | 11 |
| Video 7 · 3. Self-organization | definition; stigmergy; ants, swarm robotics, social networks | 12 |
| Video 7 · 4. Other applications | environmental economics; healthcare and public health; education and urban planning | 11 |
| Video 7 · 5. Recap | broader applications; practical takeaway | 11 and 12 |
| Video 7 · 6. Series wrap-up | key concepts recap; inspiring further exploration | 12 |

**Added beyond the PDF** (needed for technical completeness): step-size threshold and conditioning, momentum, projected GD (1); LP outcomes, simplex optimality certificate, weak/strong duality, complementary slackness (2); KKT conditions in full with their validity conditions, force-balance interpretation (3); multipliers as derivatives, kinks versus jumps, trajectory sensitivity (4); Newton, Gauss–Newton, Levenberg–Marquardt, regularization as constraint, SGD noise floor (5); backpropagation, remedies for vanishing gradients, limits of adaptivity (6); consensus as gradient descent, eigenvalue convergence, leaders and containment (7); why DGD stalls, primal–dual mention, Voronoi coverage (8); Bellman, LQR, MPC (9); Bellman optimality, exploration, discount, policy gradient (10); Pareto scalarization, welfare functions, prices as multipliers (11); ACO equations, DeGroot model, tracking a moving optimum (12).

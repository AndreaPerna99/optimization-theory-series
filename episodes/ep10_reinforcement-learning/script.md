# Episode 10 · Script and Shot List

Draft narration and on-screen plan, scene by scene, in timeline order. The
specification is [README.md](README.md); notation, tone rules and the visual
language are in [SERIES.md](../../SERIES.md). When a scene's narration is final,
move it into [narration.toml](narration.toml) as timed segments.

**Status:** not started.

---

## s00 · Title (`Title`)

**On screen:** the episode title card.

**Narration:** none.

## s01 · No model of the world (`HookNoModel`)

**On screen (from the spec):**
- Can a drone learn to act just by trying?

**Narration draft:**

> TODO

## s02 · Rewards and returns (`RlSetup`)

**On screen (from the spec):**
- Agent, environment, reward = -cost
- Discounted return

**Narration draft:**

> TODO

## s03 · Bellman optimality (`BellmanOptimality`)

**On screen (from the spec):**
- Q*(s,a) = E[r + gamma max Q*(s',a')]
- Optimal control without a model

**Narration draft:**

> TODO

## s04 · Q-learning in a grid world (`QLearning`)

**On screen (from the spec):**
- Values spreading back from the goal
- The update is a stochastic step (SGD callback)

**Narration draft:**

> TODO

## s05 · Explore or exploit (`Exploration`)

**On screen (from the spec):**
- epsilon-greedy
- Never exploring: stuck on a mediocre route

**Narration draft:**

> TODO

## s06 · Patience is a parameter (`Discount`)

**On screen (from the spec):**
- Short-sighted vs patient agent
- Horizon about 1/(1 - gamma)

**Narration draft:**

> TODO

## s07 · Policy gradient (`PolicyGradient`)

**On screen (from the spec):**
- Gradient ascent on expected return
- Actor-critic, PPO, SAC (names only)

**Narration draft:**

> TODO

## s08 · Continuous control (`ContinuousControl`)

**On screen (from the spec):**
- Learning curve on a simulated system
- Quadrotor only if RL was used [CONFIRM]

**Narration draft:**

> TODO

## s09 · Recap and closing (`RecapClosing`)

**On screen (from the spec):**
- Act, observe, update
- Closing line

**Narration draft:**

> TODO

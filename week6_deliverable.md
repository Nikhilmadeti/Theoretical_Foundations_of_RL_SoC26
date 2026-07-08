# Week 6 Deliverables

# Derivation of REINFORCE with Baseline and Explanation of Variance Reduction

## Introduction

Policy Gradient methods directly optimize the policy instead of estimating value functions or Q-values. The policy is represented by a parameterized function that outputs the probability of selecting each action in a given state. The objective is to maximize the expected cumulative reward by adjusting the policy parameters using gradient ascent.

One of the simplest policy gradient algorithms is **REINFORCE**, which updates the policy after observing complete episodes. However, REINFORCE often suffers from high variance. To improve learning stability, a **baseline** is introduced, leading to the REINFORCE with Baseline algorithm.

---

## Policy Gradient Objective

The objective of policy gradient methods is to maximize the expected return.

```text
J(θ) = Eπθ[G]
```

where:

- **θ** = policy parameters
- **πθ** = parameterized policy
- **G** = cumulative return

The goal is to find the policy parameters that maximize the expected return.

---

## Policy Gradient Theorem

The gradient of the objective function is

```text
∇J(θ) = Eπθ[∇ log πθ(a|s) × Qπ(s,a)]
```

This theorem shows that the policy can be improved by increasing the probability of actions that produce higher expected returns.

---

## REINFORCE Algorithm

REINFORCE estimates the action-value using the actual return observed after completing an episode.

Replacing the action-value with the sampled return gives

```text
∇J(θ) = E[∇ log πθ(a|s) × Gt]
```

The policy parameters are updated using gradient ascent.

The update rule is

```text
θ ← θ + α ∇ log πθ(a|s) Gt
```

where:

- **α** = learning rate
- **Gt** = return from time step *t*

This algorithm updates the policy after every complete episode.

---

## REINFORCE with Baseline

Although REINFORCE is unbiased, the returns can vary significantly from one episode to another, leading to high variance.

To reduce this variance, a **baseline** is subtracted from the return.

The baseline is usually chosen as the state-value function.

```text
b(s) = V(s)
```

The policy gradient becomes

```text
∇J(θ) = E[∇ log πθ(a|s) (Gt − b(s))]
```

Using the state-value function as the baseline,

```text
∇J(θ) = E[∇ log πθ(a|s) (Gt − V(s))]
```

The quantity

```text
A(s,a) = Gt − V(s)
```

is called the **Advantage Function**.

The parameter update becomes

```text
θ ← θ + α ∇ log πθ(a|s) (Gt − V(s))
```

This algorithm is known as **REINFORCE with Baseline**.

---

## Why the Baseline Reduces Variance

The return **Gt** can fluctuate considerably even when the agent is in the same state. Large fluctuations produce noisy gradient estimates, making learning slow and unstable.

The baseline estimates the average expected return from a state. By subtracting this average, the algorithm focuses only on how much better or worse an action performs compared to the expected outcome.

As a result:

- Positive advantage increases the probability of good actions.
- Negative advantage decreases the probability of poor actions.
- Gradient estimates become less noisy.
- Learning becomes more stable.
- Convergence is faster.

Importantly, subtracting a baseline **does not change the expected value of the gradient**, so the estimator remains unbiased while having lower variance.

---

## Comparison of REINFORCE and REINFORCE with Baseline

| Feature | REINFORCE | REINFORCE with Baseline |
|----------|-----------|-------------------------|
| Uses Return Only | Yes | No |
| Uses State Value | No | Yes |
| Variance | High | Lower |
| Bias | Unbiased | Unbiased |
| Stability | Lower | Higher |
| Convergence Speed | Slower | Faster |

---

## Advantages of REINFORCE with Baseline

- Reduces variance in policy gradient estimates.
- Produces smoother and more stable learning.
- Converges faster than standard REINFORCE.
- Improves training efficiency without introducing bias.
- Forms the foundation of modern Actor-Critic algorithms.

---

## Summary

REINFORCE is a Monte Carlo policy gradient algorithm that updates policy parameters using the returns obtained from complete episodes. Although it provides an unbiased estimate of the policy gradient, it suffers from high variance. Introducing a baseline, typically the state-value function, reduces this variance by measuring the advantage of an action relative to the expected return. REINFORCE with Baseline therefore achieves more stable learning, faster convergence, and serves as the basis for many advanced policy optimization methods used in modern reinforcement learning.

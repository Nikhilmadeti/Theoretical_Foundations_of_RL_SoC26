# Week 3 Deliverables

## 1. Pseudocode for Dynamic Programming Algorithms

### Policy Evaluation

Policy Evaluation computes the value function for a given policy by repeatedly applying the Bellman Expectation Equation until the value estimates converge.

**Pseudocode**

```text
Initialize V(s) = 0 for all states

Repeat
    Δ = 0
    For each state s
        v = V(s)
        V(s) = Σa π(a|s) Σs',r P(s',r|s,a)[r + γV(s')]
        Δ = max(Δ, |v − V(s)|)
Until Δ < θ

Return V
```

where:

- **π(a|s)** is the policy.
- **γ** is the discount factor.
- **θ** is a small threshold used to determine convergence.

---

### Policy Iteration

Policy Iteration alternates between evaluating the current policy and improving it until the policy becomes stable.

**Pseudocode**

```text
Initialize policy π randomly

Repeat

    Perform Policy Evaluation to compute Vπ

    policy_stable = True

    For each state s
        old_action = π(s)

        π(s) = argmaxa Σs',r P(s',r|s,a)[r + γV(s')]

        If old_action ≠ π(s)
            policy_stable = False

Until policy_stable

Return π and V
```

Policy Iteration always converges to the optimal policy for a finite Markov Decision Process.

---

### Value Iteration

Value Iteration combines policy evaluation and policy improvement into a single update by directly applying the Bellman Optimality Equation.

**Pseudocode**

```text
Initialize V(s) = 0 for all states

Repeat

    Δ = 0

    For each state s

        v = V(s)

        V(s) = maxa Σs',r P(s',r|s,a)[r + γV(s')]

        Δ = max(Δ, |v − V(s)|)

Until Δ < θ

For each state s

    π(s) = argmaxa Σs',r P(s',r|s,a)[r + γV(s')]

Return π and V
```

Value Iteration generally converges faster than Policy Iteration because it does not require a complete policy evaluation after every update.

---

## 2. Comparison of Monte Carlo and Temporal Difference (TD) Learning on a Toy MDP

### Toy MDP

Consider the following simple Markov Decision Process.

```text
S1 ----> S2 ----> Terminal

Reward = +1      Reward = +2
Discount factor γ = 1
```

The agent always follows the same policy.

---

### Monte Carlo Learning

Monte Carlo methods wait until the episode finishes before updating value estimates.

The episode is

```text
S1 → S2 → Terminal
```

The returns are

For **State S2**

```text
Return = 2
```

For **State S1**

```text
Return = 1 + 2 = 3
```

Therefore,

```text
V(S2) = 2

V(S1) = 3
```

Monte Carlo updates these values only after the entire episode has completed.

---

### Temporal Difference Learning (TD(0))

Suppose initially

```text
V(S1) = 0

V(S2) = 0
```

Learning rate

```text
α = 0.5
```

Discount factor

```text
γ = 1
```

---

### Updating State S2

Using the TD update rule

```text
V(S) ← V(S) + α[r + γV(S') − V(S)]
```

```text
V(S2) = 0 + 0.5(2 + 0 − 0)

V(S2) = 1
```

---

### Updating State S1

```text
V(S1) = 0 + 0.5(1 + 1 − 0)

V(S1) = 1
```

Unlike Monte Carlo, TD updates immediately after every transition without waiting for the episode to finish.

---

## Comparison

| Feature | Monte Carlo | TD Learning |
|----------|-------------|-------------|
| Learns after | Complete episode | Every step |
| Uses | Actual returns | Estimated future values |
| Bootstrapping | No | Yes |
| Bias | Low | Higher |
| Variance | High | Lower |
| Suitable for | Episodic tasks | Continuing and episodic tasks |
| Convergence | Slower | Faster |

---

### Bias-Variance Tradeoff

Monte Carlo methods estimate values using complete returns, making them **unbiased** but with **high variance** because episode outcomes can vary significantly.

Temporal Difference methods estimate future rewards using current value estimates (bootstrapping). This introduces some **bias**, but greatly reduces variance and usually leads to faster learning.

Consequently, TD learning is generally preferred for large or continuing environments, while Monte Carlo methods are useful when complete episodes are available and unbiased estimates are desired.

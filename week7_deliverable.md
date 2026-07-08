# Week 7 Deliverables

# Planning, Exploration, and Advanced Reinforcement Learning

## 1. Dyna-Q and Comparison of Epsilon-Greedy vs Upper Confidence Bound (UCB)

### Introduction

One of the major challenges in Reinforcement Learning is balancing **learning from real interactions** with **planning using previously acquired knowledge**. Model-based reinforcement learning addresses this challenge by learning an approximate model of the environment and using it to simulate additional experiences. One of the most influential model-based algorithms is **Dyna-Q**, proposed by Richard Sutton. Alongside planning, effective exploration strategies such as **Epsilon-Greedy** and **Upper Confidence Bound (UCB)** play an important role in improving learning efficiency.

---

## Dyna-Q

### What is Dyna-Q?

Dyna-Q is a **model-based reinforcement learning algorithm** that combines **direct learning**, **model learning**, and **planning** within a single framework. Unlike traditional model-free algorithms that learn only from real interactions with the environment, Dyna-Q also learns a model of the environment and uses simulated experiences to improve the action-value function.

The Dyna-Q framework consists of three main components:

1. **Direct Reinforcement Learning** – Updates Q-values using real interactions with the environment.
2. **Model Learning** – Stores the observed state transitions and rewards to build an approximate model of the environment.
3. **Planning** – Randomly samples previously observed state-action pairs from the learned model and performs additional Q-value updates.

This combination allows the agent to learn not only from actual experiences but also from simulated experiences, making learning significantly more sample-efficient.

---

### Dyna-Q Algorithm

The overall learning process is:

1. Observe the current state.
2. Select an action using the exploration policy.
3. Execute the action and observe the next state and reward.
4. Update the Q-value using the Q-Learning update rule.
5. Store the observed transition in the learned model.
6. Randomly sample previously stored transitions.
7. Perform several simulated Q-value updates using the model.
8. Repeat until convergence.

Because planning updates are performed without additional interaction with the environment, Dyna-Q learns much faster than purely model-free methods.

---

### Advantages of Dyna-Q

- Combines learning and planning.
- Improves sample efficiency.
- Learns faster using simulated experiences.
- Requires fewer real interactions with the environment.
- Suitable when an approximate environment model can be learned.

### Limitations of Dyna-Q

- Requires learning and storing an environment model.
- Planning becomes computationally expensive for large environments.
- Performance depends on the accuracy of the learned model.
- Less effective in highly complex or stochastic environments.

---

## Epsilon-Greedy Exploration

### Working Principle

Epsilon-Greedy is one of the simplest exploration strategies.

At every decision step:

- With probability **ε**, the agent selects a random action (exploration).
- With probability **1 − ε**, the agent selects the action with the highest estimated Q-value (exploitation).

Initially, ε is kept high to encourage exploration and is gradually reduced during training.

### Advantages

- Simple to implement.
- Computationally inexpensive.
- Works well for many reinforcement learning problems.

### Disadvantages

- Random exploration may waste interactions.
- Treats all unexplored actions equally.
- Does not consider uncertainty in value estimates.

---

## Upper Confidence Bound (UCB)

### Working Principle

Upper Confidence Bound selects actions by considering both:

- Estimated reward.
- Uncertainty of the estimate.

Actions that have been explored less frequently receive a higher exploration bonus.

A typical UCB action-selection rule is

```text
Action = Estimated Value + Exploration Bonus
```

This encourages the agent to explore uncertain actions while gradually favoring actions with high expected rewards.

### Advantages

- Exploration is directed rather than random.
- Efficiently balances exploration and exploitation.
- Achieves lower cumulative regret.
- Frequently outperforms ε-greedy in many problems.

### Disadvantages

- Computationally more expensive.
- Requires maintaining action visit counts.
- More difficult to apply in high-dimensional deep reinforcement learning settings.

---

## Comparison of Epsilon-Greedy and UCB

| Feature | Epsilon-Greedy | Upper Confidence Bound (UCB) |
|----------|----------------|------------------------------|
| Exploration Strategy | Random | Confidence-based |
| Uses Uncertainty | No | Yes |
| Exploration Quality | Random | Directed |
| Computational Cost | Low | Higher |
| Sample Efficiency | Moderate | High |
| Regret | Higher | Lower |
| Implementation | Simple | More Complex |

---

## Summary

Dyna-Q improves reinforcement learning by combining direct learning with planning through a learned model of the environment, resulting in faster and more sample-efficient learning. Epsilon-Greedy provides a simple exploration strategy based on random action selection, whereas Upper Confidence Bound performs more informed exploration by considering uncertainty in action-value estimates. Although UCB generally achieves better exploration performance, ε-greedy remains popular because of its simplicity and low computational cost.

---

# 2. Strengths and Weaknesses of PPO, DDPG, and SAC

## Introduction

As reinforcement learning problems become larger and more complex, traditional tabular algorithms become insufficient. Deep Reinforcement Learning combines neural networks with reinforcement learning to solve high-dimensional problems. Three of the most influential deep reinforcement learning algorithms are **Proximal Policy Optimization (PPO)**, **Deep Deterministic Policy Gradient (DDPG)**, and **Soft Actor-Critic (SAC)**. Although all three are designed for continuous control problems, they differ significantly in their learning strategies, stability, and sample efficiency.

---

## Proximal Policy Optimization (PPO)

### Overview

PPO is an **on-policy actor-critic** algorithm developed by OpenAI. It improves policy gradient methods by limiting the size of policy updates using a clipped objective function, preventing unstable changes during learning.

### Strengths

- Stable and reliable training.
- Simple to implement.
- Strong performance across many tasks.
- Robust to hyperparameter choices.
- Widely adopted in robotics and simulation environments.

### Weaknesses

- Requires fresh data after every policy update.
- Lower sample efficiency than off-policy methods.
- Training can be slower because old experiences cannot be reused.

---

## Deep Deterministic Policy Gradient (DDPG)

### Overview

DDPG is an **off-policy actor-critic** algorithm designed for continuous action spaces. It combines deterministic policy gradients with deep neural networks and uses experience replay together with target networks.

### Strengths

- High sample efficiency.
- Suitable for continuous control.
- Can reuse previous experiences.
- Performs well in robotics applications.

### Weaknesses

- Sensitive to hyperparameter tuning.
- Training can become unstable.
- Exploration is often insufficient without additional noise mechanisms.

---

## Soft Actor-Critic (SAC)

### Overview

SAC is an **off-policy actor-critic** algorithm that maximizes both cumulative reward and policy entropy. The entropy objective encourages continuous exploration throughout training.

### Strengths

- Excellent exploration.
- Highly sample efficient.
- Stable learning.
- Robust across many benchmark environments.
- Less sensitive to hyperparameter selection than DDPG.

### Weaknesses

- More computationally expensive.
- More complex implementation.
- Requires additional entropy-related calculations.

---

## Comparison of PPO, DDPG, and SAC

| Feature | PPO | DDPG | SAC |
|----------|-----|------|-----|
| Learning Type | On-Policy | Off-Policy | Off-Policy |
| Action Space | Continuous & Discrete | Continuous | Continuous |
| Sample Efficiency | Moderate | High | Very High |
| Training Stability | High | Moderate | Very High |
| Exploration | Good | Limited | Excellent |
| Replay Buffer | No | Yes | Yes |
| Target Networks | No | Yes | Yes |
| Hyperparameter Sensitivity | Low | High | Moderate |
| Computational Cost | Moderate | Moderate | High |

---

## Overall Comparison

PPO is preferred when stable and reliable learning is the primary objective. DDPG is effective for continuous control tasks but often requires careful tuning and exploration strategies. SAC combines the strengths of off-policy learning with entropy maximization, providing better exploration, improved stability, and higher sample efficiency, making it one of the most effective modern reinforcement learning algorithms.

---

## Summary

Modern deep reinforcement learning algorithms extend classical reinforcement learning by integrating neural networks with policy optimization techniques. PPO provides stable policy updates and is widely used for practical applications, DDPG offers efficient learning for continuous action spaces through deterministic policies, and SAC further improves performance by encouraging exploration using entropy maximization. Together, these algorithms demonstrate how classical reinforcement learning concepts such as value functions, policy optimization, and temporal difference learning scale to solve complex real-world problems.

# Week 5 Deliverables

# Deep Q-Network (DQN) Loss Function and the Importance of Experience Replay and Target Networks

## Introduction

As reinforcement learning problems become more complex, maintaining a Q-table for every state-action pair becomes impractical. Deep Q-Networks (DQN) address this limitation by using a deep neural network to approximate the Q-function. Instead of storing values in a table, the neural network learns to predict Q-values directly from the state. To make training stable and efficient, DQN introduces two important techniques: **Experience Replay** and **Target Networks**.

---

## Deep Q-Network (DQN)

A Deep Q-Network approximates the action-value function

```text
Q(s,a;θ)
```

where:

- **s** is the current state.
- **a** is the action.
- **θ** represents the neural network parameters.

The network receives the current state as input and outputs the estimated Q-value for every possible action.

---

## DQN Loss Function

The DQN learning objective is to minimize the difference between the predicted Q-value and the target Q-value.

The target value is

```text
y = r + γ max Q(s', a'; θ⁻)
```

where:

- **r** = immediate reward
- **γ** = discount factor
- **s'** = next state
- **θ⁻** = parameters of the target network

The DQN loss is

```text
L(θ) = E[(y − Q(s,a;θ))²]
```

or equivalently,

```text
L(θ) = E[(r + γ max Q(s',a';θ⁻) − Q(s,a;θ))²]
```

The objective is to minimize the mean squared error between the predicted Q-value and the target value.

---

## Experience Replay

### What is Experience Replay?

During training, every interaction with the environment is stored in a memory buffer as an experience:

```text
(state, action, reward, next state)
```

Instead of learning only from the latest experience, the agent randomly samples small batches from this replay buffer.

### Why Experience Replay Helps

Experience Replay provides several advantages:

- Breaks the strong correlation between consecutive experiences.
- Reuses past experiences multiple times, improving sample efficiency.
- Produces more stable gradient updates.
- Reduces variance during training.
- Prevents the network from overfitting to recent experiences.

Without replay, the network would learn from highly correlated data, making training unstable and slowing convergence.

---

## Target Networks

### What is a Target Network?

DQN maintains two neural networks:

1. **Online Network** – updates after every training step.
2. **Target Network** – used only for computing target Q-values.

The target network parameters are copied from the online network after a fixed number of training steps.

### Why Target Networks Help

Target Networks improve learning by:

- Keeping target values stable during training.
- Preventing feedback loops caused by continuously changing targets.
- Reducing oscillations in Q-value estimates.
- Improving convergence.
- Making deep reinforcement learning significantly more stable.

Without a target network, both the prediction and target values would change simultaneously, often causing unstable learning.

---

## Combined Effect of Replay Buffer and Target Networks

The combination of Experience Replay and Target Networks was one of the major innovations introduced in the original DQN paper.

Together they:

- Improve training stability.
- Increase sample efficiency.
- Reduce correlations between training samples.
- Produce smoother gradient updates.
- Prevent divergence during learning.
- Enable deep neural networks to successfully approximate Q-values.

These improvements allowed DQN to achieve human-level performance on several Atari 2600 games, demonstrating that deep neural networks can effectively learn control policies directly from high-dimensional inputs.

---

## Summary

Deep Q-Networks extend traditional Q-Learning by replacing the Q-table with a neural network that approximates the action-value function. The DQN loss minimizes the squared difference between predicted and target Q-values. Experience Replay stabilizes learning by breaking correlations between experiences and improving sample efficiency, while Target Networks provide stable target values that prevent divergence during training. Together, these techniques make DQN one of the foundational algorithms in Deep Reinforcement Learning.

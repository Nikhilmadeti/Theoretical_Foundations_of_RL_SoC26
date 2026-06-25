# Week 4 Deliverables

## Derivation and Comparison of SARSA and Q-Learning Updates

### Introduction

Model-Free Control methods enable an agent to learn an optimal policy without having prior knowledge of the environment's transition probabilities or reward function. Instead, the agent improves its behavior by interacting with the environment and updating its action-value estimates. Two of the most important model-free control algorithms are **SARSA** and **Q-Learning**. Both algorithms use Temporal Difference (TD) learning, but they differ in how they estimate future rewards and update their action-value functions.

---

## SARSA (State-Action-Reward-State-Action)

SARSA is an **on-policy** reinforcement learning algorithm. It learns the value of the policy that the agent is currently following. The update depends on both the current action and the next action actually selected by the policy.

The sequence of interaction is:

```text
State → Action → Reward → Next State → Next Action
```

Hence the name **SARSA**.

### Derivation of the SARSA Update Rule

The action-value function is

```text
Q(s,a) = Expected return when taking action a in state s and following policy π.
```

The Temporal Difference target is

```text
Target = Reward + γ × Q(Next State, Next Action)
```

The TD error is

```text
TD Error = Target − Current Estimate
```

Substituting,

```text
TD Error = r + γQ(s',a') − Q(s,a)
```

Updating the action-value estimate gives

```text
Q(s,a) ← Q(s,a) + α[r + γQ(s',a') − Q(s,a)]
```

where

- **α** = Learning rate
- **γ** = Discount factor
- **r** = Immediate reward
- **a'** = Next action selected by the current policy

Because the next action comes from the current policy, SARSA learns the value of the policy actually being followed.

---

## Q-Learning

Q-Learning is an **off-policy** reinforcement learning algorithm. Instead of following the current policy during updates, it assumes that the agent always chooses the best possible action in the next state.

### Derivation of the Q-Learning Update Rule

The optimal action-value function satisfies the Bellman Optimality Equation.

The target value is

```text
Target = Reward + γ × max Q(Next State, Next Action)
```

The TD error becomes

```text
TD Error = r + γ max Q(s',a') − Q(s,a)
```

The update equation is

```text
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') − Q(s,a)]
```

The maximum operator selects the action with the highest estimated value, regardless of the action actually taken by the policy.

This enables Q-Learning to learn the optimal policy even while the agent explores using another policy such as ε-greedy.

---

## On-Policy vs Off-Policy Learning

### On-Policy Learning

In on-policy learning, the algorithm learns from the same policy that generates the experience.

Characteristics:

- Learns the policy currently being followed.
- Updates depend on the action actually selected.
- Exploration directly affects learning.
- Usually produces safer learning behaviour.

SARSA is an example of an on-policy algorithm.

---

### Off-Policy Learning

In off-policy learning, the algorithm learns the optimal policy independently of the policy used to collect experiences.

Characteristics:

- Learns the optimal policy directly.
- Uses the maximum estimated future reward.
- Exploration policy and learning policy are different.
- Often converges faster toward the optimal solution.

Q-Learning is an example of an off-policy algorithm.

---

## Comparison of SARSA and Q-Learning

| Feature | SARSA | Q-Learning |
|----------|--------|------------|
| Learning Type | On-Policy | Off-Policy |
| Update Target | Q(s', a') | max Q(s', a') |
| Next Action | Action chosen by current policy | Best estimated action |
| Exploration Included | Yes | No |
| Learning Behaviour | Conservative | Aggressive |
| Convergence | Learns current policy | Learns optimal policy |
| Suitable For | Environments where safety matters | Finding the optimal policy efficiently |

---

## Example

Suppose

```text
Current Q(s,a) = 5

Reward = 2

γ = 0.9

α = 0.1
```

Next state's action values

```text
Action A = 8

Action B = 6
```

Suppose the current policy selects **Action B**.

### SARSA Update

Since the policy selects Action B,

```text
Target = 2 + 0.9 × 6

Target = 7.4
```

Updated Q-value

```text
Q(s,a) = 5 + 0.1(7.4 − 5)

Q(s,a) = 5.24
```

---

### Q-Learning Update

Q-Learning chooses the maximum future value.

```text
Target = 2 + 0.9 × 8

Target = 9.2
```

Updated Q-value

```text
Q(s,a) = 5 + 0.1(9.2 − 5)

Q(s,a) = 5.42
```

The Q-Learning update is larger because it assumes the best possible future action instead of the action actually chosen.

---

## Conclusion

SARSA and Q-Learning are both Temporal Difference control algorithms used for model-free reinforcement learning. SARSA is an on-policy algorithm that updates its estimates using the action selected by the current policy, making it more conservative and suitable for environments where safe exploration is important. Q-Learning is an off-policy algorithm that updates using the maximum estimated future reward, allowing it to learn the optimal policy more quickly. Understanding the difference between these update rules provides the foundation for many modern reinforcement learning algorithms.

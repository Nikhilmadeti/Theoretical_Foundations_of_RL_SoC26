# Week 1 Deliverable

## Reinforcement Learning

Reinforcement Learning (RL) is a branch of machine learning in which an agent learns how to make decisions by interacting with an environment. Unlike supervised learning, where correct answers are provided, an RL agent learns through trial and error. The agent takes actions, receives rewards or penalties, and gradually improves its behavior to maximize long-term rewards.

An RL system consists of four main components:

1. **Agent** – the learner or decision maker.
2. **Environment** – everything the agent interacts with.
3. **State (s)** – the current situation of the environment.
4. **Action (a)** – a decision made by the agent.

At each time step, the agent observes the current state, chooses an action, receives a reward, and transitions to a new state. This interaction continues until the task is completed.

## Return

The primary objective of an RL agent is not to maximize immediate reward but to maximize the **return**, which represents the total accumulated future reward.

The return at time step \(t\) is defined as:

\[
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots
\]

where:

- \(R_{t+1}\) is the reward received after taking an action.
- \(\gamma\) is the discount factor \((0 \leq \gamma \leq 1)\).

A discount factor close to 1 makes the agent value future rewards more strongly, while a smaller value makes it focus on immediate rewards.

## Policy

A **policy** defines the behavior of the agent. It specifies which action should be taken in a given state.

A policy is represented as:

\[
\pi(a|s)
\]

which denotes the probability of selecting action \(a\) when the agent is in state \(s\).

Policies can be:

- **Deterministic:** always choose the same action for a state.
- **Stochastic:** choose actions according to probabilities.

The goal of RL is to find an optimal policy that maximizes the expected return.

## Value Functions

Value functions estimate how good it is to be in a state or to take a particular action.

### State-Value Function

The state-value function measures the expected return when starting from state \(s\) and following policy \(\pi\):

\[
V^\pi(s)=E_\pi[G_t|S_t=s]
\]

It tells us how valuable a state is under a given policy.

### Action-Value Function

The action-value function measures the expected return obtained by taking action \(a\) in state \(s\) and then following policy \(\pi\):

\[
Q^\pi(s,a)=E_\pi[G_t|S_t=s,A_t=a]
\]

It helps the agent compare different actions and choose the most rewarding one.

## Exploration vs Exploitation

A fundamental challenge in RL is balancing **exploration** and **exploitation**.

### Exploration

Exploration involves trying new actions to gather information about the environment. Although some actions may initially produce lower rewards, exploration can reveal better strategies in the future.

**Example:** Trying a new route to class even when the current route works.

### Exploitation

Exploitation involves choosing the action currently believed to provide the highest reward based on existing knowledge.

**Example:** Always taking the shortest known route to class.

### Trade-off

Too much exploration wastes time on poor choices, while too much exploitation may prevent discovering better alternatives. Effective RL algorithms maintain a balance between the two.

## Reinforcement Learning as an Optimization Problem

Reinforcement Learning can be viewed as an optimization problem where the objective is to find a policy that maximizes the expected cumulative return.

\[
\pi^* = \arg\max_\pi E[G_t]
\]

where \(\pi^*\) is the optimal policy.

The agent continuously updates its policy using experience gathered from interactions with the environment. Over time, the policy improves, leading to better decision-making and higher rewards.

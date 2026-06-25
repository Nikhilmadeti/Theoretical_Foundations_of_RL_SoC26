# Week 2 Deliverables

## 1. Brief Report on Reinforcement Learning Algorithms

### Q-Learning

Q-Learning is a **model-free, off-policy** reinforcement learning algorithm that learns the optimal action-value function without requiring knowledge of the environment's dynamics. Instead of learning a model of the environment, it directly estimates the expected cumulative reward (Q-value) for every state-action pair using Temporal Difference (TD) learning. The Q-values are updated iteratively based on the reward received and the estimated value of the next state.

The Q-value update rule is:


Q(s,a) ← Q(s,a) + α [r + γ max Q(s',a') − Q(s,a)]


where:

- **α** – Learning rate
- **γ** – Discount factor
- **r** – Immediate reward

Q-Learning is simple, efficient for discrete environments, and guarantees convergence under suitable conditions. However, maintaining a Q-table becomes impractical for environments with large or continuous state spaces.

---

### Monte Carlo Methods

Monte Carlo (MC) methods learn value functions by interacting with the environment and averaging the returns obtained from complete episodes. Unlike Temporal Difference methods, Monte Carlo algorithms wait until an episode terminates before updating value estimates. This allows them to use actual returns instead of estimated future values.

The state value is estimated as:


V(s) = Average(Returns obtained from state s)


Monte Carlo methods are unbiased and easy to understand but usually have high variance and require complete episodes for learning. They are commonly used in episodic tasks where the environment naturally reaches a terminal state.

---

### Proximal Policy Optimization (PPO)

Proximal Policy Optimization (PPO) is a policy-gradient algorithm developed by OpenAI for stable and efficient reinforcement learning. Instead of learning Q-values directly, PPO learns a policy that maps states to actions. It uses a clipped objective function that prevents excessively large policy updates, resulting in more stable training.

PPO is based on the Actor-Critic architecture, where the actor selects actions while the critic estimates the value function. Due to its simplicity, stability, and strong empirical performance, PPO has become one of the most widely used algorithms for robotics, gaming, and continuous control tasks.

---

### Deep Deterministic Policy Gradient (DDPG)

Deep Deterministic Policy Gradient (DDPG) is an off-policy actor-critic algorithm designed for environments with continuous action spaces. It combines deterministic policy gradients with deep neural networks, allowing it to learn directly in high-dimensional environments.

DDPG consists of an actor network that outputs continuous actions and a critic network that evaluates those actions. It also uses experience replay and target networks to improve training stability. Although DDPG performs well in robotics and control problems, it is sensitive to hyperparameter selection and exploration strategies.

---

### Soft Actor-Critic (SAC)

Soft Actor-Critic (SAC) is an off-policy actor-critic algorithm that extends traditional reinforcement learning by maximizing both cumulative reward and policy entropy. The entropy term encourages the agent to maintain randomness in its actions, leading to improved exploration and more robust policies.

Its objective is:


J(π) = Expected [Reward + α × Entropy]


SAC is highly sample-efficient, stable during training, and performs exceptionally well on continuous control benchmarks. Compared to DDPG, SAC generally achieves better performance because its entropy maximization reduces the likelihood of converging to poor local optima.

---

### Deep Q-Network (DQN) 

Deep Q-Network (DQN) extends Q-Learning by replacing the Q-table with a deep neural network that approximates Q-values. It introduced two important innovations: experience replay, which stores past experiences for random sampling, and a target network, which stabilizes learning.

DQN enabled reinforcement learning to solve complex tasks with high-dimensional inputs, such as Atari video games. However, it is primarily designed for discrete action spaces and is less suitable for continuous control problems.

---

# 2. Glossary

| Term | Meaning |
|------|---------|
| Agent | The learner that interacts with the environment. |
| Environment | The external system in which the agent operates. |
| State | The current situation of the environment. |
| Action | A decision made by the agent. |
| Reward | Feedback received after taking an action. |
| Return | Total discounted future reward. |
| Policy | Strategy used by the agent to choose actions. |
| Model-Free | Learns without knowing the environment's transition model. |
| Off-Policy | Learns an optimal policy while following another policy for exploration. |
| On-Policy | Learns using the same policy that generates experiences. |
| Q-Value | Expected return of taking an action in a state. |
| Value Function | Expected return from a state while following a policy. |
| Temporal Difference (TD) Learning | Updates estimates using observed rewards and estimated future values. |
| Episode | A complete sequence of interactions from start to terminal state. |
| Experience Replay | Memory buffer that stores previous experiences for training. |
| Target Network | Separate neural network used to stabilize deep RL updates. |
| Actor | Neural network responsible for selecting actions. |
| Critic | Neural network that evaluates actions or policies. |
| Entropy | Measure of randomness that encourages exploration. |
| Continuous Action Space | Actions can take any real-valued number within a range. |
| Discrete Action Space | Actions are selected from a finite set of choices. |

---

# 3. Short Derivation of Bellman Expectation Equations

## Bellman Expectation Equation for the State-Value Function

The return is defined as:


Gt = Rt+1 + γGt+1


The state-value function is:


Vπ(s) = Eπ[Gt | St = s]


Substituting the definition of return:


Vπ(s) = Eπ[Rt+1 + γGt+1 | St = s]


Replacing the future return with the value of the next state gives:


Vπ(s) = Σa π(a|s) Σs',r P(s',r|s,a) [r + γVπ(s')]


This is called the **Bellman Expectation Equation for the State-Value Function**.

---

## Bellman Expectation Equation for the Action-Value Function

The action-value function is defined as:


Qπ(s,a) = Eπ[Gt | St = s, At = a]


Substituting the recursive definition of return:


Qπ(s,a) = Eπ[Rt+1 + γGt+1 | St = s, At = a]


Expressing the future return using the policy gives:


Qπ(s,a) = Σs',r P(s',r|s,a) [r + γ Σa' π(a'|s') Qπ(s',a')]


This is called the **Bellman Expectation Equation for the Action-Value Function**.


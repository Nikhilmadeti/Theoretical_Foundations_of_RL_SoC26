# Final Project Report


**Implementation and Experimental Evaluation of a Deep Q-Network (DQN) for Reinforcement Learning**

---

# 1. Introduction

Reinforcement Learning (RL) enables an agent to learn optimal behaviour through interactions with an environment by maximizing cumulative rewards. During this project, the theoretical foundations of RL—including Markov Decision Processes, Dynamic Programming, Temporal Difference Learning, Policy Gradient Methods, and Deep Reinforcement Learning—were studied. The practical component focused on implementing a **Deep Q-Network (DQN)** from scratch and evaluating its performance on a standard benchmark environment.

---

# 2. Objectives

The objectives of this project were to:

* Implement a Deep Q-Network (DQN) from scratch.
* Validate the mathematical concepts through implementation.
* Train and evaluate the agent on the CartPole-v1 environment.
* Perform experiments using different hyperparameter settings.
* Analyze the effect of hyperparameters on learning performance.

---

# 3. Methodology

The implementation was developed using **Python**, **PyTorch**, and **Gymnasium**.

The project consists of the following modules:

* Neural Network
* Replay Buffer
* DQN Agent
* Training Module
* Evaluation Module

The neural network approximates the action-value function. A replay buffer stores previous experiences for random sampling, while a target network stabilizes learning. An epsilon-greedy strategy balances exploration and exploitation throughout training.

---

# 4. Experimental Setup

## Environment

* CartPole-v1

## Software

* Python
* PyTorch
* Gymnasium
* NumPy
* Matplotlib

---

# 5. Experiments

Three experiments were performed by modifying DQN hyperparameters.

| Experiment   | Learning Rate | Epsilon Decay | Purpose                  |
| ------------ | ------------: | ------------: | ------------------------ |
| Experiment 1 |         0.001 |         0.995 | Baseline configuration   |
| Experiment 2 |        0.0005 |         0.995 | Smaller learning rate    |
| Experiment 3 |         0.001 |          0.99 | Faster exploration decay |

---

# 6. Results and Observations

## Experiment 1

The baseline configuration showed stable learning and a steady increase in episode rewards. The reward curve demonstrated consistent convergence toward a successful balancing policy.

## Experiment 2

Reducing the learning rate produced smoother updates and more stable learning, although convergence occurred more slowly than in the baseline experiment.

## Experiment 3

Using a faster epsilon decay reduced exploration more quickly. The agent learned faster during the initial stages but explored less in later episodes, which could slightly affect the final policy quality.

---

# 7. Discussion

The implementation demonstrates how classical Q-learning can be extended using deep neural networks. Experience replay reduces the correlation between consecutive training samples, while the target network stabilizes learning by providing fixed targets during updates. These improvements allow DQN to solve environments with continuous state spaces effectively.

The experiments also show that hyperparameter selection influences learning stability, convergence speed, and overall performance.

---

# 8. Limitations

Although the implementation successfully solved the CartPole-v1 environment, the evaluation was limited to a single benchmark environment. More challenging tasks may require deeper neural networks, longer training, or more advanced reinforcement learning algorithms. Future work may include implementing and comparing algorithms such as PPO or SAC.

---

# 9. Conclusion

This project successfully implemented and evaluated a Deep Q-Network for reinforcement learning. The implementation demonstrated the practical application of reinforcement learning concepts, including Q-learning, neural network function approximation, replay buffers, target networks, and epsilon-greedy exploration. Experimental results showed that the DQN agent effectively learned the CartPole-v1 task, and the hyperparameter experiments highlighted the impact of learning rate and exploration strategy on training performance. Overall, the project provided a strong understanding of both the theoretical and practical aspects of Deep Reinforcement Learning.



# Week 8 Report – Final Project Part 1

## Title

**Implementation of a Deep Q-Network (DQN) for the CartPole-v1 Environment**

---

## Objective

The objective of this phase was to implement a baseline Deep Q-Network (DQN) agent from scratch and validate the mapping between the mathematical formulation of the DQN algorithm and its practical implementation. The implementation was tested on the **CartPole-v1** environment provided by Gymnasium.

---

## Environment

The CartPole-v1 environment consists of a cart that moves along a horizontal track with a pole attached by a joint. The objective of the agent is to keep the pole balanced by applying forces to the left or right.

**Environment Details**

* **Environment:** CartPole-v1
* **State Space:** 4 continuous variables
* **Action Space:** 2 discrete actions (Left and Right)
* **Reward:** +1 for every time step the pole remains balanced

---

## Algorithm Implemented

A **Deep Q-Network (DQN)** was implemented from scratch using **PyTorch**. The implementation included the following components:

* Deep Neural Network for Q-value approximation
* Experience Replay Buffer
* Target Network
* Epsilon-Greedy exploration strategy
* Mean Squared Error (MSE) loss function
* Adam optimizer

The neural network consists of two hidden layers with **128 neurons** each using **ReLU activation**.

---

## Project Structure

The implementation was divided into multiple modules:

* `network.py` – Neural network architecture
* `replay_buffer.py` – Experience replay implementation
* `dqn.py` – DQN agent and learning algorithm
* `train.py` – Training script
* `evaluate.py` – Evaluation script

---

## Hyperparameters

| Parameter           | Value |
| ------------------- | ----: |
| Learning Rate       | 0.001 |
| Discount Factor (γ) |  0.99 |
| Batch Size          |    64 |
| Replay Buffer Size  | 10000 |
| Initial ε           |   1.0 |
| Minimum ε           |  0.01 |
| ε Decay             | 0.995 |
| Training Episodes   |   500 |

---

## Initial Results

The DQN agent successfully learned to balance the pole in the CartPole-v1 environment. During training, the episode rewards gradually increased, indicating that the agent learned an effective policy through interaction with the environment.

The implementation generated:

* Trained model (`model.pth`)
* Reward curve (`reward.png`)
* Successful evaluation using the trained model

The implementation verified the correct use of:

* Neural network function approximation
* Experience replay
* Target network updates
* Epsilon-greedy exploration

---

## Conclusion

The baseline DQN implementation successfully solved the CartPole-v1 environment. The project demonstrated how theoretical reinforcement learning concepts—including Q-learning, function approximation, replay buffers, and target networks—can be translated into a working implementation. This baseline serves as the foundation for the experiments and analysis conducted in the final stage of the project.

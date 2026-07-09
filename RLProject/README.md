# Reinforcement Learning Project - Deep Q-Network (DQN)

## Overview

This project implements a **Deep Q-Network (DQN)** from scratch using **PyTorch** and **Gymnasium**. The agent is trained on the **CartPole-v1** environment to learn how to balance a pole using reinforcement learning.

## Project Structure

```text
RL_Project/
├── network.py
├── replay_buffer.py
├── dqn.py
├── train.py
├── evaluate.py
│── Week8_Report.md
│── Final_Report.md
├── results/
│   ├── reward_exp1.png
│   ├── reward_exp2.png
│   ├── reward_exp3.png
└── README.md
```

## Running the Project

Train the agent:

```bash
python train.py
```

Evaluate the trained model:

```bash
python evaluate.py
```

## Results

The DQN agent successfully learned to balance the pole in the CartPole-v1 environment. Three experiments were conducted by varying the learning rate and epsilon decay to compare training performance.

## References

* Sutton & Barto – *Reinforcement Learning: An Introduction*
* David Silver – Reinforcement Learning Lecture Series
* OpenAI Spinning Up
* Gymnasium Documentation

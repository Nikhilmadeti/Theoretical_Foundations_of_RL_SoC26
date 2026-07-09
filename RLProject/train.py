import gymnasium as gym
import matplotlib.pyplot as plt
import os

from dqn import DQNAgent

# Create environment
env = gym.make("CartPole-v1")

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

agent = DQNAgent(state_size, action_size)

episodes = 500
target_update = 10

rewards = []

os.makedirs("results", exist_ok=True)

for episode in range(episodes):

    state, _ = env.reset()
    done = False
    total_reward = 0

    while not done:

        action = agent.act(state)

        next_state, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        agent.remember(state, action, reward, next_state, done)

        agent.replay()

        state = next_state
        total_reward += reward

    rewards.append(total_reward)

    if episode % target_update == 0:
        agent.update_target_network()

    print(
        f"Episode {episode + 1}/{episodes} | "
        f"Reward: {total_reward:.0f} | "
        f"Epsilon: {agent.epsilon:.3f}"
    )

# Save trained model
import torch
torch.save(agent.policy_net.state_dict(), "results/model.pth")

# Plot rewards
plt.figure(figsize=(10, 5))
plt.plot(rewards)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("DQN Training on CartPole-v1")
plt.grid(True)
plt.savefig("results/reward.png")
plt.show()

env.close()
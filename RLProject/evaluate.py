import gymnasium as gym
import torch

from network import DQN

# Create environment
env = gym.make("CartPole-v1", render_mode="human")

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load trained model
model = DQN(state_size, action_size).to(device)
model.load_state_dict(torch.load("results/model.pth", map_location=device))
model.eval()

state, _ = env.reset()
done = False
total_reward = 0

while not done:

    state_tensor = torch.FloatTensor(state).unsqueeze(0).to(device)

    with torch.no_grad():
        action = torch.argmax(model(state_tensor)).item()

    next_state, reward, terminated, truncated, _ = env.step(action)

    done = terminated or truncated

    state = next_state
    total_reward += reward

print(f"Total Reward: {total_reward}")

env.close()
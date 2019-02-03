"""
Built by following:
Tutorial: https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe
Code: https://github.com/simoninithomas/Deep_reinforcement_learning_Course/tree/master/Q%20learning/FrozenLake
"""

import random

import gym
import numpy as np

env = gym.make('FrozenLake-v0')

# Create the Qtable
action_size = env.action_space.n
state_size = env.observation_space.n
qtable = np.zeros((state_size, action_size))

# Output the initial Qtable
print('Qtable: ')
print(qtable)

# Hyperparameters
total_episodes = 10000
learning_rate = 0.85
max_steps = 50
gamma = 0.95  # This is the discount rate

# Exploration parameters - Note that we are using the epsilon greedy strategy

# Exploration rate
epsilon = 1.0
# Exploration probability at start
max_epsilon = 1.0
# Min. exploration prob.
min_epsilon = 0.01
# Exponential decay rate
decay_rate = 0.005

# Start Q learning

rewards = []

for episode in range(total_episodes):
    state = env.reset()
    step = 0
    done = False
    total_reward = 0

    for step in range(max_steps):
        # The exploration exploitation tradeoff
        tradeoff = random.uniform(0, 1)

        if tradeoff > epsilon:
            # Exploitation
            action = np.argmax(qtable[state, :])
        else:
            # Exploration
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # Update the Qtable - Bellman's Formula
        qtable[state, action] = qtable[state, action] + learning_rate * (
                    reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])

        # Update the state
        state = new_state

        total_reward += reward

        if done == True:
            break

    # Reduce epsilon
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    rewards.append(total_reward)

print('Score over time: ' + str(sum(rewards) / total_episodes))
print('The Qtable after training is: ')
print(qtable)

# Now use this Qtable to play FrozenLake

env.reset()
# We are playing the game 10 times
for episode in range(10):
    state = env.reset()
    step = 0
    done = False
    print('Episode: ' + str(episode))
    for step in range(max_steps):
        action = np.argmax(qtable[state, :])

        new_state, reward, done, info = env.step(action)
        env.render()

        if done:
            print('Finished with a proper end. Number of steps: ' + str(step))
            break
        state = new_state
    print('Episode ' + str(episode) + ' finished!')

env.close()

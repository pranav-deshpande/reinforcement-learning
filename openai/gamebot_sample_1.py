import gym
import time

env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    time.sleep(0.05)
    env.render()
    env.step(env.action_space.sample())

env.close()

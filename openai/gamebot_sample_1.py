# Basic example : https://gym.openai.com/docs/
# Note the extra time.sleep(..) and env.close() statements

import gym
import time

env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    time.sleep(0.05)
    env.render()
    env.step(env.action_space.sample())

env.close()

# -*- coding: utf-8 -*-
"""
Lectorial 5 - Implementing Intelligent Agents
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

#%% import python libs
import gym

#%% general agent class
class Agent:
    def __init__(self, env):
        self.env = env

    def get_random_action(self):
        action = self.env.action_space.sample()
        return action

    def play(self, num_episodes):
        rewards = [0.0] * num_episodes
        
        for i_episode in range(num_episodes):
            observation = env.reset()
            score = 0.0
            
            for t in range(100):
                self.env.render()
                action = self.get_random_action()
                observation, reward, done, info = env.step(action)
                score += reward
                if done:
                    rewards[i_episode] = score
                    print("Scored {} in episode {}".format(score, i_episode+1))
                    break
        return rewards

#%% Run
env = gym.make("CartPole-v0")
agent = Agent(env)
rewards = agent.play(num_episodes=20)

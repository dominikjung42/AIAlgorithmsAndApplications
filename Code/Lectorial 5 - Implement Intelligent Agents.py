# -*- coding: utf-8 -*-
"""
Lectorial 5 - Implementing Intelligent Agents
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

#%% import python libs
import gym
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical


#%% general agent class
class Agent:
    def __init__(self, env):
        self.env = env
        self.observations = 4
        self.actions = 2
        self.model = self.generate_model(num_input_dim = self.observations, 
                                         num_output_dim = self.actions)
    
    def generate_model(self, num_input_dim, num_output_dim):
        model = Sequential()
        model.add(Dense(units=100, input_dim=num_input_dim))
        model.add(Activation("relu"))
        model.add(Dense(units=num_output_dim)) # Output: Action [L, R]
        model.add(Activation("softmax"))
        model.summary()
        model.compile(
            optimizer="sgd",  #Gradient descent (with momentum) optimizer
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )
        return model

    def get_action(self, observation):
        observation = observation.reshape(1,-1)
        action = self.model(observation).numpy()[0]
        action = np.random.choice(self.actions, p = action)
        return action
    
    def get_samples(self, num_episodes):
        rewards = [0.0] * num_episodes
        episodes = list()
        for i in range(num_episodes):
            episodes.append([])
        
        for episode in range(num_episodes):
            observation = self.env.reset()
            score = 0.0
        
        while True: 
            action = self.get_action(observation)
            new_observation, reward, done, info = env.step(action)
            score += reward
            episodes[episode].append((observation, action))
            observation = new_observation
            if done:
                rewards[episode] = score
                break
        return rewards, episodes
    
    def filter_episodes(self, rewards, episodes, percentile):
        reward_bound = np.percentile(rewards, percentile)
        x_train, y_train = [],[]
        for i in range(len(rewards)):
            reward, episode = (rewards[i], episodes[i])
            if reward >= reward_bound:
                observation = list()
                for step in episode:
                    observation.append(step[0])
                action = list()
                for step in episode:
                    action.append(step[1])
                
                x_train.extend(observation)
                y_train.extend(action)
        x_train = np.asarray(x_train)
        y_train = to_categorical(y_train, num_classes=self.actions)
        return x_train, y_train, reward_bound
    
    def train(self, percentile, num_iterations, num_episodes):
        for iteration in range (num_iterations):
            rewards, episodes = self.get_samples(num_episodes)
            x_train, y_train, reward_bound = self.filter_episodes(rewards, episodes, percentile)
            self.model.fit(x= x_train, y = y_train, verbose=0)
            reward_mean = np.mean(rewards)
            print(f"Reward mean: {reward_mean}, reward bound: {reward_bound}")
            if reward_mean > 500:
                break
    
    def play(self, num_episodes):
        for i_episode in range(num_episodes):
            observation = self.env.reset()
            score = 0.0
            
            while True:
                self.env.render()
                action = self.get_action(observation)
                observation, reward, done, info = env.step(action)
                score += reward
                if done:
                    break
#%% Run
env = gym.make("CartPole-v0")
agent = Agent(env)
print(agent.observations)
print(agent.actions)

agent.train(percentile=70.0, num_iterations=15, num_episodes=100)
agent.play(num_episodes=5)




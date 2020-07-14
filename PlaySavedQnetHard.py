import abc
import tensorflow as tf
import numpy as np

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

import GameHard
import DisplayIA

from tensorflow import keras

class YoushiEnv(py_environment.PyEnvironment):
    
    def __init__(self):
        self._env = GameHard.Game()
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=2, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(10, 2), dtype=np.float64, minimum=-999, maximum=600, name='observation')
        self._state = self._env.reset()
        self._episode_ended = False
        
    def action_spec(self):
        return self._action_spec
    
    def observation_spec(self):
        return self._observation_spec
    
    def _reset(self):
        self._state = self._env.reset()
        self._episode_ended = False
        return ts.restart(self._state)
    
    def _step(self, action):
        
        if self._episode_ended:
            return self.reset()
        
        cumulative_reward = 0
        cumulative_done = False
        obs, reward, done, info = self._env.step(action)
        cumulative_reward += reward
        self._state = obs
        if (done):
            cumulative_done = True
        
        if cumulative_done:
            self._episode_ended = True
            return ts.termination(self._state, reward)
        else:
            return ts.transition(self._state, reward, discount=0.98)

from tf_agents.environments.tf_py_environment import TFPyEnvironment

tf_env = TFPyEnvironment(YoushiEnv)
#tf_env = YoushiEnv()

#tf_agent = tf.saved_model.load(saved_models_path)
q_net = tf.saved_model.load("MyPolicyHard")

time_step = tf_env.reset()
display = DisplayIA.Display()

lost = False
score = 0

print(type(q_net))

while not time_step.is_last():
	display.refresh(time_step.observation)
	action = q_net.action(time_step)
	time_step = tf_env.step(action)
	score += 1

print(score)
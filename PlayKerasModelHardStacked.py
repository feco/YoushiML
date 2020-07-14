from tensorflow import keras
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np

import GameHard
import DisplayIA

class StackedFrame:
    def __init__(self):
        self.data = []
        
    def append(self, frame):
        self.data.append(frame)
        
        while(len(self.data) < 4) :
            self.data.append(frame)
            
        while(len(self.data) > 4) :
            self.data.pop(0)
    
    def reset(self):
        self.data = []
        
    def get(self):
        return np.asarray(self.data)





env = GameHard.Game()
model = load_model('kerasDQL.h5')

obs = env.reset()
obs = np.divide(obs, 1000)
display = DisplayIA.Display()

lost = False
score = 0

stacked_frame = StackedFrame()
stacked_frame.append(obs)

while not lost:
	display.refreshOld(env.player, env.trees)
	Q_values = model.predict(stacked_frame.get()[np.newaxis])
	print(Q_values)
	action = np.argmax(Q_values[0])
	obs, reward, lost, _ = env.step(action)
	obs = np.divide(obs, 1000)
	stacked_frame.append(obs)
	
	score += 1

print(score)
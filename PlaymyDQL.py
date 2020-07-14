from tensorflow import keras
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np

import GameHard
import DisplayIA

env = GameHard.Game()
model = load_model('myDQL.h5')

obs = env.reset()
display = DisplayIA.Display()

lost = False
score = 0


while not lost:
	display.refreshOld(env.player, env.trees)
	Q_values = model.predict(obs[np.newaxis])
	print(Q_values)
	action = np.argmax(Q_values[0])
	obs, reward, lost, _ = env.step(action)
	score += 1

print(score)
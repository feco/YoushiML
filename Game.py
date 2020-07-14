import numpy as np
from PIL import Image

WINDOW_X = 400
WINDOW_Y = 600

RENDER = False

class Player:
	def __init__(self):
		self.pos_x = np.random.randint(150, 250)
		self.pos_y = 0
		self.sprite_size_x = 16
		self.sprite_size_y = 24

	def move(self, direction):
		if direction == 0:
			pass
		elif direction == 1:
			self.pos_x -= 10
		elif direction == 2:
			self.pos_x += 10

		if self.pos_x < 0:
			self.pos_x = 0
		if self.pos_x > WINDOW_X - self.sprite_size_x :
			self.pos_x = WINDOW_X - self.sprite_size_x

class Tree:
	def __init__(self):
		self.sprite_size_x = 40
		self.sprite_size_y = 40
		self.pos_x = np.random.randint(0, WINDOW_X - self.sprite_size_x)
		self.pos_y = WINDOW_Y

	def tick(self, speed):
		self.pos_y -= speed

class Game:
	def __init__(self):
		self.window_x = WINDOW_X
		self.window_y = WINDOW_Y
		self.actions = 3
		self.player = Player()
		self.trees = []
		self.score = 0
		self.lost = False
		self.speed = 8
		self.observation_shape = (10, 2)
		self.action_shape = (3,)

	def reset(self):
		self.player = Player()
		self.trees = []
		self.score = 0
		self.lost = False
		self.speed = 8

		return self.get_state()

	def tick(self, action):
		self.player.move(action)
		for tree in self.trees:
			tree.tick(self.speed)

			if (self.player.pos_x < (tree.pos_x + tree.sprite_size_x) and (self.player.pos_x + self.player.sprite_size_x) > tree.pos_x
				and self.player.pos_y < (tree.pos_y + tree.sprite_size_y) and (self.player.pos_y + self.player.sprite_size_y) > tree.pos_y):
				self.lost = True

			if tree.pos_y < -tree.sprite_size_y:
				self.trees.remove(tree)

		if self.score % 20 == 0:
			self.trees.append(Tree())
		
		if self.score % 120 == 0:
			self.speed += 1

		self.score += 1

		if self.lost:
			print("LOST ! Score : " + str(self.score))

		return self.lost

	def step(self, action):
		self.player.move(action)
		for tree in self.trees:
			tree.tick(self.speed)

			if (self.player.pos_x < (tree.pos_x + tree.sprite_size_x) and (self.player.pos_x + self.player.sprite_size_x) > tree.pos_x
				and self.player.pos_y < (tree.pos_y + tree.sprite_size_y) and (self.player.pos_y + self.player.sprite_size_y) > tree.pos_y):
				self.lost = True

			if tree.pos_y < -tree.sprite_size_y:
				self.trees.remove(tree)

		if self.score % 20 == 0:
			self.trees.append(Tree())
		
		if self.score % 120 == 0:
			self.speed += 1

		self.score += 1

		reward = 1

		if self.lost:
			reward = 0

		return self.get_state(), reward, self.lost, reward

	def get_state(self):
		i = 0
		state = []
		state.append([float(self.player.pos_x), float(self.player.pos_y)])
		i+=1
		for tree in self.trees:
			state.append([float(tree.pos_x), float(tree.pos_y)])
			i+=1
		while i < 10 :
			state.append([float(-999), float(-999)])
			i+=1
		
		return np.asarray(state)


	def get_image(self):
		env = np.zeros((int(self.window_y/4), int(self.window_x/4), 3), dtype=np.uint8)  # starts an rbg of our size
		env[int(self.player.pos_y/4):int((self.player.pos_y+self.player.sprite_size_y)/4), int(self.player.pos_x/4):int((self.player.pos_x+self.player.sprite_size_x)/4)] = (255, 0, 0)
		for tree in self.trees:
			env[int(tree.pos_y/4):int((tree.pos_y+tree.sprite_size_y)/4), int(tree.pos_x/4):int((tree.pos_x+tree.sprite_size_x)/4)] = (0, 255, 0)
		img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
		return img
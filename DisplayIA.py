import sys, pygame
import Game

WINDOW_X = 400
WINDOW_Y = 600

class Display:
	def __init__(self):
		pygame.init()
		self.size = width,  height = WINDOW_X, WINDOW_Y

		self.screen = pygame.display.set_mode(self.size)

		self.youshi = pygame.image.load("youshineige.png")

		self.treeSurface = pygame.image.load("arbre.png")

		self.white = 255, 255, 255

	def refreshOld(self, player, trees):
		self.screen.fill(self.white)
		self.screen.blit(self.youshi, (player.pos_x, player.pos_y))
		for tree in trees :
			self.screen.blit(self.treeSurface, (tree.pos_x, tree.pos_y))
		pygame.display.flip()
		pygame.event.pump()
		pygame.time.wait(16)

	def refresh(self, obs):
		print(obs)
		self.screen.fill(self.white)
		self.screen.blit(self.youshi, (obs[0, 0, 0].numpy(), obs[0, 0, 1].numpy()))
		for i in range(9) :
			self.screen.blit(self.treeSurface, (obs[0, i+1, 0].numpy(), obs[0, i+1, 1].numpy()))
		pygame.display.flip()
		pygame.event.pump()
		pygame.time.wait(16)
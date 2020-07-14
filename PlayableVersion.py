import sys, pygame
import GameHard

pygame.init()

game = GameHard.Game()

size = width,  height = game.window_x, game.window_y

screen = pygame.display.set_mode(size)

youshi = pygame.image.load("youshineige.png")

treeSurface = pygame.image.load("arbre.png")

white = 255, 255, 255


finished = False

while not finished:
	pygame.time.wait(16)

	move = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	pressed = pygame.key.get_pressed()
	if (pressed[pygame.K_a]):
		print("move left")
		move = 1
	if (pressed[pygame.K_d]):
		print("move right")
		move = 2

	lost = game.tick(move)
	if lost:
		finished = True

	screen.fill(white)

	youshi_rect = game.player.pos_x
	screen.blit(youshi, (game.player.pos_x, game.player.pos_y))
	for tree in game.trees :
		screen.blit(treeSurface, (tree.pos_x, tree.pos_y))
	pygame.display.flip()

print(game.score)
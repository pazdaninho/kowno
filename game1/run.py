import pygame
#komentar
pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
	pygame.draw.line(window, (255,255,255),
							(50,50), (75, 75), True)

	pygame.display.update()
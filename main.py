import pygame

print('Setup Sstar')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('setup End')

while True:
	# check for all events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Close Window
			pygame.quit()  # end pygame
			quit()

from pygame import *
import sys, pygame
pygame.init()

size = width, height = 1024,1024

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Gold Trash Dash')

tux = pygame.image.load('images/back.png')
zachImg = pygame.image.load('images/Zach.png')
runrightImg = pygame.image.load('images/runright.png')
runleftImg = pygame.image.load("images/runleft.png')
gameIcon = pygame.image.load('images/gameicon.png')

pygame.display.set_icon(gameIcon)



screen.blit(tux,(1024,1024))
screen.blit(tux,(0,0))


pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()
###


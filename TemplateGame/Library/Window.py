import os
import pygame

Title = ""
window_width = 1200
window_height = 800
FPS = 60

Frame = pygame.display.set_mode((window_width, window_height))

def RenderText(screen, text, x, y, size,color, font_location):
	text = str(text)
	font = pygame.font.Font(font_location, size)
	text = font.render(text, True, color)
	screen.blit(text, (x, y))

def Settings(title, width, height):
	Title = title
	window_width = width
	window_height = height
	pygame.display.set_caption(title)

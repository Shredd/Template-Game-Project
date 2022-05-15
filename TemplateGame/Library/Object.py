import os
import pygame

Camx = 0
Camy = 0

def Draw_Image(win, Image, x, y, width, height):
	win.blit(Image, (x,y,width,height))

def Collison(x1, y1, w1, h1, x2, y2, w2, h2):
	if (x2 - Camx + w2 >= x1 >= x2 - Camx and y2- Camy + h2 >= y1 >= y2 - Camy):
		return True
	elif (x2 - Camx + w2 >= x1 + w1 >= x2 - Camx and y2 - Camy + h2 >= y1 >= y2 - Camy):
		return True
	elif (x2 - Camx + w2 >= x1 >= x2 - Camx and y2 - Camy + h2 >= y1 + h1 >= y2 - Camy):
		return True
	elif (x2 - Camx + w2 >= x1 + w1 >= x2 - Camx and y2 - Camy + h2 >= y1 + h1 >= y2 - Camy):
		return True
	else:
		return False	

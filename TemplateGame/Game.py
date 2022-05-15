import pygame
import Player
import Library.Object
import Library.ColorCode
import Library.Window
import Library.Graphics

Library.Window.Settings("[Your Game Title]", 1000, 800)

pygame.init()

colornum = 70
rectx = 60
recty = 60 
rectwidth = 50
rectheight = 50
setCharnum = 1

image = pygame.image.load('Assets/image.png')

def setStat(CharNum):
	if CharNum == 1:
		Player.vel = 4
	if CharNum == 2:
		Player.vel = 8
	if CharNum == 3:
		Player.vel = 12

def setSprite(setChar):
	if setChar == 1:
		setStat(1)
		if Player.Idle:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
			Library.Graphics.Draw_Image(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
		if Player.left:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
		elif Player.right:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
	elif setChar == 2:
		setStat(2)
		if Player.Idle:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
		if Player.left:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
		elif Player.right:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
	elif setChar == 3:
		setStat(3)
		if Player.Idle:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
		if Player.left:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))
		elif Player.right:
			pygame.draw.rect(Library.Window.Frame, Player.player_color, (Player.x, Player.y,Player.width,Player.height))	
			
def setCollisons():
	collisons = Library.Object.Collison(Player.x,Player.y,Player.width,Player.height,rectx,recty,rectwidth,rectheight)
	
	if collisons == True:
		pygame.draw.rect(Library.Window.Frame, (0, 0, colornum), (rectx - Library.Object.Camx, recty - Library.Object.Camy,rectwidth,rectheight))
	else: 
		pygame.draw.rect(Library.Window.Frame, (0, 255, 0), (rectx - Library.Object.Camx, recty - Library.Object.Camy,rectwidth,rectheight))	

def renderObjects():
	Library.Window.Frame.fill(Library.ColorCode.White)	
	
	Library.Window.RenderText(Library.Window.Frame, 'speed: ' + str(setCharnum),30, 30,50, (0,0,0), '/usr/share/fonts/truetype/freefont/FreeMono.ttf')
	setSprite(setCharnum)
	setCollisons()
	pygame.display.update()

run = True
while run:
	pygame.time.delay(Library.Window.FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a]:
		Library.Object.Camx -= Player.vel
		Player.left = True
		Player.right = False
		Player.Idle = False
	else:
		right = False
		left = False
		Idle = True
	
	if keys[pygame.K_d]:
		Library.Object.Camx += Player.vel
		Player.right = True
		Player.left = False
		Player.Idle = False
	else:
		Player.right = False
		Player.Left = False
		Player.Idle = True
	
	if keys[pygame.K_w]:
		Library.Object.Camy -= Player.vel	
	
	if keys[pygame.K_s]:
		Library.Object.Camy += Player.vel	
	
	if keys[pygame.K_i]:
		setCharnum += 1
		if setCharnum > 3:
			setCharnum = 1
		
	renderObjects()
			
pygame.quit()			

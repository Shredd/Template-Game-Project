import pygame
import Player
import Library.Object
import Library.ColorCode
import Library.Window
import Library.Graphics

Library.Window.Settings("[Your Game Title]", 1000, 800)
Font = "Assets/Font/[NAME OF FONT].ttf"

pygame.init()

colornum = 70
rectx = 60
recty = 60 
rectwidth = 50
rectheight = 50
setCharnum = 1

image = pygame.image.load('Assets/image.png')

def setPlayerDrawing():
	Player.Set_DebugBox(False, Library.Window.Frame, Player.player_color, Player.x, Player.y,Player.width,Player.height)
	if Player.Idle:
		Player.Draw_Player(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
	elif Player.left:
		Player.Draw_Player(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
	elif Player.right:
		Player.Draw_Player(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
	elif Player.down:
		Player.Draw_Player(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
	elif Player.up:
		Player.Draw_Player(Library.Window.Frame, image, Player.x, Player.y, Player.width, Player.height)
			
def setCollisons():
	collisons = Library.Object.Collison(Player.x,Player.y,Player.width,Player.height,rectx,recty,rectwidth,rectheight)
	
	if collisons == True:
		pygame.draw.rect(Library.Window.Frame, (0, 0, colornum), (rectx - Library.Object.Camx, recty - Library.Object.Camy,rectwidth,rectheight))
	else: 
		pygame.draw.rect(Library.Window.Frame, (0, 255, 0), (rectx - Library.Object.Camx, recty - Library.Object.Camy,rectwidth,rectheight))	

def renderObjects():
	Library.Window.Frame.fill(Library.ColorCode.White)	
	
	Library.Window.RenderText(Library.Window.Frame, 'speed: ' + str(setCharnum),30, 30,50, (0,0,0), Font)
	setPlayerDrawing()
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
		Player.Idle - False	
		Player.right = False
		Player.left = True
		Player.down = False
		Player.Up = False

	elif keys[pygame.K_d]:
		Library.Object.Camx += Player.vel
		Player.Idle - False	
		Player.right = True
		Player.left = False
		Player.down = False
		Player.Up = False

	elif keys[pygame.K_w]:
		Library.Object.Camy -= Player.vel
		Player.Idle - False	
		Player.right = False
		Player.left = False
		Player.down = False
		Player.Up = True
	
	elif keys[pygame.K_s]:
		Library.Object.Camy += Player.vel
		Player.Idle - False	
		Player.right = False
		Player.left = False
		Player.down = True
		Player.Up = False

	else:
		Player.Idle - True	
		Player.right = False
		Player.left = False
		Player.down = False
		Player.Up = False
		
	renderObjects()
			
pygame.quit()			

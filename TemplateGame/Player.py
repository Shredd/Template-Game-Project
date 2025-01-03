import os
import pygame
import Library.Graphics

x = 560
y = 250
width = 40
height = 60
player_color = (0, 0, 70)

vel = 15
left = False
right = False
up = False
down = False
Idle = True

def Set_DebugBox(enabled, win, color, x, y, width, height):
    if enabled == True:
        pygame.draw.rect(win, color, (x, y,width,height))

def Draw_Player(win, Image, x, y, width, height):
    Library.Graphics.Draw_Image(win, Image, x, y, width, height)
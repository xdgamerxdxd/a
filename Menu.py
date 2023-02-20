import pygame
import time
import sys
from pygame.locals import *

global width, height
width = 1920
height = 1080

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class image_button_maker():
    def __init__(self, img, surface, x, y):
        super(image_button_maker, self).__init__()
        self.surface = surface
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def button(self):
        self.surface.blit(self.image, self.rect)

class main_menu():
    def __init__(self, screen):
        self.screen = screen
        self.state = False

    def run(self, function):
        pygame.init()
        global font
        font = pygame.font.SysFont('Monocraft', 100)
        bfont = pygame.font.SysFont('Monocraft', 40)
        i = image_button_maker('other/c.png', self.screen, 0, 490)
        e = image_button_maker('other/d.png', self.screen, 1500, 676)
        click = False
        while self.state:

            pygame.Surface.blit(self.screen, pygame.image.load('other/mean.png'), (0, 20))
            draw_text('Minecraft', font, (255,255,255), self.screen, 960, 40)
            i.button()
            e.button()
            mx, my = pygame.mouse.get_pos()

            button = pygame.Rect(50, 100, 200, 50)
            button1 = pygame.Rect(50, 200, 200, 50)

            rect = pygame.draw.rect(self.screen, (255,0,0), button)
            draw_text('Fuck you', bfont, (255,255,255), self.screen, rect.centerx, rect.centery)
            rect1 = pygame.draw.rect(self.screen, (255,0,0), button1)
            draw_text('Re-fuck you', bfont, (255,255,255), self.screen, rect1.centerx, rect1.centery)

            if button.collidepoint((mx, my)):
                if click:
                    pygame.display.quit()
                    sys.exit()
            if button1.collidepoint((mx, my)):
                if click:
                    function()
                    self.state = False
            if i.rect.collidepoint((mx, my)):
                if click:
                    print('Amongus!')
            if e.rect.collidepoint((mx, my)):
                if click:
                    print('No Amongus!')
            
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE and self.state == True:
                        self.state = False
                        pygame.display.set_icon(pygame.image.load('other/b.png'))
                        pygame.display.set_caption("Game")
                        time.sleep(0.08)
            pygame.display.update()
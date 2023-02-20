import pygame
from sprites import *


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()

        self.image = pygame.image.load(f'{w}nowepon.png')

        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()
        self.facing = ''
        self.on = False
        self.count = False
        self.counter = 10

    def update(self, facing, rectx, recty):
        k = pygame.key.get_pressed()
        #bone attack
        if facing == 'right' and self.count == False:
            self.rect.x = rectx + 50
        if facing == 'left' and self.count == False:
            self.rect.x = rectx - 55

        if k[pygame.K_i] and self.count == False:
            self.count = True
            self.on = True
            self.counter = 10
            self.rect.y = recty - 40
            if facing == 'right':
                self.facing = 'right'
            else:
                self.facing = 'left'

        if self.count == True:
            self.image = pygame.image.load(f'{w}san_attack.png')
            self.counter -= 1
            if self.facing == 'right':
                self.rect.x += 20
            if self.facing == 'left':
                self.rect.x -= 20

        if self.counter == -10:
            self.count = False
            self.on = False
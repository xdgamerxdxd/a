import pygame
from Menu import width, height

global c, w, p, pi
c = 'skins/characters/'
w = 'skins/weabone/'
p = 'skins/characters/player/'
pir = 'skins/characters/player/idre/'
pil = 'skins/characters/player/idle/'

class Player(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super(Player, self).__init__()


        self.idre = [pygame.image.load(f'{pir}char (1).png'), pygame.image.load(f'{pir}char (2).png'),pygame.image.load(f'{pir}char (3).png'),
        pygame.image.load(f'{pir}char (4).png'), pygame.image.load(f'{pir}char (5).png'), pygame.image.load(f'{pir}char (6).png'),
        pygame.image.load(f'{pir}char (7).png'), pygame.image.load(f'{pir}char (8).png'), pygame.image.load(f'{pir}char (9).png'),
        pygame.image.load(f'{pir}char (10).png')]
        
        self.idle = [pygame.image.load(f'{pil}chal (1).png'), pygame.image.load(f'{pil}chal (2).png'),pygame.image.load(f'{pil}chal (3).png'),
        pygame.image.load(f'{pil}chal (4).png'), pygame.image.load(f'{pil}chal (5).png'), pygame.image.load(f'{pil}chal (6).png'),
        pygame.image.load(f'{pil}chal (7).png'), pygame.image.load(f'{pil}chal (8).png'), pygame.image.load(f'{pil}chal (9).png'),
        pygame.image.load(f'{pil}chal (10).png')]
        self.idlecount = 0
        self.type = type
        if self.type == 'p':
            self.image = self.idre[self.idlecount]
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load(f'{c}filename.png')
            self.rect = self.image.get_rect()
        self.facing = ''
        self.rect.x = x
        self.rect.y = y
        self.wants_jump = False
        self.gravity = False
        self.positiony = y
        self.ground = y
        self.jumpy = False
        self.fally = False

    def update(self, speed, left, right, up):
        k = pygame.key.get_pressed()
        # Idle animation here
        self.idlecount += 1

        if self.idlecount >= len(self.idre):
            self.idlecount = 0
        # makes character player
        if self.type == 'p':

            self.image = self.idre[self.idlecount]

            if self.facing == 'right':
                self.image = self.idre[self.idlecount]

            elif self.facing == 'left':
                self.image = self.idle[self.idlecount]

            if k[left] and self.rect.x > 0:
                    self.image = pygame.image.load(f'{p}chal.png')
                    self.rect.x -= speed
                    self.facing = 'left'

            if k[right] and self.rect.x < width - self.rect.width:
                    self.image = pygame.image.load(f'{p}char.png')
                    self.rect.x += speed
                    self.facing = 'right'
        # makes character enemy
        else:
             if k[left] and self.rect.x > 0:
                self.image = pygame.image.load(f'{c}filename.png')
                self.rect.x -= speed
                self.facing = 'left'

             if k[right] and self.rect.x < width - self.rect.width:
                self.image = pygame.image.load(f'{c}filenamel.png')
                self.rect.x += speed
                self.facing = 'right'
        # This make the thingie go uppy
        if k[up] and self.fally == False:
            self.jumpy = True

        if self.jumpy == True:
            if self.rect.y > self.positiony - 300:  
                self.rect.y -= speed
            if self.rect.y > self.positiony - 350:
                self.rect.y -= speed / 2
            if self. rect.y > self.positiony - 400:
                self.rect.y -= speed / 4

        if k[up] == False and self.jumpy == True or self.rect.y <= self.positiony - 400:
            self.jumpy = False
            self.gravity = True
            self.fally = True
        
        if self.gravity == True:
            self.rect.y += speed
            if self.rect.y >= self.ground:
                self.gravity = False
                self.fally = False

            
class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()

        self.image = pygame.image.load(f'{w}nowepon.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def update(self, facing, rectx, recty, button, type):
        self.atk = False
        k =  pygame.key.get_pressed()
        #meele attack
        if k[button]:
            if facing == 'right':
                self.image = pygame.image.load(f'{w}swor.png')
                self.rect = self.image.get_rect()
                if type == 'p':
                    self.rect.x = rectx + 110
                    self.rect.y = recty - 15
                else:
                     self.rect.x = rectx + 200
                     self.rect.y = recty - 15
                self.atk = True
            elif facing == 'left':
                self.image = pygame.image.load(f'{w}swol.png')
                self.rect = self.image.get_rect()
                if type == 'p':
                    self.rect.x = rectx - 65
                    self.rect.y = recty - 15
                else:
                    self.rect.x = rectx - 65
                    self.rect.y = recty - 15
                self.atk = True
        else:
            self.image = pygame.image.load(f'{w}nowepon.png')
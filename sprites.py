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
        self.wants_down = False

    def update(self, speed, left, right, up, down):
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
                            # Make thing go up (Jump up)
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

        if k[up] and self.rect.y > 0 and self.wants_down == False:
            self.wants_jump = True
        if self.wants_jump == True:
            if self.rect.y > 800:
                self.rect.y -= speed
            if self.rect.y > 780:
                self.rect.y -= speed / 2
            if self.rect.y > 700:
                self.rect.y -= speed / 4
            if self.rect.y == 700:
                self.wants_jump = False
                self.wants_down = True

        # Make thing to down (Fall down)
        if self.wants_down == True and self.rect.y < 860:
            self.rect.y += speed
            if self.rect.y == 860:
                self.wants_down = False
            
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
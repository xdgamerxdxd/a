import pygame
from Menu import width, height

global c, w, p, pi
c = 'skins/characters/'
w = 'skins/weabone/'
p = 'skins/characters/player/'
pir = 'skins/characters/player/idre/'
pil = 'skins/characters/player/idle/'

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.image = self.idre[self.idlecount]
        self.rect = self.image.get_rect()
        self.facing = ''
        self.rect.x = x
        self.rect.y = y

    def update(self, speed, left, right, up, down):
        k = pygame.key.get_pressed()

        # Idle animation here
        self.idlecount += 1

        if self.idlecount >= len(self.idre):
            self.idlecount = 0

        self.image = self.idre[self.idlecount]

        if self.facing == 'right':
            self.image = self.idre[self.idlecount]

        elif self.facing == 'left':
            self.image = self.idle[self.idlecount]

        # Movement starts here
        if k[left] and self.rect.x > 0:
            self.image = pygame.image.load(f'{p}chal.png')
            self.rect.x -= speed
            self.facing = 'left'

        if k[right] and self.rect.x < width - self.rect.width:
            self.image = pygame.image.load(f'{p}char.png')
            self.rect.x += speed
            self.facing = 'right'

        if k[up] and self.rect.y > 0:
            self.rect.y -= speed

        if k[down] and self.rect.y < height - self.rect.height:
            self.rect.y += speed
            
class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()

        self.image = pygame.image.load(f'{w}nowepon.png')

        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()
        self.facing = ''

    def update(self, facing, rectx, recty):
        self.atk = False
        k =  pygame.key.get_pressed()
        #meele attack
        if k[pygame.K_o]:
            if facing == 'right':
                self.image = pygame.image.load(f'{w}swor.png')
                self.rect = self.image.get_rect()
                self.rect.x = rectx + 110
                self.rect.y = recty - 15
                self.atk = True
            elif facing == 'left':
                self.image = pygame.image.load(f'{w}swol.png')
                self.rect = self.image.get_rect()
                self.rect.x = rectx - 65
                self.rect.y = recty - 15
                self.atk = True
        else:
            self.image = pygame.image.load(f'{w}nowepon.png')
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()

        self.image = pygame.image.load(f'{c}filename.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.live = True

    def update(self, speed):
        k = pygame.key.get_pressed()
        if self.live == True:

            if k[pygame.K_a] and self.rect.x > 0:
                self.image = pygame.image.load(f'{c}filename.png')
                self.rect.x -= speed
                self.facing = 'left'

            if k[pygame.K_d] and self.rect.x < width - self.rect.width:
                self.image = pygame.image.load(f'{c}filenamel.png')
                self.rect.x += speed
                self.facing = 'right'

            # Make thing go up (Jump up)
            if k[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= speed

            if k[pygame.K_s] and self.rect.y < height - self.rect.height:
                self.rect.y += speed

class Eattack(pygame.sprite.Sprite):
    def __init__(self):
        super(self, Eattack).__init__()
   
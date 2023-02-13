import pygame

global c, w
c = 'skins/characters/'
w = 'skins/weabone/'

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.image.load(f'{c}player.png')
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.facing = ''
        self.rect.x = x
        self.rect.y = y
        self.live = True

    def update(self, speed):
        k = pygame.key.get_pressed()
        if self.live == True:

            if k[pygame.K_LEFT] and self.rect.x > 0:
                self.image = pygame.image.load(f'{c}player.png')
                self.image = pygame.transform.scale(self.image, (80,80))
                self.rect.x -= speed
                self.facing = 'left'

            if k[pygame.K_RIGHT] and self.rect.x < 1920 - self.rect.width:
                self.image = pygame.image.load(f'{c}playerr.png')
                self.image = pygame.transform.scale(self.image, (80,80))
                self.rect.x += speed
                self.facing = 'right'

            if k[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= speed


            if k[pygame.K_DOWN] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += speed
            
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

            if k[pygame.K_d] and self.rect.x < 1920 - self.rect.width:
                self.image = pygame.image.load(f'{c}filenamel.png')
                self.rect.x += speed
                self.facing = 'right'

            # Make thing go up (Jump up)
            if k[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= speed

            if k[pygame.K_s] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += speed
            
class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()

        self.image = pygame.image.load(f'{w}nowepon.png')

        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()

        self.on = False
        self.count = False
        self.counter = 10
        self.facing = ''

    def update(self, facing, rectx, recty):

        k =  pygame.key.get_pressed()
        # what attack looks like without pushing button
        self.image = pygame.image.load(f'{w}nowepon.png')

        #meele attack
        if k[pygame.K_o]:
            if facing == 'right':
                self.image = pygame.image.load(f'{w}swor.png')
                self.image = pygame.transform.scale(self.image, (150, 100))
                self.rect = self.image.get_rect()
                self.rect.x = rectx + 40
                self.rect.y = recty - 50
                self.atk = True
            elif facing == 'left':
                self.image = pygame.image.load(f'{w}swol.png')
                self.image = pygame.transform.scale(self.image, (150, 100))
                self.rect = self.image.get_rect()
                self.rect.x = rectx - 200
                self.rect.y = recty - 50
                self.atk = True

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
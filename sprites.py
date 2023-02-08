import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.image.load('skins/player.png')
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.live = True

    def update(self, speed):
        keys = pygame.key.get_pressed()
        if self.live == True:

            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.image = pygame.image.load('skins/player.png')
                self.image = pygame.transform.scale(self.image, (80,80))
                self.rect.x -= speed
                facing = 'left'

            if keys[pygame.K_RIGHT] and self.rect.x < 1920 - self.rect.width:
                self.image = pygame.image.load('skins/playerr.png')
                self.image = pygame.transform.scale(self.image, (80,80))
                self.rect.x += speed
                facing = 'right'

            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= speed


            if keys[pygame.K_DOWN] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += speed
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()

        self.image = pygame.image.load('skins/filename.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.live = True
    def update(self, speed):
        keys = pygame.key.get_pressed()
        if self.live == True:

            if keys[pygame.K_a] and self.rect.x > 0:
                self.image = pygame.image.load('skins/filename.png')
                self.rect.x -= speed
                self.facing = 'left'

            if keys[pygame.K_d] and self.rect.x < 1920 - self.rect.width:
                self.image = pygame.image.load('skins/filenamel.png')
                self.rect.x += speed
                self.facing = 'right'

            # Make thing go up (Jump up)
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= speed

            if keys[pygame.K_s] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += speed
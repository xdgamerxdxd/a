import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.live = True

    def update(self, speed):
        keys = pygame.key.get_pressed()
        if self.live == True:

            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= speed
                facing = 'left'

            if keys[pygame.K_RIGHT] and self.rect.x < 1920 - self.rect.width:
                self.rect.x += speed
                facing = 'right'

            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= speed


            if keys[pygame.K_DOWN] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += speed

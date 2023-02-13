import pygame
from sprites import *

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.entities()

    def entities(self):
        self.all_entities = pygame.sprite.Group()
        self.bad_boys = pygame.sprite.Group()
        self.attack = pygame.sprite.Group()
        self.player = Player(500, 100)
        self.enemy = Enemy(1000,500)
        self.atk = Attack()
        self.attack.add(self.atk)
        self.bad_boys.add(self.enemy)
        self.all_entities.add(self.player, self.enemy, self.atk)

    def run(self):
        keys = pygame.key.get_pressed()
        self.all_entities.draw(self.screen)
        if self.player.live == True:
            self.player.update(20)
            self.atk.update(self.player.facing, self.player.rect.x, self.player.rect.y)
        self.enemy.update(15)
        if pygame.sprite.spritecollideany(self.player, self.bad_boys):
            self.player.kill()
            self.player.live = False

        if pygame.sprite.spritecollideany(self.atk, self.bad_boys):
            self.enemy.kill()
            
        if keys[pygame.K_ESCAPE]:
            self.running = False
            
        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            self.entities()



def main():

    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    game = Game(screen)
    
    while game.running:
        screen.fill((14, 14, 17))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.run()

        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
main()
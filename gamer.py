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
        self.atk = pygame.sprite.Group()
        self.player = Player(500, 100)
        self.enemy = Enemy(1000,500)
        self.matk = Meele_attack()
        self.atk.add(self.matk)
        self.bad_boys.add(self.enemy)
        self.all_entities.add(self.player, self.enemy, self.matk)

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.running = False
        self.all_entities.draw(self.screen)
        self.player.update(20)
        self.enemy.update(15)
        self.matk.update()
        if pygame.sprite.spritecollideany(self.player, self.bad_boys):
            self.player.kill()
            self.player.live = False
        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            self.running = False
            main()



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
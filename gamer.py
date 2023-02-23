import pygame
from Menu import *
from sprites import *

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.entities()

    def entities(self):
        self.all_entities = pygame.sprite.Group()
        self.bad_boys = pygame.sprite.Group()
        self.eattack = pygame.sprite.Group()
        self.attack = pygame.sprite.Group()
        self.player = Player('p', 500, 860)
        self.enemy = Player('e',1000,720)
        self.atk = Attack()
        self.eatk = Attack()
        self.attack.add(self.atk)
        self.eattack.add(self.eatk)
        self.bad_boys.add(self.enemy)
        self.all_entities.add(self.player, self.enemy, self.atk, self.eatk)

    def run(self):
        keys = pygame.key.get_pressed()
        self.all_entities.draw(self.screen)
        self.player.update(20, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN )
        self.atk.update(self.player.facing, self.player.rect.x, self.player.rect.y, pygame.K_o, 'p')
        self.enemy.update(15, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        self.eatk.update(self.enemy.facing, self.enemy.rect.x, self.enemy.rect.y, pygame.K_t, 'e')

        if pygame.sprite.spritecollideany(self.player, self.bad_boys):
            self.atk.kill()
            self.player.kill()

        if pygame.sprite.spritecollideany(self.player, self.eattack) and self.eatk.atk == True:
            self.atk.kill()
            self.player.kill()

        if pygame.sprite.spritecollideany(self.enemy, self.attack) and self.atk.atk == True:
            self.enemy.kill()
            self.eatk.kill()
            
        if keys[pygame.K_ESCAPE]:
            self.menu()

        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            self.restart()

    def menu(self):
        menu = main_menu(self.screen)
        if menu.state == False:
            menu.state = True
            pygame.display.set_caption("Minecraft 'real'")
            #pygame.display.set_icon(pygame.image.load('other/a.png'))
            menu.run(self.restart)

    def restart(self):
        self.entities()

def game():

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    game = Game(screen)
    
    while game.running:
        screen.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.run()

        pygame.display.update()
        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
game()
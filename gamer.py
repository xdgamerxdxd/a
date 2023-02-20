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
        self.player.update(20, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        self.atk.update(self.player.facing, self.player.rect.x, self.player.rect.y)
        self.enemy.update(15)
        if pygame.sprite.spritecollideany(self.player, self.bad_boys):
            self.atk.kill()
            self.player.kill()

        if pygame.sprite.spritecollideany(self.enemy, self.attack) and self.atk.atk == True:
            self.enemy.kill()
            
        if keys[pygame.K_ESCAPE]:
            self.menu()

        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            self.restart()

    def menu(self):
        menu = main_menu(self.screen)
        if menu.state == False:
            menu.state = True
            pygame.display.set_caption("Minecraft 'real'")
            pygame.display.set_icon(pygame.image.load('other/a.png'))
            menu.run(self.restart)

    def restart(self):
        self.entities()

def game():

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_icon(pygame.image.load('other/b.png'))
    clock = pygame.time.Clock()

    game = Game(screen)
    
    while game.running:
        screen.fill((14, 14, 17))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.run()

        pygame.display.update()
        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
game()
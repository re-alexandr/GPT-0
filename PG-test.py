#Just for fun
import pygame
print(pygame)

WIDTH = 720  # ширина игрового окна
HEIGHT = 700 # высота игрового окна
FPS = 60 # частота кадров в секунду

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sizexy = (50, 50)

        self.image = pygame.Surface(self.sizexy)
        self.image.fill(0x000000)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.SPEEDx = 8
        self.SPPEDy = 8
        
        
    def update(self):
        keystates = pygame.key.get_pressed()
        self.rect.x += self.SPEEDx * (keystates[pygame.K_RIGHT] - keystates[pygame.K_LEFT])
        self.rect.y += self.SPPEDy * (keystates[pygame.K_DOWN] - keystates[pygame.K_UP])

        self.rect.x = self.rect.x % WIDTH
        self.rect.y = self.rect.y % HEIGHT

# создаем игру и окно
pygame.init()
#pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    #events    
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(0xffffff)
    all_sprites.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()



pygame.quit()





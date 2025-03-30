import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#Создание окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Загрузка изображения дороги
road_image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\9lab\9Racer\track.png")  
road_image = pygame.transform.scale(road_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Класс врага 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\9lab\9Racer\car.png")
        self.image = pygame.transform.scale(self.image, (50, 80))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 6  

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\9lab\9Racer\player-car.png")
        self.image = pygame.transform.scale(self.image, (50, 80))  
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.score = 0
        self.speed = 6  

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
    
    def collect_coin(self, coin_group):
        for coin in coin_group:
            if self.rect.colliderect(coin.rect):
                coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40))
                self.score += coin.value  #Добавляем очки за монету
                coin_group.remove(coin)
                coin_group.add(Coin())  #Создаём новую монету

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
#Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #20% шанс появления редкой монеты (3 очка), иначе обычная (1 очко)
        if random.random() < 0.2:
            self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\9lab\9Racer\coin.png")  # Редкая монета
            self.value = 3
        else:
            self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\9lab\9Racer\min-coin.png")  # Обычная монета
            self.value = 1
        self.image = pygame.transform.scale(self.image, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40))
        self.speed = 3  

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Создание игрока и групп спрайтов
P1 = Player()
enemies = pygame.sprite.Group()
enemies.add(Enemy())
coins = pygame.sprite.Group()
for _ in range(5):  
    coins.add(Coin())

#Основной игровой цикл
while True:
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #Обновление игрока и объектов
    P1.update()
    for enemy in enemies:
        enemy.move()
    for coin in coins:
        coin.move()
    P1.collect_coin(coins)
    
    #Увеличение скорости врагов при очков
    if P1.score >= 10:
        for enemy in enemies:
            enemy.speed = 8
    if P1.score >= 20:
        for enemy in enemies:
            enemy.speed = 10
    
    #Отрисовка объектов
    DISPLAYSURF.blit(road_image, (0, 0))  
    P1.draw(DISPLAYSURF)
    for enemy in enemies:
        enemy.draw(DISPLAYSURF)
    for coin in coins:
        coin.draw(DISPLAYSURF)
    
    #Отображение счета
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {P1.score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 120, 10))
    
    #Проверка столкновения с врагом
    for enemy in enemies:
        if P1.rect.colliderect(enemy.rect):
            DISPLAYSURF.fill(RED)  
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("GAME OVER", True, BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            DISPLAYSURF.blit(game_over_text, text_rect)
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
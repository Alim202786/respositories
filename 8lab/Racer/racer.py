import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen info
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Load and scale the road image
road_image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\8lab\Racer\track.png")  # Replace with actual filename
road_image = pygame.transform.scale(road_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\8lab\Racer\car.png")
        self.image = pygame.transform.scale(self.image, (50, 80))  # Resize enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 6  # Start at 50% of player speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\8lab\Racer\player-car.png")
        self.image = pygame.transform.scale(self.image, (50, 80))  # Resize player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.score = 0
        self.speed = 8  # Player speed

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
                self.score += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Алим\OneDrive\Desktop\python\8lab\Racer\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 100))
        self.speed = 3  # Speed of falling coins

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initialize player, enemies, and coins
P1 = Player()
enemies = pygame.sprite.Group()
enemies.add(Enemy())
coins = pygame.sprite.Group()
for _ in range(5):  # Create multiple coins
    coins.add(Coin())

# Game loop
while True:
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    P1.update()
    for enemy in enemies:
        enemy.move()
    for coin in coins:
        coin.move()
    P1.collect_coin(coins)
    
    # Increase number of enemies at score thresholds
    if P1.score == 50 and len(enemies) == 1:
        enemies.add(Enemy())
    if P1.score == 150 and len(enemies) == 2:
        enemies.add(Enemy())
    
    DISPLAYSURF.blit(road_image, (0, 0))  # Draw road background
    P1.draw(DISPLAYSURF)
    for enemy in enemies:
        enemy.draw(DISPLAYSURF)
    for coin in coins:
        coin.draw(DISPLAYSURF)
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {P1.score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 120, 10))
    
    # Check collision with enemy
    for enemy in enemies:
        if P1.rect.colliderect(enemy.rect):
            DISPLAYSURF.fill(RED)  # Red background
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
import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20  # Размер ячейки змеи и еды
SPEED = 10  # Начальная скорость

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

# Шрифт
font = pygame.font.Font(None, 36)

# Функция отображения текста
def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = "RIGHT"
        self.grow = False
        self.speed = SPEED

    def move(self):
        x, y = self.body[0]

        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE

        new_head = (x, y)

        # Проверка на выход за границы
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            return False

        # Проверка на столкновение с самой собой
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False  # Сброс флага роста

        return True

    def change_direction(self, direction):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposite.get(self.direction, ""):
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Класс еды
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return x, y

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
def game():
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        # Движение змеи
        if not snake.move():
            break  # Конец игры, если змея столкнулась со стеной или собой

        # Проверка, съела ли змея еду
        if snake.body[0] == food.position:
            snake.grow = True
            score += 1
            food = Food(snake.body)

            # Повышение уровня каждые 3 еды
            if score % 3 == 0:
                level += 1
                snake.speed += 2  # Увеличение скорости

        # Отрисовка объектов
        snake.draw()
        food.draw()

        # Отображение счета и уровня
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", 10, 40)

        pygame.display.update()
        clock.tick(snake.speed)

    pygame.quit()

# Запуск игры
game()

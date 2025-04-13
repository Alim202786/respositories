import pygame
import random
import time
import psycopg2
from datetime import datetime

def connect():
    return psycopg2.connect(
        dbname="postgres",        
        user="postgres",          
        password="alim_788607131523",  
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def get_user_level(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1;", (user_id,))
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result[0] if result else 1

def save_game_state(user_id, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);",
        (user_id, score, level)
    )

    conn.commit()
    cur.close()
    conn.close()

create_tables()
username = input("Введите ваше имя пользователя: ")
user_id = get_or_create_user(username)
level = get_user_level(user_id)

print(f"Добро пожаловать, {username}! Ваш текущий уровень: {level}")

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = "RIGHT"
        self.grow = False
        self.speed = 10 + (level - 1) * 2  

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP": y -= CELL_SIZE
        elif self.direction == "DOWN": y += CELL_SIZE
        elif self.direction == "LEFT": x -= CELL_SIZE
        elif self.direction == "RIGHT": x += CELL_SIZE
        new_head = (x, y)

        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            return False
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, direction):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposite.get(self.direction, ""):
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.type = random.choice(["regular", "bonus"])
        self.position = self.generate_position(snake_body)
        self.weight = 1 if self.type == "regular" else 3
        self.color = RED if self.type == "regular" else BLUE
        self.spawn_time = time.time() if self.type == "bonus" else None

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return x, y

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

def game():
    global level
    snake = Snake()
    food = Food(snake.body)
    score = 0

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake.change_direction("UP")
                elif event.key == pygame.K_DOWN: snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT: snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT: snake.change_direction("RIGHT")

        if not snake.move():
            break

        if snake.body[0] == food.position:
            snake.grow = True
            score += food.weight
            food = Food(snake.body)
            if score % 5 == 0:
                level += 1
                snake.speed += 2

        if food.type == "bonus" and time.time() - food.spawn_time > 8:
            food = Food(snake.body)

        snake.draw()
        food.draw()
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", 10, 40)
        pygame.display.update()
        clock.tick(snake.speed)

    pygame.quit()
    save_game_state(user_id, score, level)
    print(f"Игра окончена. Очки: {score}, Уровень: {level} сохранены.")

game()
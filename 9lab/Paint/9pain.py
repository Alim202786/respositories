import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))  
clock = pygame.time.Clock()  
radius = 15  #Радиус кисти
mode = 'blue'  #Начальный цвет кисти
points = []  #Список точек для рисования
shapes = []  #Список нарисованных фигур

drawing_shape = None  #Переменная для хранения текущей формы
start_pos = None  #Начальная позиция для фигур

#Определение доступных цветов
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}
current_color = colors['blue']  #Установка начального цвета кисти

#Функция для рисования линии между двумя точками
def drawLineBetween(screen, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)

#Функции для рисования различных фигур
def draw_triangle(screen, color, start_pos, size):
    x, y = start_pos
    points = [(x, y), (x + size, y + size), (x, y + size)]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(screen, color, start_pos, size):
    x, y = start_pos
    height = (math.sqrt(3) / 2) * size  #Вычисление высоты треугольника
    points = [(x, y), (x + size, y), (x + size / 2, y - height)]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(screen, color, start_pos, size):
    x, y = start_pos
    points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
    pygame.draw.polygon(screen, color, points)

def main():
    global mode, radius, drawing_shape, start_pos, current_color, points
    
    while True:
        screen.fill((0, 0, 0))  #Очистка экрана
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                #Изменение цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                    current_color = colors['red']
                elif event.key == pygame.K_g:
                    mode = 'green'
                    current_color = colors['green']
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    current_color = colors['blue']
                elif event.key == pygame.K_w:
                    current_color = colors['white']
                elif event.key == pygame.K_k:
                    current_color = colors['black']
                
                #Выбор фигуры для рисования
                elif event.key == pygame.K_e:
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_c:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_t:
                    drawing_shape = 'rect'
                elif event.key == pygame.K_s:
                    drawing_shape = 'square'
                elif event.key == pygame.K_y:
                    drawing_shape = 'triangle'
                elif event.key == pygame.K_q:
                    drawing_shape = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    drawing_shape = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos  #Запоминаем начальную точку
                if event.button == 1:  #Левая кнопка мыши
                    if drawing_shape == 'eraser':
                        shapes.append(('eraser', start_pos, radius))
                    elif drawing_shape == 'circle':
                        shapes.append(('circle', start_pos, radius, current_color))
                    elif drawing_shape == 'rect':
                        shapes.append(('rect', start_pos, (50, 50), current_color))
                    elif drawing_shape == 'triangle':
                        shapes.append(('triangle', start_pos, 50, current_color))
                    elif drawing_shape == 'equilateral_triangle':
                        shapes.append(('equilateral_triangle', start_pos, 50, current_color))
                    elif drawing_shape == 'rhombus':
                        shapes.append(('rhombus', start_pos, 40, current_color))
                elif event.button == 3:  #Правая кнопка мыши уменьшает радиус кисти
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if pygame.mouse.get_pressed()[0]:
                    if drawing_shape == 'eraser':
                        shapes.append(('eraser', position, radius))
                    else:
                        points.append((position, current_color))
                        points = points[-256:]  #Ограничение на 256 точек
        
        #Отрисовка всех сохраненных фигур
        for shape in shapes:
            if shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'rect':
                pygame.draw.rect(screen, shape[3], (*shape[1], *shape[2]))
            elif shape[0] == 'triangle':
                draw_triangle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'equilateral_triangle':
                draw_equilateral_triangle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'rhombus':
                draw_rhombus(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'eraser':
                pygame.draw.circle(screen, colors['black'], shape[1], shape[2])
        
        #Удаление точек, попавших под ластик
        new_points = []
        for pos, color in points:
            erased = False
            for shape in shapes:
                if shape[0] == 'eraser' and pygame.math.Vector2(pos).distance_to(shape[1]) < shape[2]:
                    erased = True
                    break
            if not erased:
                new_points.append((pos, color))
        points = new_points
        
        #Рисование линий между точками
        for i in range(1, len(points)):
            drawLineBetween(screen, points[i-1][0], points[i][0], radius, points[i][1])
        
        pygame.display.flip()  
        clock.tick(60)  

main()
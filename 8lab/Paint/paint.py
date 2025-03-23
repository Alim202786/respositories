import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
radius = 15
mode = 'blue'
points = []
drawing_shape = None
start_pos = None
shapes = []

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}
current_color = colors['blue']

def drawLineBetween(screen, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)

def main():
    global mode, radius, drawing_shape, start_pos, current_color, points
    
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                    current_color = colors['red']
                elif event.key == pygame.K_g:
                    mode = 'green'
                    current_color = colors['green']
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    current_color = colors['blue']
                elif event.key == pygame.K_e:
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_c:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_t:
                    drawing_shape = 'rect'
                elif event.key == pygame.K_w:
                    current_color = colors['white']
                elif event.key == pygame.K_k:
                    current_color = colors['black']
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                if event.button == 1:
                    if drawing_shape == 'eraser':
                        shapes.append(('eraser', start_pos, radius))
                    elif drawing_shape == 'circle':
                        shapes.append(('circle', start_pos, radius, current_color))
                    elif drawing_shape == 'rect':
                        shapes.append(('rect', start_pos, (50, 50), current_color))
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if pygame.mouse.get_pressed()[0]:
                    if drawing_shape == 'eraser':
                        shapes.append(('eraser', position, radius))
                    else:
                        points.append((position, current_color))
                        points = points[-256:]
        
        for shape in shapes:
            if shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'rect':
                pygame.draw.rect(screen, shape[3], (*shape[1], *shape[2]))
            elif shape[0] == 'eraser':
                pygame.draw.circle(screen, colors['black'], shape[1], shape[2])
        
        new_points = []
        for pos, color in points:
            erased = False
            for shape in shapes:
                if shape[0] == 'eraser':
                    if pygame.math.Vector2(pos).distance_to(shape[1]) < shape[2]:
                        erased = True
                        break
            if not erased:
                new_points.append((pos, color))
        points = new_points
        
        for i in range(1, len(points)):
            drawLineBetween(screen, points[i-1][0], points[i][0], radius, points[i][1])
        
        pygame.display.flip()
        clock.tick(60)

main()
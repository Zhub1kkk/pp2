import pygame

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
STEP = 20

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Начальные координаты шара (центр экрана)
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
x = 800
y = 600

running = True
while running:
    # 1. Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Нажатие клавиш
        
            
    press = pygame.key.get_pressed()
    if press[pygame.K_UP]:
        ball_y -= 10
    if press[pygame.K_DOWN]:
        ball_y += 10
    if press[pygame.K_RIGHT]:
        ball_x += 10
    if press[pygame.K_LEFT]:
        ball_x -= 10

    # 2. Отрисовка
    screen.fill(WHITE) # Очищаем экран белым цветом
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS) # Рисуем шар
    
    pygame.display.flip() # Обновляем экран
    clock.tick(45)

pygame.quit()
import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Размеры окна
window_size = ((800, 600))
CELL_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((window_size))
pygame.display.set_caption("Pac-Man")

# Создание таймера
clock = pygame.time.Clock()

# Определение лабиринта (1 - стена, 0 - проход)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Позиция игрока
player_pos = [1, 1]

# Список точек
points = []

# Создание точек в лабиринте
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 0:
            points.append((x, y))

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_pos = [player_pos[0] - 1, player_pos[1]]
            elif event.key == pygame.K_RIGHT:
                new_pos = [player_pos[0] + 1, player_pos[1]]
            elif event.key == pygame.K_UP:
                new_pos = [player_pos[0], player_pos[1] - 1]
            elif event.key == pygame.K_DOWN:
                new_pos = [player_pos[0], player_pos[1] + 1]
            else:
                new_pos = player_pos

            if maze[new_pos[1]][new_pos[0]] == 0:
                player_pos = new_pos

    # Проверка на съедание точки
    if tuple(player_pos) in points:
        points.remove(tuple(player_pos))

    # Очистка экрана
    screen.fill(BLACK)

    # Рисуем лабиринт
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Рисуем точки
    for point in points:
        pygame.draw.circle(screen, WHITE, (point[0] * CELL_SIZE + CELL_SIZE // 2, point[1] * CELL_SIZE + CELL_SIZE // 2), 3)

    # Рисуем игрока
    pygame.draw.circle(screen, YELLOW, (player_pos[0] * CELL_SIZE + CELL_SIZE // 2, player_pos[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

    # Обновляем экран
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(10)

# Завершение Pygame
pygame.quit()

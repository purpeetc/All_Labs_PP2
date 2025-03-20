import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400  # Ширина и высота окна отображения
CELL_SIZE = 20  # Размер ячейки (еда)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Snake Game")  # Название окна

WHITE = (255, 255, 255)  # Белый цвет фона
GREEN = (0, 255, 0)      # Зелёный цвет змейки
RED = (255, 0, 0)        # Красный цвет еды
BLACK = (0, 0, 0)        # Цвет индикатора (чёрный)

snake = [(100, 100)]  # Начальное положение змейки (список координат)
snake_dir = (CELL_SIZE, 0)  # Начальное направление движения змейки
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # Случайное положение еды
food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])  # Случайный размер еды
food_timer = 100  # Таймер исчезновения еды
score = 0  # Счёт игрока
level = 1  # Уровень игрока
speed = 10  # Скорость игры (количество кадров в секунду)

running = True
clock = pygame.time.Clock()  # Объект для контроля FPS

while running:
    screen.fill(WHITE)  # Заливка экрана белым цветом
    
    # Обработка событий (например, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажимает кнопку закрытия окна
            running = False
            
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):  # Если нажата клавиша вверх и змейка не движется вниз
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):  # Если нажата клавиша вниз и змейка не движется вверх
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):  # Если нажата клавиша влево и змейка не движется вправо
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):  # Если нажата клавиша вправо и змейка не движется влево
                snake_dir = (CELL_SIZE, 0)
    
    # Вычисление новой головы змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Если новая голова выходит за границы экрана или сталкивается с телом змейки, игра заканчивается
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
        break
    
    snake.insert(0, new_head)  # Добавляем новую голову в начало списка координат змейки
    
    # Если змейка "съела" еду (пересечение прямоугольников)
    if new_head[0] < food[0] + food_size and new_head[0] + CELL_SIZE > food[0] and \
       new_head[1] < food[1] + food_size and new_head[1] + CELL_SIZE > food[1]:
        score += food_size // CELL_SIZE  # Добавление очков в зависимости от размера еды
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # Новая позиция еды
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])  # Новый случайный размер еды
        food_timer = 100  # Сброс таймера еды
        if score % 4 == 0:  # Если счёт кратен 4, увеличиваем уровень и скорость
            level += 1
            speed += 2
    else:
        snake.pop()  # Если еда не собрана, убираем последний элемент змейки (движение без роста)
    
    food_timer -= 1  # Уменьшаем таймер еды
    if food_timer <= 0:  # Если таймер истёк, создаём новую еду
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100
    
    # Отрисовка еды (прямоугольник)
    pygame.draw.rect(screen, RED, (food[0], food[1], food_size, food_size))
    
    # Отрисовка змейки (каждая часть змейки — прямоугольник)
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))
    
    # Отрисовка текста с результатами (счёт и уровень)
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.update()  # Обновление экрана
    clock.tick(speed)  # Задержка для достижения нужной скорости

pygame.quit()  # Завершение работы PyGame

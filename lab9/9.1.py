import pygame
import random
pygame.init()  # Инициализация PyGame

WIDTH, HEIGHT = 800, 600  # Ширина и высота окна отображения
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Racer Game")  # Название окна

WHITE = (255, 255, 255)  # Цвет фона (белый)
GREEN = (0, 200, 0)      # Цвет моей машины (зелёный)
RED = (200, 0, 0)        # Цвет машины противника (красный)
GOLD = (255, 215, 0)     # Цвет маленькой монеты (золотой)
BIG_GOLD = (255, 223, 0) # Цвет большой монеты

clock = pygame.time.Clock()  # Объект для контроля FPS
FPS = 60  # Количество кадров в секунду

car_width, car_height = 50, 80  # Параметры (ширина и высота) моей машины
car_x, car_y = WIDTH // 2, HEIGHT - car_height - 20  # Начальные координаты моей машины
car_speed = 5  # Скорость движения моей машины

# Параметры машины противника
enemy_width, enemy_height = 50, 80  # Параметры (ширина и высота) машины противника
enemy_x = random.randint(100, WIDTH - 100)  # Начальная позиция по оси X для машины противника
enemy_y = -enemy_height  # Начальная позиция по оси Y для машины противника (выход сверху)
enemy_speed = 3  # Скорость машины противника

# Параметры монет
coin_width, coin_height = 30, 30  # Ширина и высота маленькой монеты
big_coin_width, big_coin_height = 50, 50  # Ширина и высота большой монеты
coin_x = random.randint(100, WIDTH - 100)  # Начальная позиция маленькой монеты по оси X
coin_y = -coin_height  # Начальная позиция маленькой монеты по оси Y (выход сверху)
big_coin_x = random.randint(100, WIDTH - 100)  # Начальная позиция большой монеты по оси X
big_coin_y = -big_coin_height  # Начальная позиция большой монеты по оси Y (выход сверху)
coin_speed = 3  # Скорость маленькой монеты
big_coin_speed = 3  # Скорость большой монеты
coin_value = random.randint(1, 5)  # Случайное значение маленькой монеты
big_coin_value = 10  # Значение большой монеты

# Индикаторы игры
score = 0  # Счёт
level = 1  # Уровень

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)  # Заполнение фона белым цветом
    
    # Обработка событий (например, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажал на кнопку закрытия окна
            running = False
    
    keys = pygame.key.get_pressed()  # Получение состояния клавиш (для длительного нажатия)
    if keys[pygame.K_LEFT] and car_x > 0:  # Если нажата стрелка влево и машина не у края экрана
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:  # Если нажата стрелка вправо и машина не у края экрана
        car_x += car_speed
    
    # Действия машины противника
    enemy_y += enemy_speed  # Движение машины противника вниз
    if enemy_y > HEIGHT:  # Если машина противника уехала за нижнюю границу экрана
        enemy_y = -enemy_height  # Сброс позиции по оси Y (выход сверху)
        enemy_x = random.randint(100, WIDTH - 100)  # Новая случайная позиция по оси X
    
    # Действия маленькой монеты
    coin_y += coin_speed  # Движение монеты вниз
    if coin_y > HEIGHT:  # Если монета ушла за нижнюю границу экрана
        coin_y = -coin_height  # Сброс позиции монеты по оси Y
        coin_x = random.randint(100, WIDTH - 100)  # Новая случайная позиция по оси X
        coin_value = random.randint(1, 5)  # Новое случайное значение монеты
    
    # Действия большой монеты
    big_coin_y += big_coin_speed  # Движение большой монеты вниз
    if big_coin_y > HEIGHT:  # Если большая монета ушла за нижнюю границу экрана
        big_coin_y = -big_coin_height  # Сброс позиции большой монеты по оси Y
        big_coin_x = random.randint(100, WIDTH - 100)  # Новая случайная позиция по оси X
    
    # Сбор маленькой монеты (проверка пересечения прямоугольников)
    if (car_x < coin_x + coin_width and car_x + car_width > coin_x and
            car_y < coin_y + coin_height and car_y + car_height > coin_y):
        score += coin_value  # Добавление очков за сбор монеты
        coin_y = -coin_height  # Сброс позиции монеты по оси Y
        coin_x = random.randint(100, WIDTH - 100)  # Новая случайная позиция по оси X
    
    # Сбор большой монеты (проверка пересечения прямоугольников)
    if (car_x < big_coin_x + big_coin_width and car_x + car_width > big_coin_x and
            car_y < big_coin_y + big_coin_height and car_y + car_height > big_coin_y):
        score += big_coin_value  # Добавление очков за сбор большой монеты
        big_coin_y = -big_coin_height  # Сброс позиции большой монеты по оси Y
        big_coin_x = random.randint(100, WIDTH - 100)  # Новая случайная позиция по оси X
    
    # Если моя машина сталкивается с машиной противника, игра заканчивается
    if (car_x < enemy_x + enemy_width and car_x + car_width > enemy_x and
            car_y < enemy_y + enemy_height and car_y + car_height > enemy_y):
        running = False
    
    # Если очки превышают уровень, увеличиваем сложность (скорость противника)
    if score >= level * 10:
        level += 1
        enemy_speed += 1
    
    # Отрисовка моей машины (прямоугольник)
    pygame.draw.rect(screen, GREEN, (car_x, car_y, car_width, car_height))
    
    # Отрисовка машины противника (прямоугольник)
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    
    # Отрисовка маленькой монеты (круг)
    pygame.draw.circle(screen, GOLD, (coin_x + coin_width // 2, coin_y + coin_height // 2), coin_width // 2)
    
    # Отрисовка большой монеты (круг)
    pygame.draw.circle(screen, BIG_GOLD, (big_coin_x + big_coin_width // 2, big_coin_y + big_coin_height // 2), big_coin_width // 2)
    
    # Вывод результатов игры на экран (очки и уровень)
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()  # Обновление экрана
    clock.tick(FPS)  # Задержка для достижения нужного FPS

pygame.quit()  # Завершение работы PyGame

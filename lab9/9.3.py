import pygame
import random

pygame.init()  # Инициализация PyGame

WIDTH, HEIGHT = 800, 600  # Ширина и высота окна отображения
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Random Shapes")  # Название окна

WHITE = (255, 255, 255)  # Цвет фона окна
BLACK = (0, 0, 0)        # Цвет круга
YELLOW = (255, 255, 0)   # Цвет прямоугольника
BLUE = (0, 0, 255)       # Цвет треугольника
RED = (255, 0, 0)        # Цвет ромба
BROWN = (100, 40, 0)     # Цвет квадрата

shapes = []  # Список фигур

def random_position():
    # Случайные координаты в пределах экрана с отступом 50 пикселей от краёв
    return random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

running = True
while running:
    screen.fill(WHITE)  # Заполнение экрана белым цветом

    # Отрисовка всех фигур из списка shapes
    for shape_type, color, x, y in shapes:
        if shape_type == "circle":
            pygame.draw.circle(screen, color, (x, y), 25)  # Рисуем круг с радиусом 25

        elif shape_type == "rectangle":
            pygame.draw.rect(screen, color, (x, y, 100, 50))  # Рисуем прямоугольник шириной 100 и высотой 50

        elif shape_type == "triangle":
            # Рисуем треугольник по трём точкам
            pygame.draw.polygon(screen, color, [(x, y), (x - 50, y + 100), (x + 50, y + 100)])

        elif shape_type == "rhombus":
            # Рисуем ромб по четырём точкам
            pygame.draw.polygon(screen, color, [(x, y), (x + 50, y + 50), (x, y + 100), (x - 50, y + 50)])

        elif shape_type == "square":
            pygame.draw.rect(screen, color, (x, y, 50, 50))  # Рисуем квадрат размером 50x50

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажимает кнопку закрытия окна
            running = False  # Программа завершится

        elif event.type == pygame.KEYDOWN:
            x, y = random_position()  # Генерация случайных координат

            if event.key == pygame.K_q:  # Если нажата клавиша Q, добавляем чёрный круг
                shapes.append(("circle", BLACK, x, y))

            elif event.key == pygame.K_w:  # Если нажата клавиша W, добавляем жёлтый прямоугольник
                shapes.append(("rectangle", YELLOW, x, y))

            elif event.key == pygame.K_e:  # Если нажата клавиша E, добавляем синий треугольник
                shapes.append(("triangle", BLUE, x, y))

            elif event.key == pygame.K_r:  # Если нажата клавиша R, добавляем красный ромб
                shapes.append(("rhombus", RED, x, y))

            elif event.key == pygame.K_t:  # Если нажата клавиша T, добавляем квадрат (коричневый)
                shapes.append(("square", BROWN, x, y))

    pygame.display.update()  # Обновление экрана

pygame.quit()  # Завершение работы PyGame

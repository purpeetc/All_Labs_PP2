import pygame
import random

pygame.init()

# Экран параметрлерін енгізу. 
WIDTH, HEIGHT = 500, 700 # Экраннің өлшемдері
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Экраннің өлшемдерін көрсету
pygame.display.set_caption("Car Game") # Экраннің атауы

car_img = pygame.image.load(r"/Users/aliakimbaj/Downloads/car.png") # Машина суретін жүктеу
coin_img = pygame.image.load(r"/Users/aliakimbaj/Downloads/coin.png") # Монета суретін жүктеу
road_img = pygame.image.load(r"/Users/aliakimbaj/Downloads/road.jpg") # Жол суретін жүктеу

car_width, car_height = 70, 140 # Машина өлшемі
coin_width, coin_height = 40, 40 # Монета өлшемі

car_img = pygame.transform.scale(car_img, (car_width, car_height))#масштабироваание на 70\140 пикселей
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Ойын объектілері
car_x = WIDTH // 2 - car_width // 2 # центрде по горизонтали
car_y = HEIGHT - car_height - 20 # внизу в центре кышкене отсуппен
car_speed = 5

coin_x = random.randint(50, WIDTH - 50) # случайное место по оси х
coin_y = -50 # Начальная позиция монеты (за экраном сверху)
coin_speed = 10

score = 0
font = pygame.font.Font(None, 36) # Шрифт для отображения счета
clock = pygame.time.Clock()

running = True
while running:
    screen.blit(road_img, (0, 0)) #Каждый кадр сначала заливается изображением дороги, затем отрисовываются машина и монета.
    screen.blit(car_img, (car_x, car_y))
    screen.blit(coin_img, (coin_x, coin_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()#возвращает список всех нажатых клавиш.
    if keys[pygame.K_LEFT] and car_x > 10:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
        car_x += car_speed
    # if keys[pygame.K_UP] and car_y > 0:  # Алға қозғалту мүмкіндігі
    #     car_y -= car_speed
    # if keys[pygame.K_DOWN] and car_y < HEIGHT - car_height:
    #     car_y += car_speed

    # Монета қозғалысы
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50 # Если монета вышла за нижнюю границу экрана Сбрасываем позицию монеты наверх
        coin_x = random.randint(50, WIDTH - 50)
    
    if (car_x < coin_x < car_x + car_width or car_x < coin_x + coin_width < car_x + car_width) and \
       (car_y < coin_y < car_y + car_height or car_y < coin_y + coin_height < car_y + car_height):
        score += 1 #находится ли монета внутри области машины.Условия используют координаты машины и монеты, а также их размеры.
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)
    
    # Ұпай көрсету
    text = font.render(f"Score: {score}", True, (255, 255, 255)) #изображение текста, где отображается текущий счет, white
    screen.blit(text, (10, 10)) #отображается в верх\левом углу
    
    pygame.display.update()
    clock.tick(30) #кадры в сек

pygame.quit()

import pygame
import datetime 

pygame.init()
WIDTH, HEIGHT = 1100, 920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's clock")

clock_img = pygame.image.load(r"/Users/aliakimbaj/Downloads/clock.png")
clock_face = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))#изображение масштабируется до размеров окна
hand_right = pygame.image.load(r"/Users/aliakimbaj/Downloads/rightarm.png")#minuty
hand_left = pygame.image.load(r"/Users/aliakimbaj/Downloads/leftarm.png")#secundy
leftArmSecondImage = pygame.transform.scale(hand_left, (20, hand_left.get_height() // 2.5-30))
RightArmSecondImage = pygame.transform.scale(hand_right, (hand_left.get_width() // 3, hand_left.get_height() // 3))


WHITE = (255, 255, 255)
clock = pygame.time.Clock()
running = True 

while running: 
    screen.fill(WHITE)
    screen.blit(clock_face, (0, 0))
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    minute_angle = - (minutes * 6)  #за каждую минуту стрелка смещается на 6 градусов
    second_angle = - (seconds * 6)   
    
    rotated_right_hand = pygame.transform.rotate(hand_right, minute_angle)#поворачивает изображения на вычисленный угол.
    rotated_left_hand = pygame.transform.rotate(hand_left, second_angle)
    
    rh_rect = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))#устанавливает центр изображения (вращённой стрелки)
    lh_rect = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    screen.blit(rotated_right_hand, rh_rect.topleft)#изображения стрелок накладываются на циферблат.
    screen.blit(rotated_left_hand, lh_rect.topleft)
    
    pygame.display.update()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
    clock.tick(60)#ограничивает количество кадров до 60 в секунду

pygame.quit()
import pygame
pygame.init()
screen = pygame.display.set_mode((1163, 535))

isDone = True
index = 0
sounds = [
    r"/Users/aliakimbaj/Downloads/Travis Scott - HIGHEST IN THE ROOM (feat. Duke, Jones).mp3",
    r"/Users/aliakimbaj/Downloads/Playboi Carti - magnolia.mp3",
    r"/Users/aliakimbaj/Downloads/Sergio Mendes - Mas Que Nada (2011 Rio Version).mp3"
]

color = (131, 1, 0)

isPaused = False
isPlayed = True
while isDone:
    screen.fill(color)
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isDone = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if index == len(sounds) - 1:
                index = 0
            else:
                index += 1
            isPaused = False
            isPlayed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if index == 0:
                index = len(sounds) - 1
            else:
                index -= 1
            isPaused = False
            isPlayed = True

        if event.type == pygame.KEYDOWN and isPlayed:#Если нажата любая клавиша (и условие isPlayed истинно)
            if isPaused:                    
                pygame.mixer.music.unpause()
                isPaused = not isPaused
            else:
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play(2)
            isPlayed = not isPlayed #(isPlayed == True)-готов к воспроизведению, 
                                    #isPlayed меняется на противоположное значение (то есть становится False), чтобы показать, что команда на воспроизведение уже выполнена и не нужно повторно запускать ту же операцию

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed = not isPlayed
            isPaused = not isPaused

    pygame.display.flip()
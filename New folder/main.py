import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600
screen=pygame.display.set_mode([WIDTH,HEIGHT])

image1=pygame.image.load("image1.jpg")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))

image2=pygame.image.load("image2.jpg")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("white")
    screen.blit(image1,(0,0))
    font = pygame.font.SysFont("Times New Roman", 50)


    pygame.display.update()
    time.sleep(3)

    font = pygame.font.SysFont("Times New Roman", 50)


    screen.blit(image2,(0,0))

    pygame.display.update()
    time.sleep(3)
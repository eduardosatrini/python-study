# DON'T WORKING

import pygame

pygame.init()
pygame.mixer.music.load("mozart-requiem.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)

clock = pygame.time.Clock()
clock.tick(10)

while pygame.mixer.music.get_busy():
    pygame.event.pool()
    clock.tick(10)
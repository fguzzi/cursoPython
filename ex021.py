import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('blues.mp3')
pygame.mixer.music.play()
pygame.event.wait()

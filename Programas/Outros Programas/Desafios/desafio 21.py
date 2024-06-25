import pygame
pygame.init()
pygame.mixer.music.load('Someone You Loved (128 kbps).mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
'''entre no sistema um arquivo mp3 e saia com sua reprodução'''
import pygame

# file = 'guns_n_roses_as_melhores.mp3'
'''linha para carregar arquivo mp3'''
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

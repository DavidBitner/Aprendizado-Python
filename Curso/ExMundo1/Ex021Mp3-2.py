import pygame

mp3 = str(input('Digite o caminho do mp3: '))
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('{}'.format(mp3))
pygame.mixer.music.play()
input('Aperte uma tecla para parar')

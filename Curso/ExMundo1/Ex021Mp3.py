import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('C:/Users/David/Music/Musicas/Curtains/Feint - The Things Weve Seen.mp3')
pygame.mixer.music.play()

input('Aperte uma tecla para parar')

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('C:/Users/David/Music/Musicas/Curtains/Feint - The Things Weve Seen.mp3')
pygame.mixer.music.play()
while True:
    a = int(input())
    if a == 1:
        pygame.mixer.music.stop()
        break

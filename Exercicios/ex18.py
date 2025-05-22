import pygame 

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r'C:\Users\gusta\OneDrive\Documentos\Python\Python\Exercicios\videoplayback.mp3')
pygame.mixer.music.play()

input('Presione enter para encerrar')

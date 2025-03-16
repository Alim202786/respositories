import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер")

paused = False
done = False

music_list = [
    r"C:\Users\Алим\OneDrive\Desktop\python\7lab\Ex\2Exer\dota-2-main.mp3",
    r"C:\Users\Алим\OneDrive\Desktop\python\7lab\Ex\2Exer\cs-go-main.mp3",
    r"C:\Users\Алим\OneDrive\Desktop\python\7lab\Ex\2Exer\gta-sa-main.mp3",
    r"C:\Users\Алим\OneDrive\Desktop\python\7lab\Ex\2Exer\mario-main.mp3"
]

current_track = 0  

def play_music():
    pygame.mixer.music.load(music_list[current_track])
    pygame.mixer.music.play()

play_music()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == pygame.K_RIGHT:  
                current_track = (current_track + 1) % len(music_list)
                play_music()

            elif event.key == pygame.K_LEFT:  
                current_track = (current_track - 1) % len(music_list)
                play_music()

    pygame.display.update()

pygame.quit()
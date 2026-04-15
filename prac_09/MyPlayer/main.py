import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

import os

# Получаем путь к папке, где лежит этот скрипт (main.py)
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

playlist = [
    os.path.join(BASE_PATH, "music", "song1.mp3"),
    os.path.join(BASE_PATH, "music", "song2.mp3"),
    os.path.join(BASE_PATH, "music", "song3.mp3")
]

current_track = 0
running = True


def play_current():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()


while running:
    screen.fill((255, 255, 255))

    title = font.render("Music Player", True, (0, 0, 0))
    screen.blit(title, (220, 50))

    song_name = os.path.basename(playlist[current_track])
    song_text = small_font.render(f"Current: {song_name}", True, (0, 0, 0))
    screen.blit(song_text, (220, 140))

    controls = [
        "P - Play",
        "S - Stop",
        "N - Next",
        "B - Previous",
        "Q - Quit"
    ]

    y = 220
    for text in controls:
        rendered = small_font.render(text, True, (0, 0, 0))
        screen.blit(rendered, (260, y))
        y += 30

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_current()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_current()

            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(playlist)
                play_current()

            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
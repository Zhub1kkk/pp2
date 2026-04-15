import pygame
import sys
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

#kartinka
image = pygame.image.load("prac_09/clock/images/mickeyclock.jpeg")
image = pygame.transform.scale(image, (700, 700))

center = (WIDTH // 2, HEIGHT // 2)


pivot = center


def draw_hand(angle, length, width):
    radians = math.radians(angle - 90)
    end_x = pivot[0] + length * math.cos(radians)
    end_y = pivot[1] + length * math.sin(radians)
    pygame.draw.line(screen, (0, 0, 0), pivot, (end_x, end_y), width)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(image, (50, 50))

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    #ang
    minute_angle = minute * 6
    second_angle = second * 6

    #draw
    draw_hand(minute_angle, 180, 8)
    draw_hand(second_angle, 220, 4)

    pygame.display.flip()
    clock.tick(1)
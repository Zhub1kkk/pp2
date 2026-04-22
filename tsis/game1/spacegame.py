import pygame , controls
from gun import Gun
from pygame.sprite import Group


def run():
    
    pygame.init
    screen = pygame.display.set_mode((800 ,600))
    pygame.display.set_caption("GALAXY WAR")
    bg_color = (0 ,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos  = Group()
    controls.create_army(screen , inos)


    while True:
        controls.events(screen ,gun , bullets )
        gun.update_gun()
        controls.update_bullets(bullets)
        controls.update(bg_color , screen ,gun , inos, bullets)
        

run()
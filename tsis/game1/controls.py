import pygame , sys
from bullet import Bullet
from ino import Ino

def events(screen ,gun ,bullets):
    """обработка событий"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_d:
                      gun.mright = True
                      """вправо"""
                 elif event.key == pygame.K_a:
                      gun.mleft = True
                      """влево""" 
                 elif event.key == pygame.K_SPACE:
                      new_bullet = Bullet(screen , gun)
                      bullets.add(new_bullet)  
            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_d:
                      gun.mright = False
                      """вправо"""
            
                 elif event.key == pygame.K_a:
                      gun.mleft = False
                      """влево"""
def update(bg_color , screen , gun, inos , bullets):
     """обновление экрана"""
      
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     gun.output()
     inos.draw(screen)
     pygame.display.flip()


def update_bullets(bullets):
     """обновлять позиций пуль"""
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)

def create_army(screen , inos):
     """создание армии прищельцев"""
     ino = Ino(screen)
     ino_width = ino.rect.width
     number_ino_x = int((800 - 2*ino_width) / ino_width)
     ino_height = ino.rect.height
     number_ino_y = int((600 - 100 - 2* ino_height) / ino_height)

     for row_number in range(number_ino_y):
          for ino_number in range(number_ino_x):
               ino = Ino(screen)
               ino.x = ino_width + ino_width * ino_number
               ino.rect.x = ino.x
               inos.add(ino)
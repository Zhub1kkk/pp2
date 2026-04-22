import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного прищелца"""

    def __init__(self , screen ):
        """инициялизируем и задаем начальную позицию"""
        super(Ino , self ).__init__()
        self.screen = screen
        self.image = pygame.image.load('tsis\game1\images\pixil-frame-0 (1).png')
        self.rect= self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод прищельца на экран"""
        self.screen.blit(self.image , self.rect)
        

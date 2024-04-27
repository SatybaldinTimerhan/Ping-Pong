import pygame

FPS = 30
pygame.init()
window  = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()
class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, w, h, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, path, w, h, x, y):
        super().__init__(path, w, h, x, y)
        self.dx = 0

    def update(self):
        self.rect.x += self.dx


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
    clock.tick(FPS)
    
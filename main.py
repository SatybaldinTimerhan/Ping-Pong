import pygame

FPS = 30
pygame.init()
window  = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
    clock.tick(FPS)
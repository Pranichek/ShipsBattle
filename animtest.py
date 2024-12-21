import pygame
from class_frame_animation import AnimatedSprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animated Sprite")
clock = pygame.time.Clock()


frame_paths_test = ["media/boom_animation",49]


animated_sprite = AnimatedSprite(frame_paths_test, animation_speed=1,size=(100,100))
animated_sprite.set_position(200, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    
    animated_sprite.update()
    
    

    
    screen.fill((0, 0, 0))
    screen.blit(animated_sprite.image, animated_sprite.rect)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
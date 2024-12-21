import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frame_paths, animation_speed=10, initial_frame=0, size=None):
      
        super().__init__()
        self.frame = []
        self.number = 0
        self.frame_paths = frame_paths
        
        
        
        while self.number < self.frame_paths[1]:
            self.frame.append(f"{self.frame_paths[0]}\\{self.number}.png")
            self.number += 1
        

        
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(path).convert_alpha(),
                size
            ) if size else pygame.image.load(path).convert_alpha()
            for path in self.frame
        ]
        self.animation_speed = animation_speed
        self.current_frame = initial_frame
        
        self.image = self.frames[self.current_frame]  
        self.rect = self.image.get_rect()
        self.frame_count = 0

    def update(self):
        
        
    
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_current_frame(self):
        return self.current_frame

    def set_current_frame(self, frame):
        if 0 <= frame < len(self.frames):
            self.current_frame = frame
            self.image = self.frames[self.current_frame]
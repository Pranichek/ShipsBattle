import pygame
import os

class Animation():
    def __init__(self , image_name : int, folder_name : int , count_images : int , speed_animation : int , x_cor : int , y_cor : int):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.speed_animation = speed_animation
        self.count_images = count_images
        self.folder_name = folder_name  
        self.image_name = image_name
        self.list_images = []
        self.count_images = 0
        self.count_main_loop = 0
        self.image = None

    def load_images(self):
        path = os.path.abspath(__file__ + f"/../../../media/{self.folder_name}/{self.image_name}")
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(image , (62 , 62))
        self.image = transformed_image
    
    def animation(self, count_image: int , name_folder , screen: pygame.Surface):
        if len(self.list_images) == 0:
            for number in range(count_image):
                self.image_name = f'/../../../media/{name_folder}/{number}.png'
                self.load_images()
                self.list_images.append(self.image)

        
        self.image = self.list_images[self.count_images]
        self.draw(screen = screen)

        if self.count_main_loop >= self.speed_animation:
            if self.count_images < count_image - 1:
                self.count_images += 1
            else:
                self.count_images = 0
            self.count_main_loop = 0
        self.count_main_loop += 1

    def draw(self , screen : pygame.Surface):
        screen.blit(self.image , (self.x_cor , self.y_cor))
    # def check_event(self , screen : pygame.Surface):
    #     self.animation(count_image = self.count_images , name_folder = f"/../../../media/{self.folder_name}" , main_screen = screen)
import pygame
import os

#  робимо клас для фонового зображення
class DrawImage:
        def __init__(self,width:int , height:int , x_cor:int , y_cor:str , folder_name:str , image_name:str):
              self.width = width
              self.height = height
              self.x_cor = x_cor
              self.y_cor = y_cor
              self.folder_name = folder_name
              self.image_name = image_name
              #свойство для хранения загруженую картинку
              self.image = None
              self.load_image()
        def load_image(self):
            #__file__ - хранит путь именно в нашем проекте , в файле котором мі его создали
            #/.. - выход из текущего пути на один шаг назад
            image_path = os.path.abspath(__file__ + f"/../../../images/{self.folder_name}/{self.image_name}")
            load_image = pygame.image.load(image_path)
            #получаем картинку по пути корой написали , и трансформируем по нужному размеру
            transformed_image = pygame.transform.scale(load_image, (self.width,self.height))
            self.image = transformed_image
        def draw_image(self, screen:pygame.Surface):
              #blit  -  рисует картинку на екране
              #рисуем нужную картинку , по заданым координатам
              screen.blit(self.image, (self.x_cor, self.y_cor))

  

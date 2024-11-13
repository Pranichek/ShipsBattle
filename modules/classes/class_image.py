import pygame
import os

#створюємо клас , для зручного та швидкого додавання картинки на екран
class DrawImage:
        #Створюємо метод конструктор класу ,з параметрами зображення: розміри, координати, папка де зберігається зображення та назва зображення.
        def __init__(self,width:int , height:int , x_cor:int , y_cor:str , folder_name:str , image_name:str):
              #задаємо значения властивостям класу
              self.width = width
              self.height = height
              self.x_cor = x_cor
              self.y_cor = y_cor
              self.folder_name = folder_name
              self.image_name = image_name
              #створюємо властивість для збереження загруженого зображення
              self.image = None
              #викликаємо метод завантаження зображення
              self.load_image()
        #створюємо метод для завантаження зображення з файлової системи
        def load_image(self):
            #__file__ - хранит путь именно в нашем проекте , в файле котором мы его создали
            #/.. - выход из текущего пути на один шаг назад
            image_path = os.path.abspath(__file__ + f"/../../../images/{self.folder_name}/{self.image_name}")
            #завантажуємо зображення по вказаному шляху
            load_image = pygame.image.load(image_path)
            #змінюємо зображення яке отримали у 25 рядку, по потрібному розміру
            transformed_image = pygame.transform.scale(load_image, (self.width,self.height))
            # Зберігаємо трансформоване зображення у властивість self.image, щоб його можна було використовувати далі.
            self.image = transformed_image
        #Метод draw_image відповідає за відображення зображення на екрані
        def draw_image(self, screen:pygame.Surface):
              #blit — метод(функція), що дозволяє відображати зображення на вказаній поверхні(екрані)
              # Ми передаємо об'єкт зображення (self.image) та координати, на яких воно з'явиться
              screen.blit(self.image, (self.x_cor, self.y_cor))

  

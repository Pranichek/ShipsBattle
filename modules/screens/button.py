import pygame

class Button:
    def __init__(self, x, y, width, height, color, hover_color, action):
        # Инициализируем кнопку с цветом, цветом при наведении и необязательным действием
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        
        # Создаем прямоугольник для кнопки для проверки столкновений
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        # Получаем текущую позицию мыши
        mouse_pos = pygame.mouse.get_pos()
        
        # Проверяем, находится ли мышь над кнопкой
        if self.rect.collidepoint(mouse_pos):
            # Рисуем кнопку с цветом при наведении, если мышь над кнопкой
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            # Рисуем кнопку с обычным цветом, если мышь не над кнопкой
            pygame.draw.rect(surface, self.color, self.rect)

    def check_click(self):
        # Проверяем, был ли клик мыши в области кнопки
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            if self.action:
                self.action()  # Выполняем действие при нажатии на кнопку
import pygame

def apply_fade_effect(screen, fade_speed=3, max_fade_alpha=76):
    #fade_speed=3 -скорочть затемнения 
    #max_fade_alpha=76 -максимальное затемнение  до 255
    # Создаём полупрозрачную поверхность для затемнения
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))  # Черный цвет
    overlay.set_alpha(0)  # Начальная прозрачность (0 - полностью прозрачный)

    # Постепенное увеличение альфа-канала для эффекта затемнения
    while overlay.get_alpha() < max_fade_alpha:
        # Увеличиваем альфа-канал с каждой итерацией
        overlay.set_alpha(min(overlay.get_alpha() + fade_speed, max_fade_alpha))

        # Отображаем затемнение
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
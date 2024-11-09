import pygame
import modules.screens.server_screen as server_module_screen
from ..json_functions import write_json , list_users
from ..screens import screen_server


pygame.init()





def start_game():
    user_ip = ''
    font = pygame.font.SysFont('frenchsript', 40)
    text_box = pygame.Rect((1280 // 2) - (100 //2),(832 // 2) - (50 // 2),100,50)
    activa = False
    color = pygame.Color("Red")
    run_game = True
    while run_game:
        server_module_screen.FPS.tick(60)
        server_module_screen.screen_server.fill((255 , 192 , 203))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    activa = True
                else:
                    activa = False
            
            if event.type == pygame.KEYDOWN:
                if activa:
                    if len(user_ip) < 10 or event.key == pygame.K_BACKSPACE:
                        print("get in")
                        if event.key == pygame.K_BACKSPACE:
                            user_ip = user_ip[:-1]
                        else:
                            if event.key == pygame.K_RETURN:
                                pass
                            else:
                                user_ip += event.unicode

                        if event.key == pygame.K_RETURN:
                            print(user_ip)
                            if len(user_ip) > 0:
                                if user_ip not in list_users:
                                    list_users[user_ip] = {"points": 0}
                                    write_json(filename = "data_base.json")


                            # if len(user_ip) > 0:
                            #     write_json(filename = "data_base.json", object_to_load = user_ip)
                        
                    
        if activa:
            color = pygame.Color("red")
        else:
            color = pygame.Color("white")
        pygame.draw.rect(screen_server , color , text_box , 4)
        surf = font.render(user_ip , True, "black")
        screen_server.blit(surf , (text_box.x + 5 , text_box.y + 5))
        text_box.w = max(100 , surf.get_width() + 10)
        pygame.display.flip()
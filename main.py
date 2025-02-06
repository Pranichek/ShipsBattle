import modules


if __name__ == '__main__':
    modules.list_current_scene[0] = modules.main_window#передаем функцию отображения первого окна
    while modules.list_current_scene[0] != "END GAME":
        # try:
        modules.list_current_scene[0]()#вызываем функцию которая тут запущен
        # except:
        #     continue

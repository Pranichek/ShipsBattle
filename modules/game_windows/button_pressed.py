from ..classes.class_click import music_click
# список в котором храним нажата ли кнопка
check_press_button = [None]
def button_action():
    check_press_button[0] = "button is pressed"
    music_click.play2(0)

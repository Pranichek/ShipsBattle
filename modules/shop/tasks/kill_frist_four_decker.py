from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv, player_died_ships_for_achiv
from..shop_button import second_tasks_copy
from ..shop_image import shop_item, done_task_two
our_ships_4decker = [0]
enemy_ships_4decker = [0]
def first_kill_four_decker():
    if enemy_dies_ships_for_ahiv[0] != 0:
        if enemy_ships_4decker[0] != "kill four-decker ship":
            if type(enemy_dies_ships_for_ahiv[0]) != str:
                our_ships_4decker[0] = 0
                enemy_ships_4decker[0] = 0

                our_ships_4decker[0] = 1 -player_died_ships_for_achiv[0].count(4)
                enemy_ships_4decker[0] = 1 - enemy_dies_ships_for_ahiv[0].count(4)

                if enemy_ships_4decker[0] != "kill four-decker ship":
                    if our_ships_4decker[0] > enemy_ships_4decker[0] and enemy_ships_4decker[0] == 0 and enemy_ships_4decker[0]!= "kill four-decker ship":
                        enemy_ships_4decker[0] = "kill four-decker ship"
                        check_completed_tasks[0] += 1
                        print("Ты первым убил четырехпалубный корабль")
                        del second_tasks_copy[0]
                        if done_task_two.VISIBLE != 255:
                            done_task_two.VISIBLE = 255


from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv, player_died_ships_for_achiv
from ..shop_button import second_tasks_copy
from ..shop_image import done_task_two, shop_item

our_ships_2decker = [0]
enemy_ships_2decker = [0]
def first_kill_two_decker():
    if enemy_dies_ships_for_ahiv[0] != 0:
        if enemy_ships_2decker[0] != "kill two-decker ship":
            if type(enemy_dies_ships_for_ahiv[0]) != str:
                our_ships_2decker[0] = 0
                enemy_ships_2decker[0] = 0

                our_ships_2decker[0] = 3 - player_died_ships_for_achiv[0].count(2)
                enemy_ships_2decker[0] = 3 - enemy_dies_ships_for_ahiv[0].count(2)

                if enemy_ships_2decker[0] != "kill two-decker ship":
                    if our_ships_2decker[0] > enemy_ships_2decker[0] and enemy_ships_2decker[0] == 2 and enemy_ships_2decker[0]!= "kill two-decker ship":
                        enemy_ships_2decker[0] = "kill two-decker ship"
                        check_completed_tasks[0] += 1
                        print("Ты первым убил двух палубный корабль")
                        del second_tasks_copy[0]
                        if done_task_two.VISIBLE <= 254 and enemy_ships_2decker[0] == "kill two-decker ship":
                            done_task_two.VISIBLE = 255
        else:
            if done_task_two.VISIBLE <= 254:
                done_task_two.VISIBLE = 255

from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv
from ..shop_button import fourth_tasks_copy
from ..shop_image import shop_item, done_task_four

ship_hits_three = []
count_zero_thrible = [0]
count_kill_three = [0]
def kill_three_ships_in_a_row():
    try:
        if enemy_dies_ships_for_ahiv[0] != "":
            if count_kill_three[0] != "You killes three ships in row":
                count_kill_three[0] = len(enemy_dies_ships_for_ahiv[0]) - count_zero_thrible[0]

                if 0 in ship_hits_three or 5 in ship_hits_three:
                    count_zero_thrible[0] += 1
                    ship_hits_three.clear()
                    count_kill_three[0] = 0
                    return False
                
                if count_kill_three[0] >= 3:
                    count_kill_three[0] = "You killes three ships in row"
                    check_completed_tasks[0] += 1
                    print("Ты убил три корабля подряд")
                    del fourth_tasks_copy[1]
                    if done_task_four.VISIBLE != 255:
                        done_task_four.VISIBLE = 255
    except:
        pass
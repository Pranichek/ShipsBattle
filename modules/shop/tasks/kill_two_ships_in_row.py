from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv

# kill two ships in a row
ship_hits = []
kill_count = [0]
count_zero = [0]
def kill_two_ships_in_a_row():
    if enemy_dies_ships_for_ahiv[0] != "":
        if kill_count[0] != "Kill two ships":
            kill_count[0] = len(enemy_dies_ships_for_ahiv[0]) - count_zero[0] 

            if 0 in ship_hits or 5 in ship_hits:
                count_zero[0] += 1
                ship_hits.clear()
                kill_count[0] = 0
                return False

            if kill_count[0] >= 2:
                kill_count[0] = "Kill two ships"
                check_completed_tasks[0] += 1
                print("Ты убил два корабля подряд")
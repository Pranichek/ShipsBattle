from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv

kill_three_deckcer_ship = [0]
def kill_one_three_decker_ship():
    if enemy_dies_ships_for_ahiv[0] != 0:
        if kill_three_deckcer_ship[0] != "kill three deck ship":
            if 3 in enemy_dies_ships_for_ahiv[0]:
                kill_three_deckcer_ship[0] += 1
            if kill_three_deckcer_ship[0] >= 1:
                kill_three_deckcer_ship[0] = "kill three deck ship"
                check_completed_tasks[0] += 1
                print("Ты убил один трехбалубный кораблик")
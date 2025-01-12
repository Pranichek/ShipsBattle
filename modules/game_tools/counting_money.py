import modules.shop as task_game
from ..screens import main_screen
from ..classes import Font
from ..server import enemy_balance


player_balance_in_jar = Font(
    x_cor = 1219 ,
    y_cor = 45 ,
    size = 36,
    name_font = "Jersey15.ttf",
    text = str(task_game.money_list[0]),
    text_color = "Yellow",
    screen = main_screen
)
enemy_balance_in_jar = Font(
    x_cor = 125 ,
    y_cor = 45 ,
    size = 36 ,
    name_font = "Jersey15.ttf",
    text = str(enemy_balance[0]),
    text_color = "Yellow",
    screen = main_screen
)


# для двух попаданий подряд
check_money_two_hits_in_row = [0]
# для четрыех попаданий подряд
check_money_four_hits_in_row = [0]
# для убийства одного трехабловбного корабля
check_kill_one_3deck = [0]
# для того когда убил два корабля подряд
check_money_two_kill_in_a_row = [0]
# для того когда убил два трехпалубных кораблей подряд
check_2_kills_3deck_in_row = [0]
# для того когда убил первым четырех палубный корабль
check_kill_first_four_deck = [0]
# для того чтобы убить четыре однопалубных кораблей подряд
check_kill_four_1decker_in_row = [0]
# для того чтобы когда убил корабль с первой попытки
check_kill_in_first_shot = [0]
# для того когда соперник не попал по твои кораблям 7 раз
check_kept_alive_for_5_turns = [0]
# для того чтобы убить три корабля подряд
check_kill_three_ships_in_row = [0]
# сделать первые три задания
check_completed_three_tasks = [0]
# три попадания подряд
check_money_three_hits_in_row = [0]
# первый убил трехпалубный 
check_first_kill_three_3dec = [0]
# 8 попаданий подряд
check_money_eight_hits_in_row = [0]
# убить три двухпалубных кораблей подряд
check_three_2decker_ship_in_row = [0]


# при покупке бомбы
check_money_bomb = [0]
def count_money(check_buy_bomb: bool):
    # print(task_game.check_completed_tasks[0] , "completed task")
    # print("check_money_two_hits_in_row:", check_money_two_hits_in_row[0])

    # print("check_money_four_hits_in_row:", check_money_four_hits_in_row[0])

    # print("check_kill_one_3deck:", check_kill_one_3deck[0])


    # print("check_money_two_kill_in_a_row:", check_money_two_kill_in_a_row[0])

    # print("check_2_kills_3deck_in_row:", check_2_kills_3deck_in_row[0])


    # print("check_kill_first_four_deck:", check_kill_first_four_deck[0])


    # print("check_three_2decker_ship_in_row:", check_three_2decker_ship_in_row[0])

    # print("check_kill_four_1decker_in_row:", check_kill_four_1decker_in_row[0])

    # print("check_kill_in_first_shot:", check_kill_in_first_shot[0])


    # print("check_kept_alive_for_5_turns:", check_kept_alive_for_5_turns[0])

   
    # print("check_kill_three_ships_in_row:", check_kill_three_ships_in_row[0])


    # print("check_completed_three_tasks:", check_completed_three_tasks[0])


    # print("check_money_three_hits_in_row:", check_money_three_hits_in_row[0])

    # print("check_first_kill_three_3dec:", check_first_kill_three_3dec[0])

    # print("check_money_eight_hits_in_row:", check_money_eight_hits_in_row[0])

    if check_buy_bomb == True and check_money_bomb[0] == 0:
        check_money_bomb[0] += 1
        task_game.money_list[0] -= 0
        task_game.player_balance.TEXT = str(task_game.money_list[0])
        task_game.player_balance.update_text()
        player_balance_in_jar.text = str(task_game.money_list[0])
        player_balance_in_jar.update_text()
    if check_money_bomb[0] >= 1:
        if check_money_bomb[0] != 10:
            check_money_bomb[0] += 1
            task_game.money_list[0] -= 0
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()
        elif check_buy_bomb == False and check_money_bomb[0] >= 10:
            check_money_bomb[0] = 0

    
    if "True" in task_game.two_hits_in_a_row:
        if check_money_two_hits_in_row[0] != 30:
            check_money_two_hits_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "True" in task_game.four_hits_in_a_row:
        if check_money_four_hits_in_row[0] != 30:
            check_money_four_hits_in_row[0] += 1 
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if task_game.kill_three_deckcer_ship[0] == "kill three deck ship":
        if check_kill_one_3deck[0]!= 30:
            check_kill_one_3deck[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if task_game.kill_count[0] == "Kill two ships":
        if check_money_two_kill_in_a_row[0] != 50:
            check_money_two_kill_in_a_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()
            

    if "You kill three double decker in row" in task_game.check_three_2decker_ship_in_row:
        if check_three_2decker_ship_in_row[0] != 80:
            check_three_2decker_ship_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()
    
    if task_game.enemy_ships_4decker[0] == "kill four-decker ship":
        if check_kill_first_four_deck[0] != 80:
            check_kill_first_four_deck[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "Kill two three decker in a row" in task_game.count_three_ships:
        if check_2_kills_3deck_in_row[0] != 80:
            check_2_kills_3deck_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "Kill four single ships in a row" in task_game.single_ships:
        if check_kill_four_1decker_in_row[0] != 80:
            check_kill_four_1decker_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "You are kill ship in one shot" in task_game.count_shot:
        if check_kill_in_first_shot[0] != 100:
            check_kill_in_first_shot[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "True" in task_game.count_turns:
        if check_kept_alive_for_5_turns[0] != 50:
            check_kept_alive_for_5_turns[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()
            

    if "You killes three ships in row" == task_game.count_kill_three[0]:
        if check_kill_three_ships_in_row[0] != 100:
            check_kill_three_ships_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if task_game.check_completed_tasks[0] == 999:
        if check_completed_three_tasks[0]!= 100:
            check_completed_three_tasks[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "True" in task_game.three_hits_in_a_row:
        if check_money_three_hits_in_row[0] != 30:
            check_money_three_hits_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()

    if "kill three-decker ship" == task_game.enemy_ships_3decker[0]:
        if check_first_kill_three_3dec[0]!= 50:
            check_first_kill_three_3dec[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()


    if "True" in task_game.egight_hits_in_a_row:
        if check_money_eight_hits_in_row[0] != 100:
            check_money_eight_hits_in_row[0] += 1
            task_game.money_list[0] += 1
            task_game.player_balance.TEXT = str(task_game.money_list[0])
            task_game.player_balance.update_text()
            player_balance_in_jar.x_cor = 1219
            player_balance_in_jar.text = str(task_game.money_list[0])
            player_balance_in_jar.update_text()
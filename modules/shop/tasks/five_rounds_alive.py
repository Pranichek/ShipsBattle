from .did_three_tasks import check_completed_tasks
from ..shop_button import second_tasks_copy
from ..shop_image import shop_item, done_task_two

#2  выжить 5 раз чтобы твои корабли не подбили ниразу
count_turns = [0]
save_sevens = []
def kept_all_ships_alive_for_five_turns(grid: object):
    try:
        count_turns[0] += 1
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == 7 and (row * 10) + cell not in save_sevens:
                    count_turns[0] = 0
                    save_sevens.append((row * 10) + cell)

        if count_turns[0] >= 6 and "True" not in count_turns:
            print("У тебя целы корабли 5 раундов")
            check_completed_tasks[0] += 1
            count_turns.append("True")
            if done_task_two.VISIBLE != 255 and "True" in count_turns:
                done_task_two.VISIBLE = 255
    except:
        pass

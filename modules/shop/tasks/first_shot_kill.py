from .did_three_tasks import check_completed_tasks
from ...screens import list_grid
from ..shop_button import fourth_tasks_copy
from..shop_image import done_task_four, shop_item

# первый удар убийство
count_shot = [0]
def first_shot_is_kill(cell):
    count_shot[0] += 1
    if cell == 1 and count_shot[0] == 1:
        count_shot.append("You are kill ship in one shot")
        check_completed_tasks[0] += 1
        print("You are first shot is kill")
        if "You are kill ship in one shot" in count_shot and done_task_four.VISIBLE != 255:
            done_task_four.VISIBLE = 255

from .did_three_tasks import check_completed_tasks

# первый удар убийство
count_shot = [0]
def first_shot_is_kill(cell):
    count_shot[0] += 1
    if cell == 1 and count_shot[0] == 1:
        count_shot.append("You are kill ship in one shot")
        check_completed_tasks[0] += 1
        print("You are first shot is kill")
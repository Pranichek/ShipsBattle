check_completed_tasks = [0]
def complete_three_tasks():
    if check_completed_tasks[0] != 999:
        if check_completed_tasks[0] == 3:
            check_completed_tasks[0] = 999
            print("Ты выполнил все три завдання")